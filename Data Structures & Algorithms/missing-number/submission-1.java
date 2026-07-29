class Solution {
    public int missingNumber(int[] nums) {
        int n=nums.length;
       int expected= n*(n+1)/2;
       int actual=0;
       for(int num:nums){
        actual+=num;
       }
       return expected-actual;
    }
}
// public int missingNumber(int[] nums) {
//         int xor =nums.length;
//         for(int i=0;i<nums.length;i++){
//             xor=xor^i^nums[i];
//         }
//         return xor;
//     }