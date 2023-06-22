#include <iostream>
#include <vector>

using namespace std;

vector<int> increment_integer(vector<int>& digits) {
  int n = digits.size();

  // Carry flag.
  int carry = 1;

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

int main() {
  vector<int> digits = {1, 2, 3};
  vector<int> result = increment_integer(digits);
  for (int i = 0; i < result.size(); i++) {
    cout << result[i] << " ";
  }
  cout << endl;

  return 0;
}

