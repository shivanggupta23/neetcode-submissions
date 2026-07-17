class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length==0) return 0;
        HashSet<Integer> set=new HashSet<>();
        int max=0;
        for(int num:nums){
            set.add(num);
        }
        for(int num:set){
            if(num == Integer.MIN_VALUE || !set.contains(num-1)){
                int current=num;
                int len=1;
                while(current!=Integer.MAX_VALUE && set.contains(current+1)){
                    current++;
                    len++;
            }
            
            max=Math.max(max,len);
            }
        }
        return max;
    }
}