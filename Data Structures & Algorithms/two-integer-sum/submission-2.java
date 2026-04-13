class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numsMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            numsMap.put(nums[i], i);
        }

        for(int i = 0; i < nums.length; i++){
            if(numsMap.containsKey(target - nums[i])){
                if(numsMap.get(target - nums[i]) == i){
                    continue;
                }
                return new int[]{i, numsMap.get(target - nums[i])};
            }    
        }
        return new int[0];
    }
}
