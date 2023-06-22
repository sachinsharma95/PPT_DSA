#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int remove_val(vector<int>& nums, int val) {
    int i=0,j=0;
        
      for(i=0; i<nums.size();i++){
            if(nums[i]!=val){
                nums[j]=nums[i];
                j++;
            }
      }
        return j;
        
        
    }

    
int main() {
  vector<int> nums = {3, 2, 2, 3};
  int val = 3;
  int k = remove_val(nums, val);
  for (int i = 0; i < k; i++) {
    cout << nums[i] << " ";
  }
  cout << endl;

  return 0;
}
