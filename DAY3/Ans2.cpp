#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> fourSum(std::vector<int>& nums, long target) {
        std::vector<std::vector<int>> ans;
        std::sort(nums.begin(), nums.end());
        if(nums.size()<4)
            return ans;
        int n=nums.size();
        for(int i=0;i<n-3;i++)
        {
            for(int j=i+1; j<n-2;j++)
            {
                long sum=target-nums[i]-nums[j];
                int l=j+1, r=n-1;
                std::vector<int> v(4);
                while(l<r)
                {
                    if(nums[l]+nums[r]==sum)
                    {
                        v[0]=nums[i];
                        v[1]=nums[j];
                        v[2]=nums[l];
                        v[3]=nums[r];
                        ans.push_back(v);
                        while(l<r && v[2]==nums[l])
                            l++;
                        while(l<r && v[3]==nums[r])
                            r--;
                    }
                    else if(nums[l]+nums[r]<sum)
                        l++;
                    else
                        r--;
                }
                while(j<n-2 && nums[j]==nums[j+1])
                    j++;
            }
            while(i<n-3 && nums[i]==nums[i+1])
                i++;
        }
        return ans;
    }
};

int main() {
    Solution solution;
    std::vector<int> nums = {1, 0, -1, 0, -2, 2};
    long target = 0;

    std::vector<std::vector<int>> quadruplets = solution.fourSum(nums, target);

    // Printing the quadruplets
    for (const auto& quad : quadruplets) {
        std::cout << "[";
        for (int num : quad) {
            std::cout << num << ",";
        }
        std::cout << "]" << std::endl;
    }

    return 0;
}
