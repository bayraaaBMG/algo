#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

unordered_map<int, int> memo;
// vnedsen ogogdol  Pibonachiin toog dinamik program (cache ashiglan)t
int fib(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;

    if (memo.find(n) != memo.end()) {
        return memo[n];
    }

    memo[n] = fib(n - 1) + fib(n - 2);
    return memo[n];
}
// text. failaa zow unshij bga 
vector<pair<int, int>> readTestCases(const string& filename) {
    vector<pair<int, int>> testCases;
    ifstream file(filename);
    if (file.is_open()) {
        int input, output;
        while (file >> input >> output) {
            testCases.emplace_back(input, output);
        }
        file.close();
    }
    return testCases;
}
// text failaa buruu buyu aldaag an olj bga
TEST_CASE("Test", "[fib]") {
    vector<pair<int, int>> testCases = readTestCases("testcases.txt");
    for (const auto& testCase : testCases) {
        int input = testCase.first;
        int expectedOutput = testCase.second;
        memo.clear();
        REQUIRE(fib(input) == expectedOutput);
    }
}

//Утга dp[len(text1)][len(text2)] хамгийн урт нийтлэг үр дагаврын урт байх болно.
//Unitest gedeg an testiig bolowsruulaad daraa an shalgaad hariu
