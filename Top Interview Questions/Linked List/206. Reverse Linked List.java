/**
 * 206. Reverse Linked List
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        // stack approach O_n time and O_n space
        if (head == null || head.next == null) {
            return head;
        }

        Stack<Integer> s = new Stack<Integer>();

        while (head != null) {
            s.push(head.val);
            head = head.next;
        }

        ListNode a = new ListNode(0);
        ListNode dummy = a;

        while (!s.empty()) {
            a.next = new ListNode(s.pop());
            a = a.next;
        }

        return dummy.next;

    }
}