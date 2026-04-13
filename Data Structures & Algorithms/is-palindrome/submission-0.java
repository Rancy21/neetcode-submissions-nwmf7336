class Solution {
    public boolean isPalindrome(String s) {
        String noSpace = s.replaceAll("[^a-zA-Z0-9]", "");
        int len = noSpace.length();
        char[] reverseArray = new char[len];

        for(int i = len - 1; i > -1; i--){
            reverseArray[len - 1 - i] = noSpace.charAt(i);
        }

        System.out.println(noSpace.toLowerCase());
        System.out.println(new String(reverseArray).toLowerCase());

        return noSpace.toLowerCase().equals(new String(reverseArray).toLowerCase());
    }
}
