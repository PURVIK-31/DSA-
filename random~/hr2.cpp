// A template parameter pack is a template parameter that accepts zero or more template arguments (non-types, types, or templates). To read more about parameter pack, click here.

// Create a template function named reversed_binary_value. It must take an arbitrary number of bool values as template parameters. These booleans represent binary digits in reverse order. Your function must return an integer corresponding to the binary value of the digits represented by the booleans. For example: reversed_binary_value<0,0,1>() should return .

// Input Format

// The first line contains an integer, , the number of test cases. Each of the  subsequent lines contains a test case. A test case is described as  space-separated integers,  and , respectively.

//  is the value to compare against.
//  represents the range to compare:  to .
// Constraints

// The number of template parameters passed to reversed_binary_value will be .
// Output Format

// Each line of output contains  binary characters (i.e., 's and 's). Each character represents one value in the range. The first character corresponds to the first value in the range. The last character corresponds to the last value in the range. The character is  if the value in the range matches ; otherwise, the character is .

// Sample Input

// 2
// 65 1
// 10 0
// Sample Output

// 0100000000000000000000000000000000000000000000000000000000000000
// 0000000000100000000000000000000000000000000000000000000000000000
// Explanation

// The second character on the first line is a , because the second value in the range  is  and  is .

// The eleventh character on the second line is a , because the eleventh value in the range  is  and  is .

// All other characters are zero, because the corresponding values in the range do not match .

#include <iostream>
using namespace std;

// Enter your code for reversed_binary_value < bool...>()

template < bool first, bool...digits >
    constexpr int reversed_binary_value()
    {
        if constexpr(sizeof...(digits) > 0)
        return first + reversed_binary_value < digits... > () *2;
        else
            return first;
    }

template < int n, bool...digits >
    struct CheckValues
    {
        static void check(int x, int y)
        {
            CheckValues < n - 1, 0, digits... >::check(x, y);
            CheckValues < n - 1, 1, digits... >::check(x, y);
        }
    };

template < bool...digits >
    struct CheckValues<0, digits... >
    {
        static void check(int x, int y)
        {
            int z = reversed_binary_value < digits... > ();
            std::cout << (z + 64 *y == x);
        }
    };

int main()
{
    int t;
    std::cin >> t;

    for (int i = 0; i != t; ++i)
    {
        int x, y;
        cin >> x >> y;
        CheckValues<6>::check(x, y);
        cout << "\n";
    }
}