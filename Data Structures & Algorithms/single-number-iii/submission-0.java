class Solution {
    public int[] singleNumber(int[] nums) {
        int xored=0;
        for(int num:nums){
            xored^=num;
        }
        int lsb=0;
        while(true){
            if((xored & 1)==1){
                break;
            }
            xored=xored>>1;
            lsb++;
        }
        int setBucket=0;
        int unsetBucket=0;
        for(int num:nums){
            if(((num>>lsb)&1)==1){
                setBucket^=num;
            }else{
                unsetBucket^=num;
            }
        }
        return new int[]{setBucket,unsetBucket};
    }
}