import random


def flip_coin():
    return random.choice(['H', 'T'])


def longest_streak(simulation):
    longest = 0
    current_streak = 0

    for flip in simulation:
        if flip == 'H':
            current_streak += 1
            longest = max(longest, current_streak)
        else:
            current_streak = 0

    return longest


def monte_carlo_simulation(num_simulations=1000):
    streak_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    for _ in range(num_simulations):
        simulation = [flip_coin() for _ in range(5)]
        streak = longest_streak(simulation)
        if streak in streak_counts:
            streak_counts[streak] += 1

    probabilities = {streak: count / num_simulations for streak, count in streak_counts.items()}

    return probabilities


if __name__ == "__main__":
    probabilities = monte_carlo_simulation()
    for streak, probability in probabilities.items():
        print(f"The probability of the longest streak of heads being {streak} is approximately {probability:.4f}")