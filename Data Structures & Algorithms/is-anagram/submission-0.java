class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sm = new HashMap<>();
        Map<Character, Integer> tm = new HashMap<>();


        for(int i=0; i < s.length(); i++){
            char letter = s.charAt(i);
            if(sm.containsKey(letter)){
                sm.put(letter, sm.get(letter) + 1);
            }else{
                sm.put(letter, 1);
            }

        }

        for(int i=0; i < t.length(); i++){
            char letter = t.charAt(i);
            if(tm.containsKey(letter)){
                tm.put(letter, tm.get(letter) + 1);
            }else{
                tm.put(letter, 1);
            }
        }

        System.out.println(tm);
        System.out.println(sm);
        return sm.equals(tm);
    }
}
