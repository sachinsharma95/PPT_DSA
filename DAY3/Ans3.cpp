#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    void nextPermutation(std::vector<int>& nums) {
        int n = nums.size();
        int k, l;

        for (k = n - 2; k >= 0; k--) {
            if (nums[k] < nums[k + 1]) {
                break;
            }
        }

        if (k < 0) {
            std::reverse(nums.begin(), nums.end());
        } else {
            for (l = n - 1; l > k; l--) {
                if (nums[l] > nums[k]) {
                    break;
                }
            }

            std::swap(nums[k], nums[l]);
            std::reverse(nums.begin() + k + 1, nums.end());
        }
    }
};

int main() {
    Solution solution;
    std::vector<int> nums = {1, 2, 3};

    solution.nextPermutation(nums);

    // Printing the next permutation
    for (int num : nums) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
