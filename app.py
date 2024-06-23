from flask import Flask, request, render_template, url_for
import joblib
import pandas as pd
import numpy as np
from config import players, valid_teams, team_names

app = Flask(__name__)
model = joblib.load('xgboost_model.pkl')

@app.route('/')
def home():
    return render_template('index.html', players=players, teams=valid_teams, team_names=team_names)

@app.route('/predict', methods=['POST'])
def predict():
    player_id = request.form['player_id']
    team = request.form['team'].upper()
    last_n_games = int(request.form['last_n_games'])

    # Validate the team input
    if team not in valid_teams:
        return render_template('prediction_result.html', prediction='Invalid team abbreviation')

    # Check if the player is predicting against their own team
    player_team = next(player['Team'] for player in players if player['Player ID'] == int(player_id))
    if team == player_team:
        return render_template('prediction_result.html', prediction='Unable to predict against self')

    # Load the CSV data
    df = pd.read_csv('player_last_10_games.csv')

    # Filter the data for the specific player and team
    df_player_team = df[(df['Player ID'] == int(player_id)) & (df['Opponent Team'] == team)]

    # Get the last n games
    df_player_team = df_player_team.head(last_n_games)

    if df_player_team.empty:
        return render_template('prediction_result.html', prediction='No data available for this player and team')

    # Feature Engineering: Adding more features
    df_player_team['Home/Away'] = df_player_team['MATCHUP'].apply(lambda x: 1 if 'vs.' in x else 0)
    df_player_team['Opponent'] = df_player_team['MATCHUP'].apply(lambda x: x.split()[-1])

    # One-hot encode the categorical features
    X = pd.get_dummies(df_player_team[['Opponent', 'Home/Away']], columns=['Opponent'])

    # Ensure the columns match the training data
    X = X.reindex(columns=model.get_booster().feature_names, fill_value=0)

    # Make predictions
    prediction = model.predict(X)
    avg_points = np.mean(prediction)

    # Get player name and team name
    player_name = next(player['Player Name'] for player in players if player['Player ID'] == int(player_id))
    team_name = team_names[team]
    player_image = f"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{player_id}.png"

    return render_template('prediction_result.html',
                           prediction=f'{player_name} is predicted to score {avg_points:.2f} points against {team_name}',
                           player_image=player_image)

if __name__ == '__main__':
    app.run(debug=True)
