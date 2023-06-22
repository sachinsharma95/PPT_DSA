

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int search_insert(vector<int>& nums, int target) {
  int low = 0;
  int high = nums.size() - 1;
// using the Binary search 
  while (low <= high) {
    int mid = (low + high) / 2;

    if (nums[mid] == target) {
      return mid;
    } else if (nums[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return low;
}

// driver code


int main() {
  vector<int> nums = {1, 3, 5, 6};
  int target = 5;
  int index = search_insert(nums, target);
  cout << index << endl;

  return 0;
}

