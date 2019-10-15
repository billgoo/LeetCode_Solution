/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        // int pos = -1;
        ListNode *p1 = head;
        ListNode *p2 = head;
        // bool flag = false;
        while(p2 && p2->next){
            // pos += 1;
            p1 = p1->next;
            p2 = p2->next->next;
            if(p1 == p2){
                // flag = true;
                // break;
                return true;
            }
        }
        /*
        if(flag){
            return true;
        }else{
            return false;
        }
        */
        return false;
    }
};