import numpy as np
import matplotlib.pyplot as plt
plt.close("all")
np.random.seed(2017)


def p_longest_streak(n, tries):
    # Write your Monte Carlo code here, n is the length of the sequence and tries is the number
    # of sampled sequences used to produce the estimate of the probability
    bucket = dict([(i, 0) for i in range(n+1)]) # count the number of sequences with longest streaks of number 1,2,,...,n
    for ind_trial in range(tries):
        seq = []
        for i in range(n):
            r = np.random.random()
            if r >= 0.5:
                seq.append(1)
            else:
                seq.append(0)
        longest_streaks_num = longest_streaks_number(seq)
        bucket[longest_streaks_num] += 1
    return list(map(lambda x: x / tries, bucket.values()))


def longest_streaks_number(seq):
    # Compute the longest streak in a seq list
    longest = 0
    current_streak = 0

    for flip in seq:
        if flip == 1:
            current_streak += 1
            longest = max(longest, current_streak)
        else:
            current_streak = 0

    return longest



n_tries = [1e3,5e3,1e4,5e4,1e5]

n_vals = [5,200]

color_array = ['orange','darkorange','tomato','red', 'darkred', 'tomato', 'purple', 'grey', 'deepskyblue',
               'maroon','darkgray','darkorange', 'steelblue', 'forestgreen', 'silver']
for ind_n in range(len(n_vals)):
    n = n_vals[ind_n]
    plt.figure(figsize=(20,5))
    for ind_tries in range(len(n_tries)):
        tries = n_tries[ind_tries]
        print("tries: " + str(tries))
        p_longest_tries = p_longest_streak(n, int(tries))
        plt.plot(range(n+1),p_longest_tries, marker='o',markersize=6,linestyle="dashed",lw=2,
                 color=color_array[ind_tries],
                 markeredgecolor= color_array[ind_tries],label=str(tries))
    plt.legend()

plt.show()

if __name__ == "__main__":
    print("The probability that the longest streak of ones in a Bernoulli iid sequence of length 200 has length 8 or more is ")
    print(p_longest_streak(200, 1000)) # Compute the probability and print it here
