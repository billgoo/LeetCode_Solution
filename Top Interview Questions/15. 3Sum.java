class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> re = new LinkedList<>();
        for(int i = 0; i < nums.length-2; i++){
            if(nums[i] > 0)
                break;
            if(i > 0 && nums[i] == nums[i - 1])
                continue;
            int s = -nums[i];
            int f = i + 1, l = nums.length - 1;
            while(f < l){
                if(s == nums[f] + nums[l]){
                    re.add(Arrays.asList(nums[i], nums[f], nums[l]));
                    while(f < l && nums[f] == nums[f+1]){
                        f++;
                    }
                    while(f < l && nums[l] == nums[l-1]){
                        l--;
                    }
                    f++;
                    l--;
                }
                else if(s < nums[f] + nums[l]){
                    l--;
                }
                else{
                    f++;
                }
            }
        }
        return re;
    }
}