class Solution {
    public int rob(int[] nums) {
        if(nums.length<2) return nums[0];
        int n=nums.length;
        int[] lastSkip=new int[n-1];
        int[] firstSkip=new int[n-1];
        for(int i=0;i<n-1;i++){
            lastSkip[i]=nums[i];
            firstSkip[i]=nums[i+1];
        }
        int first=robHouse(lastSkip);
        int last=robHouse(firstSkip);
        return Math.max(first,last);
    }
    public int robHouse(int[] arr){
        if(arr.length==0) return 0;
        if(arr.length==1) return arr[0];
        int[] dp=new int[arr.length];
        dp[0]=arr[0];
        dp[1]=Math.max(arr[0],arr[1]);
        for(int i=2;i<arr.length;i++){
            dp[i]=Math.max(dp[i-2]+arr[i],dp[i-1]);
        }
        return dp[arr.length-1];
    }
}
