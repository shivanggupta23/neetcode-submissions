class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length==0) return 0;
        HashSet<Integer> set=new HashSet<>();
        int max=0;
        for(int num:nums){
            set.add(num);
        }
        for(int num :nums){
            if(!set.contains(num-1)){
                int current=num;
                int length=1;
                while(set.contains(current+1)){
                    current++;
                    length+=1;
                    
                }
                max=Math.max(length,max);
            }
        }
        return max;
    }
}
