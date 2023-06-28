#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> plusOne(std::vector<int>& digits) {
        int n = digits.size();
        int carry = 1; // Carry flag.

        for (int i = n - 1; i >= 0; i--) {
            int digit = digits[i] + carry;

            // If the digit is 9, then it rolls over to 0 and the carry flag is set.
            if (digit == 10) {
                digit = 0;
                carry = 1;
            } else {
                carry = 0;
            }

            digits[i] = digit;
        }

        // If the carry flag is set, then we need to add one more digit to the array.
        if (carry) {
            digits.insert(digits.begin(), 1);
        }

        return digits;
    }
};

int main() {
    Solution solution;
    std::vector<int> digits = {1, 2, 3};

    std::vector<int> result = solution.plusOne(digits);

    // Printing the result
    for (int digit : result) {
        std::cout << digit << " ";
    }
    std::cout << std::endl;

    return 0;
}
