class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> checker = new HashSet<>();

        for(int i = 0; i < nums.length; i++){
            if(!checker.add(nums[i])){
                return true;
            }
        }

        return false;
    }
}