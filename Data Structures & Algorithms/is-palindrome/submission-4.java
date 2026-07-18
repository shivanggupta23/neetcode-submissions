class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder str=new StringBuilder();
        Stack<Character> stack=new Stack<>();
        for(char ch:s.toCharArray()){
            if(Character.isLetterOrDigit(ch)){
                str.append(Character.toLowerCase(ch));
            }
        }
        String clean=str.toString();
        // String reverse=str.reverse().toString();
        // return clean.equals(reverse);
        for(char ch:clean.toCharArray()){
            stack.push(ch);            
        }
        for(char ch:clean.toCharArray()){
            if(ch!=stack.pop()){
                return false;
            }
        }
        return true;
    }
}
