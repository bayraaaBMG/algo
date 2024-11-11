# import unittest

# def knapSack(W, wt, val, n):
#     dp = [0 for _ in range(W+1)]
    
#     for i in range(1, n+1):
#         for w in range(W, 0, -1):
#             if wt[i-1] <= w:
#                 dp[w] = max(dp[w], dp[w-wt[i-1]] + val[i-1])
#             else:
#                 p = (W - (W - w)) / wt[i-1]
#                 dp[w] = max(dp[w], dp[w-wt[i-1]] + val[i-1] * p)
    
#     return int(dp[W])


# def read_test_data_from_txt(filename):
#     test_cases = []
#     with open(filename, 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             parts = line.strip().split('/')  
#             W = int(parts[0]) 
#             weight = list(map(int, parts[1].split()))  
#             profit = list(map(int, parts[2].split())) 
#             test_cases.append((W, weight, profit))
#     return test_cases


# class TestKnapSack(unittest.TestCase):


#     def setUp(self):
#         self.test_cases = read_test_data_from_txt('myFile.txt')

#     def test_knapSack(self):
#         for case in self.test_cases:
#             W, weight, profit = case
#             n = len(profit)
#             expected_results = {
#                 5: 280,  
#                 10: 178  
#             }
#             result = knapSack(W, weight, profit, n)
#             self.assertEqual(result, expected_results[W])

# if __name__ == '__main__':
#     unittest.main()

# import numpy as np

class Node:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

def decode_huff(root, s):
    current_node = root
    decoded_string = ""

    for char in s:
        if char == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_string += current_node.symbol
            current_node = root

    return decoded_string


root = Node(10)
root.left = Node(5, 'A')  # 'A' has code '0'
root.right = Node(5)
root.right.left = Node(2, 'B')  # 'B' has code '10'
root.right.right = Node(3)
root.right.right.left = Node(1, 'C')  # 'C' has code '110'
root.right.right.right = Node(2, 'D')  # 'D' has code '111'


s = "0110111010"

# Decode the string
decoded_output = decode_huff(root, s)
print(decoded_output) 
