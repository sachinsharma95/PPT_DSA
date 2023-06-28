#include <iostream>
#include <vector>

class Solution {
public:
    int searchInsert(std::vector<int>& nums, int target) {
        int l = 0;
        int end = nums.size() - 1;
        int mid = l + (end - l) / 2;
        
        while (l <= end) {
            if (nums[mid] == target) {
                return mid;
            }
            
            if (target > nums[mid]) {
                l = mid + 1;
            } else {
                end = mid - 1;
            }
            
            mid = l + (end - l) / 2;
        }
        
        return l;
    }
};

int main() {
    Solution solution;
    std::vector<int> nums = {1, 3, 5, 6};
    int target = 5;

    int index = solution.searchInsert(nums, target);

    std::cout << "Index: " << index << std::endl;

    return 0;
}
