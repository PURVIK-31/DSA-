

//https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
 

 // SOLUTION TO THE PROBLEM : 

 // 1. Find the minimum and maximum element in an array

 //{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
#include <vector>  
#include <algorithm> // For min_element and max_element  
#include <utility>   // For pair  

class Solution {  
public:  
    std::pair<long long, long long> getMinMax(std::vector<long long> arr) {  
        if (arr.empty()) {  
            return {0, 0}; // Handle empty array case  
        }  
        
        long long minElement = *std::min_element(arr.begin(), arr.end());  
        long long maxElement = *std::max_element(arr.begin(), arr.end());  
        
        return {minElement, maxElement};  
    }  
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<long long int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution ob;
        pair<long long, long long> pp = ob.getMinMax(arr);
        cout << pp.first << " " << pp.second << endl;
    }
    return 0;
}
// } Driver Code Ends