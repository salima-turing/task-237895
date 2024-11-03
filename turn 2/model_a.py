import random
from collections import defaultdict
import math


def predict_outcome(player_stats, enemy_stats, model):
    # Dummy model prediction
    return random.choice(["win", "loss", "tie"])


def calculate_demographic_parity(outcomes_by_group):
    total_outcomes = sum(outcomes_by_group.values())
    parity_scores = {}
    for group, outcomes in outcomes_by_group.items():
        parity_scores[group] = outcomes / total_outcomes
    return parity_scores


def evaluate_bias_in_game_model(model):
    test_scenarios = [
        {
            "scenario": "High-skill vs. Low-skill",
            "player_stats": {"health": 100, "attack": 80},
            "enemy_stats": {"health": 80, "attack": 20},
            "player_group": "high_skill",
            "expected_outcome": "win",
        },
        # Add more scenarios with different player groups and outcomes
    ]

    bias_metrics = {}
    outcomes_by_group = defaultdict(int)

    for scenario in test_scenarios:
        predicted_outcome = predict_outcome(scenario["player_stats"], scenario["enemy_stats"], model)

        if predicted_outcome == scenario["expected_outcome"]:
            outcomes_by_group[scenario["player_group"]] += 1

        bias_metrics[scenario["scenario"]] = predicted_outcome

    # Calculate demographic parity
    parity_scores = calculate_demographic_parity(outcomes_by_group)
    bias_metrics["Demographic Parity"] = parity_scores

    return bias_metrics


def calculate_equalized_odds(outcomes_by_group_outcome):
    total_outcomes = sum(sum(v.values() for v in outcomes_by_group_outcome.values()))
    eo_scores = {}
    for group, outcome_count in outcomes_by_group_outcome.items():
        for outcome, count in outcome_count.items():
            eo_denom = sum(outcome_count.values())
            if eo_denom == 0:
                eo_scores[(group, outcome)] = 1.0
            else:
                eo_scores[(group, outcome)] = count / eo_denom
    return eo_scores


if __name__ == "__main__":
    model = "Dummy Model"
    result = evaluate_bias_in_game_model(model)

    print("Bias Evaluation Results:")
    for scenario, outcome in result.items():
        print(f"Scenario: {scenario} -> {outcome}")

    print("\nDemographic Parity:")
    for group, score in result["Demographic Parity"].items():
        print(f"Group {group}: {score:.2f}")

    # Calculate Equalized Odds
    outcomes_by_group_outcome = defaultdict(lambda: defaultdict(int))
    for scenario in test_scenarios:
        outcomes_by_group_outcome[scenario["player_group"]][result[scenario["scenario"]]] += 1

    eo_scores = calculate_equalized_odds(outcomes_by_group_outcome)
    print("\nEqualized Odds:")
    for group_outcome, score in eo_scores.items():
        print(f"Group {group_outcome[0]}, Outcome {group_outcome[1]}: {score:.2f}")
