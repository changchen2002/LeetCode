class Solution {
    public int maxProduct(int[] nums) {
        int currmax = nums[0];
        int currmin = nums[0];
        int compare = nums[0];

        for (int i = 1; i < nums.length; i++) {
        int temp = currmax;
        currmax = Math.max(nums[i], Math.max(currmax*nums[i], currmin*nums[i]));
        currmin = Math.min(nums[i], Math.min(temp*nums[i], currmin*nums[i]));
        compare = Math.max(compare, currmax);
        }

        return compare; 
    }
}