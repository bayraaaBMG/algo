#import numpy as np

def optimal_bst_cost(frequencies, n):
    
    dp = np.full((n, n), float('inf'))

    freq_sum = np.zeros((n, n), dtype=int)
    
    for i in range(n):
        dp[i][i] = frequencies[i]
        freq_sum[i][i] = frequencies[i]
    
    for L in range(2, n+1):  
        for i in range(n - L + 1):
            j = i + L - 1
            freq_sum[i][j] = freq_sum[i][j-1] + frequencies[j]
            
            for r in range(i, j + 1):
                
                cost = (0 if r == i else dp[i][r - 1]) + \
                       (0 if r == j else dp[r + 1][j]) + \
                       freq_sum[i][j]
                
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

# Гараас түлхүүрүүд болон давтамжуудыг оруулах
n = int(input("Түлхүүрүүдийн тоог оруулна уу: "))
keys = []
frequencies = []

print("Түлхүүрүүдийг оруулна уу:")
for i in range(n):
    key = int(input(f"Түлхүүр {i + 1}: "))
    keys.append(key)

print("Түлхүүр тус бүрийн давтамжуудыг оруулна уу:")
for i in range(n):
    freq = int(input(f"{keys[i]} түлхүүрийн давтамж: "))
    frequencies.append(freq)

# Хамгийн бага өртөгийг тооцоолох
print("OBST-ийн хамгийн бага өртөг:", optimal_bst_cost(frequencies, n))
