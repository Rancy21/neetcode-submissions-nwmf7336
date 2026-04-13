class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> solution = new ArrayList<>();
        Map<Map<Character, Integer>, Integer> words = new HashMap<>();

        for(int i = 0; i < strs.length; i++){
            String word = strs[i];
            Map<Character, Integer> letters = new HashMap<>();
            for(int j = 0; j < word.length(); j++){
                char letter = word.charAt(j);
                if(letters.containsKey(letter)){
                    letters.put(letter, letters.get(letter) + 1);
                }else{
                    letters.put(letter, 1);
                }  
            }
            
            System.out.println(letters);

            if(words.containsKey(letters)){
                solution.get(words.get(letters)).add(word);
            }else{
                List<String> anagrams = new ArrayList<>();
                anagrams.add(word);
                solution.add(anagrams);
                words.put(letters, solution.indexOf(anagrams));
            }
        }

        return solution;
    }
}
