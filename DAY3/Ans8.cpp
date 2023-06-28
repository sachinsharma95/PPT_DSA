#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    bool canAttendMeetings(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
            return a[0] < b[0];
        });

        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i - 1][1] > intervals[i][0]) {
                return false;
            }
        }

        return true;
    }
};

int main() {
    Solution solution;
    std::vector<std::vector<int>> intervals = {{0, 30}, {5, 10}, {15, 20}};

    bool canAttendAll = solution.canAttendMeetings(intervals);

    std::cout << (canAttendAll ? "true" : "false") << std::endl;

    return 0;
}
