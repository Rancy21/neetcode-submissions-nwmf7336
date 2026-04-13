class Solution {
    public boolean isPalindrome(String s) {
        String noSpace = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int start = 0;
        int end = noSpace.length() - 1;
        boolean flag = true;
        while (start <= end){
            if(noSpace.charAt(start) != noSpace.charAt(end)){
                flag = false;
                break;
            }

            start++;
            end--;
        }

        return flag;




    }
}
