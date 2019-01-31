/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    HashMap<RandomListNode, RandomListNode> nodes = new HashMap<RandomListNode, RandomListNode>();
    HashMap<Integer, Integer> visited = new HashMap<Integer, Integer>();
    public RandomListNode copyRandomList(RandomListNode head) {
        if(head == null){
            return null;
        }
        RandomListNode next = head;
        while(next != null){
            this.visited.put(next.label, 0);
            next = next.next;
        }
        
        Stack<RandomListNode> s = new Stack<RandomListNode>();
        s.push(head);
        while(!s.isEmpty()){
            RandomListNode node = s.pop();
            RandomListNode v = new RandomListNode(node.label);
            if(this.visited.get(v.label) == 0){
                this.visited.remove(v.label);
                this.visited.put(v.label, 1);
                if(node.next != null){
                    v.next = new RandomListNode(node.next.label);
                    s.push(node.next);
                }else{
                    v.next = null;
                }
                if(node.random != null){
                    v.random = new RandomListNode(node.random.label);
                    s.push(node.random);
                }else{
                    v.random = null;
                }
            
                this.nodes.put(head, v);
            }
        }
        return this.nodes.get(head);
    }
}