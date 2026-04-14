class Solution {
    public int maxArea(int[] heights) {
       int start = 0, end = heights.length - 1;
       boolean isEnd = true;
       int max = 0;
       while(start < end){
        int distance = end - start;
        int endHeight = heights[end];
        int startHeight = heights[start];
        int water = 0;

        System.out.println("start: "+startHeight+", end: "+endHeight+", distance: "+distance);

        if(endHeight > startHeight){
            water = startHeight * distance;
        }else{
            water = endHeight * distance;
        }

        System.out.println(water);

        if(water > max){
            max = water;
        }else{
            if(endHeight > startHeight){
                start ++;
            }else{
                end --;
            }

        }

       } 
       return max;
    }
}
