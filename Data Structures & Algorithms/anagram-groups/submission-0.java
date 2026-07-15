class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> map= new HashMap<>();
        for(String str:strs){
            char[] ch= str.toCharArray();
            Arrays.sort(ch);
            String updatedStr=new String(ch);
            if(!map.containsKey(updatedStr)){
                map.put(updatedStr,new ArrayList<>());
            }
            map.get(updatedStr).add(str);
        }
        return new ArrayList<>(map.values());

    }
}
