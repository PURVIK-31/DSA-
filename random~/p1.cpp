#include <iostream>  
#include <vector>  
using namespace std;  

int maxSumSubarray(vector<int>& arr, int K) {  
    int n = arr.size();  
    if (n < K) return -1; // Edge case: if array size is less than K  

    int maxSum = 0;  
    int windowSum = 0;  

    // Calculate the sum of the first K elements  
    for (int i = 0; i < K; i++) {  
        windowSum += arr[i];  
    }  
    maxSum = windowSum;  

    // Slide the window over the array  
    for (int i = K; i < n; i++) {  
        windowSum += arr[i] - arr[i - K]; // Slide the window  
        maxSum = max(maxSum, windowSum);  // Update maxSum if needed  
    }  

    return maxSum;  
}  

int main() {  
    vector<int> arr = {1, 4, 2, 10, 23, 3, 1, 0, 20};  
    int K = 4;  
    cout << "Maximum sum of subarray of size " << K << " is " << maxSumSubarray(arr, K) << endl;  
    return 0;  
}