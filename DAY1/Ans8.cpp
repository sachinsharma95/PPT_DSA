#include <iostream>
#include <vector>

using namespace std;

vector<int> find_error_nums(vector<int>& nums) {
  int n = nums.size();
  vector<int> count(n + 1, 0);
  vector<int> result;

  for (int num : nums) {
    count[num]++;
  }

  for (int i = 1; i <= n; i++) {
    if (count[i] == 2) {
      result.push_back(i);
    } else if (count[i] == 0) {
      result.push_back(i);
    }
  }

  return result;
}

// driver code 

int main() {
  vector<int> nums = {1, 2, 2, 4};
  vector<int> result = find_error_nums(nums);
  for (int num : result) {
    cout << num << " ";
  }
  cout << endl;

  return 0;
}
