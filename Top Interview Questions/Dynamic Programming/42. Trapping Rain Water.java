class Solution {
    public int trap(int[] height) {
        int i = 0, j = height.length - 1, left_max = 0, right_max = 0;
        int result = 0;
        while(i < j){
            if(height[i] <= height[j]){
                if(height[i] >= left_max){
                    left_max = height[i];
                }else{
                    result += left_max - height[i];
                }
                i++;
            }else{
                if(height[j] >= right_max){
                    right_max = height[j];
                }else{
                    result += right_max - height[j];
                }
                j--;
            }
        }
        return result;
    }
}