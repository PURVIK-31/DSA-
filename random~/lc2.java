/*

import java.util.List;

class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int n = nums.size();
        int[] ans = new int[n];
        
        for (int i = 0; i < n; i++) {
            int num = nums.get(i);
            int minimalAns = Integer.MAX_VALUE;
            boolean found = false;
            
            // Iterate through each bit position (0 to 30)
            for (int bit = 0; bit <= 30; bit++) {
                if (((num >> bit) & 1) == 1) {
                    // Unset the current bit
                    int candidate = num & ~(1 << bit);
                    
                    // Ensure candidate is non-negative
                    if (candidate < 0) continue;
                    
                    // Check if candidate OR (candidate + 1) equals num
                    if ((candidate | (candidate + 1)) == num) {
                        if (candidate < minimalAns) {
                            minimalAns = candidate;
                            found = true;
                        }
                    }
                }
            }
            
            if (found) {
                ans[i] = minimalAns;
            } else {
                ans[i] = -1;
            }
        }
        
        return ans;
    }
}
*/


import java.util.List;

class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int n = nums.size();
        int[] ans = new int[n];
        
        for (int i = 0; i < n; i++) {
            int num = nums.get(i);
            int minimalAns = Integer.MAX_VALUE;
            boolean found = false;
            
            // Iterate through each bit position (0 to 30)
            for (int bit = 0; bit <= 30; bit++) {
                if (((num >> bit) & 1) == 1) {
                    // Unset the current bit
                    int candidate = num & ~(1 << bit);
                    
                    // Ensure candidate is non-negative
                    if (candidate < 0) continue;
                    
                    // Check if candidate OR (candidate + 1) equals num
                    if ((candidate | (candidate + 1)) == num) {
                        if (candidate < minimalAns) {
                            minimalAns = candidate;
                            found = true;
                        }
                    }
                }
            }
            
            if (found) {
                ans[i] = minimalAns;
            } else {
                ans[i] = -1;
            }
        }
        
        return ans;
    }
}

