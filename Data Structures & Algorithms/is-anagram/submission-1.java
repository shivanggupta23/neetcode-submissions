class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false;
        TreeMap<Character,Integer> map1=new TreeMap<>();
        // TreeMap<Character,Integer> map2=new TreeMap<>();
        for(char ch:s.toCharArray()){
            map1.put(ch,map1.getOrDefault(ch,0)+1);

        }
        for(char ch:t.toCharArray()){
            if(!map1.containsKey(ch)){
                return false;
            }
            map1.put(ch,map1.get(ch)-1);
            if(map1.get(ch)==0){
                map1.remove(ch);
            }
        }
        
        return map1.isEmpty();
    }
}
