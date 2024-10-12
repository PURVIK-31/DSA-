// Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :
// 1. Each student gets exactly one packet.
// 2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.



#include<algorithm> 
class Solution{
    public:
    long long findMinDiff(vector<long long> a, long long n, long long m){
    sort(a.begin(), a.end());

    int minDiff = INT_MAX;

    for (int i = 0; i + m - 1 < n; i++) {
          
          // calculate difference of current window
        int diff = a[i + m - 1] - a[i];
      
          // if current difference is smaller
          // then update the minimum difference
        if (diff < minDiff)
            minDiff = diff;
    }
    return minDiff;
    }   
};
