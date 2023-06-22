#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        
        for(int i=0;i<nums.size()-1;i++){
           
                if(nums[i]==nums[i+1]){
                    return true ;
                
                }
                
            }
        
        return false ;
        
    }


int main() {
  vector<int> nums = {1, 2, 3, 1};
  bool has_duplicate = containsDuplicate(nums);
  if(has_duplicate== 1 ){
    cout<<"true";
  }
else{
    cout<<"false"<<endl;
}

  return 0;
}
