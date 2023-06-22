#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<int> two_sum(vector<int>& nums, int target) {
  int n = nums.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
}

// driver code 

int main() {
  vector<int> nums = {2, 7, 11, 15};
  int target = 9;
  vector<int> indices = two_sum(nums, target);
  for (int index : indices) {
    cout << index << " ";
  }
  cout << endl;

  return 0;
}

