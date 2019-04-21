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
    public int maxDepth(TreeNode root) {
        int d = 0;
        if (root != null){
            d++;
            d += Math.max(maxDepth(root.left), maxDepth(root.right));
        }
        return d;
    }
}