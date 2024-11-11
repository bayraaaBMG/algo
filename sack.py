import unittest

# knapsack ptoblem 0-1 vvrgewch hulgaich delgvvrees her hemjeenii baraa awah bolomj 220 bagtaamj maht  // unitest zasna
def knapsack(W, weights, values, n):
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


class TestKnapsack(unittest.TestCase):
    def test_knapsack_from_file(self):
        with open("sacktest.txt", "r") as file:
            for line in file:
                W, weights, values, expected = line.strip().split(",")
                W = int(W)
                weights = list(map(int, weights.split()))
                values = list(map(int, values.split()))
                expected = int(expected)
                n = len(values)
                result = knapsack(W, weights, values, n)
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()


#W = 50: Knapsack хүчин чадал.
# weights = [10, 20, 30]: Зүйлийн жин.
# values = [60, 100, 120]: Зүйлийн үнэ цэнэ.
# expected = 220: Хулгайч хүлээгдэж буй хамгийн их утга.