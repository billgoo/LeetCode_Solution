/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        int l = nums.length;
        if (l == 0) {
            return null;
        }
        
        int m = l / 2;
        TreeNode root = new TreeNode(nums[m]);
        root.left = sortedArrayToBST(Arrays.copyOfRange(nums, 0, m));
        root.right = sortedArrayToBST(Arrays.copyOfRange(nums, m + 1, l));
        
        return root;
    }
}