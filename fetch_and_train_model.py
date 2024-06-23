import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from xgboost import XGBRegressor
import joblib
from sklearn.metrics import mean_absolute_error

# Load the dataset
df = pd.read_csv('player_last_10_games.csv')

# Feature Engineering: Adding more features
df['Home/Away'] = df['MATCHUP'].apply(lambda x: 1 if 'vs.' in x else 0)
df['Opponent'] = df['MATCHUP'].apply(lambda x: x.split()[-1])

# One-hot encode the categorical features
X = pd.get_dummies(df[['Opponent', 'Home/Away']], columns=['Opponent'])
y = df['PTS']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the XGBoost model
model = XGBRegressor(objective='reg:squarederror', random_state=42)

# Hyperparameter tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.3],
    'subsample': [0.6, 0.8, 1.0]
}

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring='neg_mean_absolute_error', cv=5, verbose=1)
grid_search.fit(X_train, y_train)

# Best model from grid search
best_model = grid_search.best_estimator_

# Evaluate the model
y_pred = best_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Save the best model
joblib.dump(best_model, 'xgboost_model.pkl')

print("Model trained and saved as xgboost_model.pkl")
