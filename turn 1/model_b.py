import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Dummy data generation (replace this with your actual data)
np.random.seed(0)
data = pd.DataFrame({
    'player_id': np.arange(1, 1001),
    'player_level': np.random.randint(1, 100, size=1000),
    'player_race': np.random.choice(['Human', 'Elf', 'Dwarf', 'Orc'], size=1000, p=[0.3, 0.2, 0.2, 0.3]),
    'game_mode': np.random.choice(['Easy', 'Medium', 'Hard'], size=1000),
    'win_rate': np.random.uniform(0, 1, size=1000),
    'outcome': np.where(np.random.uniform(0, 1, size=1000) < 0.5, 'Win', 'Loss')
})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop(columns=['outcome']), data['outcome'], test_size=0.2,
                                                    random_state=42)

# Train a Random Forest Classifier (replace with your AI model)
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy and print the classification report
accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Scenario-based testing: Analyze bias in specific scenarios
# Example: Let's analyze bias based on player race and game mode
race_bias = pd.crosstab(X_test['player_race'], y_test, normalize='index').loc[:, 'Win']
print("\nBias Analysis by Player Race:")
print(race_bias)

mode_bias = pd.crosstab(X_test['game_mode'], y_test, normalize='index').loc[:, 'Win']
print("\nBias Analysis by Game Mode:")
print(mode_bias)
