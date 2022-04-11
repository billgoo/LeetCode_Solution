/**
 * 206. Reverse Linked List
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        // recursively O_n time and O_n space
        if (head == null || head.next == null) return head;
        ListNode p = reverseList(head.next);
        head.next.next = head; //指向同一个对象，对象在内存中不变，所以每次操作都使得前后指针同时指向中间，比如5和3同时指向head4
        head.next = null;
        return p;
    }
}