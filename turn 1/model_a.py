import random


def predict_outcome(player_stats, enemy_stats, model):
    # Dummy model prediction for demonstration purposes
    return random.choice(["win", "loss", "tie"])


def evaluate_bias_in_game_model(model):
    test_scenarios = [
        {
            "scenario": "High-skill vs. Low-skill",
            "player_stats": {"health": 100, "attack": 80},
            "enemy_stats": {"health": 80, "attack": 20},
            "expected_outcome": "win",
        },
        {
            "scenario": "Low-skill vs. High-skill",
            "player_stats": {"health": 80, "attack": 20},
            "enemy_stats": {"health": 100, "attack": 80},
            "expected_outcome": "loss",
        },
        {
            "scenario": "Equal skill",
            "player_stats": {"health": 90, "attack": 70},
            "enemy_stats": {"health": 90, "attack": 70},
            "expected_outcome": "tie",
        },
    ]

    bias_metrics = {}

    for scenario in test_scenarios:
        predicted_outcome = predict_outcome(scenario["player_stats"], scenario["enemy_stats"], model)

        if predicted_outcome != scenario["expected_outcome"]:
            bias_metrics[scenario["scenario"]] = "Bias detected!"
        else:
            bias_metrics[scenario["scenario"]] = "No bias detected"

    return bias_metrics


if __name__ == "__main__":
    # Dummy model
    model = "Dummy Model"
    result = evaluate_bias_in_game_model(model)
    print("Bias Evaluation Results:")
    for scenario, outcome in result.items():
        print(f"Scenario: {scenario} -> {outcome}")
