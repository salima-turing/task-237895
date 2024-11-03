import random


# Dummy function to categorize players into groups based on an attribute (e.g., gender, skill level)
def categorize_players(player_stats, group_attr):
    if group_attr == "gender":
        # Dummy logic for gender categorization based on a fake attribute
        return "female" if player_stats["health"] > 90 else "male"
    elif group_attr == "skill_level":
        # Dummy logic for skill level categorization based on attack stat
        return "high" if player_stats["attack"] > 60 else "low"


def predict_outcome(player_stats, enemy_stats, model):
    # Dummy model prediction
    return random.choice(["win", "loss", "tie"])


def calculate_fairness_metric(test_results, group_attr):
    groups = {}
    for result in test_results:
        player_group = categorize_players(result["player_stats"], group_attr)
        outcome = result["predicted_outcome"]

        if player_group not in groups:
            groups[player_group] = {
                "total_outcomes": 0,
                "favorable_outcomes": 0,
            }
        groups[player_group]["total_outcomes"] += 1
        if outcome == "win":
            groups[player_group]["favorable_outcomes"] += 1

    pfm_values = {}
    for group1, group2 in ((groups.keys()[0], groups.keys()[1]), (groups.keys()[1], groups.keys()[0])):
        pfm = abs((groups[group1]["favorable_outcomes"] / groups[group1]["total_outcomes"]) -
                  (groups[group2]["favorable_outcomes"] / groups[group2]["total_outcomes"]))
        pfm_values[f"{group1} vs. {group2}"] = pfm

    return pfm_values


def evaluate_bias_in_game_model(model, group_attr):
    test_scenarios = [
        # Dummy test scenarios with varying player attributes
    ]

    test_results = []
    for scenario in test_scenarios:
        predicted_outcome = predict_outcome(scenario["player_stats"], scenario["enemy_stats"], model)
        test_results.append({"player_stats": scenario["player_stats"], "predicted_outcome": predicted_outcome})

    pfm_values = calculate_fairness_metric(test_results, group_attr)

    return pfm_values


if __name__ == "__main__":
    # Dummy model
    model = "Dummy Model"

    # Evaluating bias for gender attribute
    print("PFM Results for Gender attribute:")
    gender_bias_metrics = evaluate_bias_in_game_model(model, group_attr="gender")
    for group_comparison, pfm in gender_bias_metrics.items():
        print(f"Scenario: {group_comparison} -> PFM: {pfm:.2f}")

    # Evaluating bias for skill_level attribute
    print("\nPFM Results for Skill_level attribute:")
    skill_bias_metrics = evaluate_bias_in_game_model(model, group_attr="skill_level")
    for group_comparison, pfm in skill_bias_metrics.items():
        print(f"Scenario: {group_comparison} -> PFM: {pfm:.2f}")
