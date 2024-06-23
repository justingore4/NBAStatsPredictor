# AIverson Bets

AIverson Bets is a web application that predicts the points a specific NBA player will score against a particular team based on historical game data. By leveraging machine learning techniques and the NBA API, this tool provides accurate predictions for sports enthusiasts and bettors.

## Inspiration

The inspiration for AIverson Bets came from a desire to combine advanced machine learning techniques with sports analytics. By leveraging the vast amount of NBA data available, we aimed to create a tool that could provide accurate predictions on player performance, specifically points scored.

## What it does

AIverson Bets predicts the points a specific NBA player will score against a particular team based on historical game data. Users can select a player, an opponent team, and the number of recent games to be considered for the prediction. The app then uses a trained machine learning model to forecast the player's performance and displays the prediction along with a chart of the points scored in the selected number of recent games.

## How we built it

1. **Data Collection**: Used the NBA API to fetch historical game data for the selected players.
2. **Data Preprocessing**: Cleaned and organized the data, focusing on points scored and matchup details.
3. **Model Training**: Trained an XGBoost regression model using the preprocessed data.
4. **Web Application**: Developed a Flask-based web application to provide a user-friendly interface for making predictions. The front-end was styled using CSS, and Chart.js was integrated to visualize past performance data.
5. **Deployment**: Hosted the application locally for development and testing purposes.

## Challenges we ran into

1. **Data Fetching**: Handling API rate limits and timeouts while fetching large amounts of historical data.
2. **Feature Engineering**: Ensuring that the features used for model training were relevant and properly formatted.
3. **Model Accuracy**: Achieving high prediction accuracy required tuning the model and experimenting with different machine learning techniques.
4. **UI/UX**: Creating a seamless and intuitive user experience, particularly with the integration of dynamic charts and responsive design.

## Accomplishments that we're proud of

1. **Model Performance**: Successfully training a model that provides reasonably accurate predictions based on historical data.
2. **User Interface**: Developing a clean, responsive web application that allows users to easily interact with the model and visualize results.
3. **Integration**: Efficiently integrating various technologies (Flask, Chart.js, CSS) to create a cohesive application.

## What we learned

1. **API Handling**: Techniques for efficiently fetching and managing large datasets from APIs, including handling timeouts and retries.
2. **Machine Learning**: Improved understanding of feature engineering, model training, and performance evaluation.
3. **Web Development**: Enhanced skills in building full-stack web applications, particularly with Flask and front-end integrations.

## What's next for AIverson Bets

1. **Model Improvements**: Continuously improve the prediction model by incorporating more features and experimenting with different algorithms.
2. **Expanded Metrics**: Add predictions for other performance metrics such as rebounds, assists, and player efficiency ratings.
3. **User Authentication**: Implement user accounts and personalized settings to enhance user experience.
4. **Deployment**: Deploy the application on a cloud platform for broader accessibility and scalability.
5. **Live Updates**: Integrate live game updates and real-time predictions for ongoing games.

## Built with

- **Languages**: Python, HTML, CSS
- **Frameworks**: Flask, Chart.js
- **Platforms**: PyCharm
- **APIs**: NBA API
- **Libraries**: Pandas, NumPy, Joblib, XGBoost
- **Databases**: CSV Files

## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/AIversonBets.git
    cd AIversonBets
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python app.py
    ```

5. **Open your web browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact

If you have any questions or suggestions, feel free to reach out to me at justingore@ucla.edu

---

Enjoy predicting with AIverson Bets!
