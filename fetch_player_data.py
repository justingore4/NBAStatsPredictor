import pandas as pd
from nba_api.stats.endpoints import playergamelog
from config import players, valid_teams
import time
from requests.exceptions import ReadTimeout

# Function to fetch player game logs for all available seasons
def fetch_player_game_log(player_id, timeout=60):
    all_data = []
    # Fetch game logs for all available seasons
    seasons = ['2022-23', '2021-22', '2020-21']
    for season in seasons:
        for attempt in range(3):  # Retry up to 3 times
            try:
                gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season, season_type_all_star='Regular Season', timeout=timeout)
                df = gamelog.get_data_frames()[0]
                if not df.empty:
                    all_data.append(df)
                break
            except ReadTimeout:
                print(f"Timeout occurred. Retrying... ({attempt + 1}/3)")
                time.sleep(5)  # Wait for 5 seconds before retrying
            except Exception as e:
                print(f"An error occurred: {e}")
                break

    # Concatenate all non-empty data frames into a single data frame
    if all_data:
        df_all_seasons = pd.concat(all_data, ignore_index=True)
        df_all_seasons = df_all_seasons.sort_values(by='GAME_DATE', ascending=False)
        return df_all_seasons
    else:
        return pd.DataFrame()  # Return an empty DataFrame if no data is available

# Initialize an empty list to store the player data
player_data = []

# Loop through each player to fetch their game logs
for player in players:
    player_id = player['Player ID']
    player_name = player['Player Name']
    player_team = player['Team']
    print(f"Fetching game logs for {player_name}")
    df = fetch_player_game_log(player_id)
    if not df.empty:
        for team in valid_teams:
            # Skip the player's own team
            if player_team == team:
                continue
            df_team = df[df['MATCHUP'].str.contains(team)]
            if not df_team.empty:
                df_team = df_team.head(10)  # Get the last 10 games
                df_team = df_team[['PTS', 'MATCHUP']]  # Only keep points and matchup
                df_team['Player Name'] = player_name
                df_team['Player ID'] = player_id
                df_team['Opponent Team'] = team
                player_data.append(df_team)
        # Throttle requests to avoid hitting the API rate limit
        time.sleep(2)  # Wait for 2 seconds before processing the next player

# Concatenate all player data into a single DataFrame
if player_data:
    all_player_data = pd.concat(player_data, ignore_index=True)
    # Save the data to a CSV file
    all_player_data.to_csv('player_last_10_games.csv', index=False)
    print("Player data saved to player_last_10_games.csv")
else:
    print("No player data available to save.")
