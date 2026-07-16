class Solution {

    public String encode(List<String> strs) {
        StringBuilder str=new StringBuilder();
        for(int i=0;i<strs.size();i++){
            int subLength=strs.get(i).length();
            str.append(subLength);
            str.append("#");
            str.append(strs.get(i));
        }
        return str.toString();

        
    }

    public List<String> decode(String str) {
        List<String> list=new ArrayList<>();
        int i=0;
        while(i<str.length()){
            int j=i;
            while(str.charAt(j)!='#'){
                j++;
            }
            int length=Integer.parseInt(str.substring(i,j));
            j++;
            String temp=str.substring(j,j+length);
            list.add(temp);

            i=j+length;
        }
        return list;
    }
}
