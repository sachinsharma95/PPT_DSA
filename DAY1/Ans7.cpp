#include <iostream>
#include <vector>

using namespace std;

void move_zeros(vector<int>& nums) {
  int j = 0;

  for (int i = 0; i < nums.size(); i++) {
    if (nums[i] != 0) {
      nums[j++] = nums[i];
    }
  }

  for (int i = j; i < nums.size(); i++) {
    nums[i] = 0;
  }
}

int main() {
  vector<int> nums = {0, 1, 0, 3, 12};
  move_zeros(nums);
  for (int num : nums) {
    cout << num << " ";
  }
  cout << endl;

  return 0;
}
