/*
我也不知道为什么另一种写法
用stack实现DFS但是老是报错
还是用迭代吧
求帮助另一种写法修改
主要是写这个的时候LeetCode挂了不知道为什么这一题不能用run code debug
只能不停submit
所以就先舍弃这个然后move on了
*/

/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    HashMap<RandomListNode, RandomListNode> nodes = 
        new HashMap<RandomListNode, RandomListNode>();
    public RandomListNode copyRandomList(RandomListNode head) {
        if(head == null){
            return null;
        }
        
        // visited
        if(this.nodes.containsKey(head)){
            return this.nodes.get(head);
        }
        
        RandomListNode node = new RandomListNode(head.label);
        
        this.nodes.put(head, node);
        
        node.next = this.copyRandomList(head.next);
        node.random = this.copyRandomList(head.random);
        
        return this.nodes.get(head);
    }
}