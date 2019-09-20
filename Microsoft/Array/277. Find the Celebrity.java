/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

public class Solution extends Relation {
    public int findCelebrity(int n) {
        int x = 0;
        for (int i = 0; i < n; i++) {
            if (knows(x, i)) {
                x = i;
            }
        }
        
        
        for (int i = 0; i < n; i++) {
            if (knows(x, i) && i < x) {
                return -1;
            }
            if (!knows(i, x)) {
                return -1;
            }
        }
        
        return x;
    }
}