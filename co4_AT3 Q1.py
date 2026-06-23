# Nandhini sri V(192521344)
# Comparing Greedy and Dynamic Programming
# for Investment Portfolio Optimization

# Investment data
investments = ['A', 'B', 'C', 'D']
capital = [20000, 30000, 40000, 50000]
returns = [25000, 40000, 50000, 70000]
budget = 80000

print("GREEDY APPROACH")

# Calculate Return/Capital ratio
items = []

for i in range(len(investments)):
    ratio = returns[i] / capital[i]
    items.append((ratio, investments[i], capital[i], returns[i]))

# Sort by ratio in descending order
items.sort(reverse=True)

selected = []
total_capital = 0
total_return = 0

# Select investments greedily
for ratio, name, cap, ret in items:
    if total_capital + cap <= budget:
        selected.append(name)
        total_capital += cap
        total_return += ret

print("Selected Investments:", selected)
print("Capital Used = Rs.", total_capital)
print("Total Return = Rs.", total_return)

print("\nDYNAMIC PROGRAMMING APPROACH")

# Scale down values by 1000 to reduce table size
weights = [c // 1000 for c in capital]
W = budget // 1000

n = len(investments)

# Create DP table
dp = [[0]*(W+1) for _ in range(n+1)]

# Fill DP table
for i in range(1, n+1):
    for w in range(W+1):
        if weights[i-1] <= w:
            dp[i][w] = max(dp[i-1][w],
                           returns[i-1] + dp[i-1][w-weights[i-1]])
        else:
            dp[i][w] = dp[i-1][w]

# Find selected investments
w = W
selected_dp = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        selected_dp.append(investments[i-1])
        w -= weights[i-1]

selected_dp.reverse()

print("Selected Investments:", selected_dp)
print("Maximum Return = Rs.", dp[n][W])
