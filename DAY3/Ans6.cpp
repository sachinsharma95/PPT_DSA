#include <iostream>
#include <vector>

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
};

int main() {
    Solution solution;
    std::vector<int> nums = {2, 2, 1};

    int singleNum = solution.singleNumber(nums);

    std::cout << "Single Number: " << singleNum << std::endl;

    return 0;
}
