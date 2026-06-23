#Nandhini sri V(192521344)
# Package details
packages = ['P1', 'P2', 'P3', 'P4']
weights = [10, 20, 30, 25]
profits = [60, 100, 120, 110]
capacity = 50
print("GREEDY APPROACH")

# Calculate profit-to-weight ratio
items = []

for i in range(len(packages)):
    ratio = profits[i] / weights[i]
    items.append((ratio, packages[i], weights[i], profits[i]))

# Sort according to ratio in descending order
items.sort(reverse=True)

selected_greedy = []
total_weight = 0
total_profit = 0

# Select packages greedily
for ratio, package, weight, profit in items:
    if total_weight + weight <= capacity:
        selected_greedy.append(package)
        total_weight += weight
        total_profit += profit

print("Selected Packages:", selected_greedy)
print("Total Weight =", total_weight, "kg")
print("Total Profit = Rs.", total_profit)

print("\nDYNAMIC PROGRAMMING APPROACH")

n = len(packages)

# Create DP table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                profits[i - 1] + dp[i - 1][w - weights[i - 1]]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Find selected packages
w = capacity
selected_dp = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_dp.append(packages[i - 1])
        w -= weights[i - 1]

selected_dp.reverse()

print("Selected Packages:", selected_dp)
print("Maximum Profit = Rs.", dp[n][capacity])
