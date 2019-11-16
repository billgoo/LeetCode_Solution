class Solution {
    public boolean isPalindrome(String s) {
        if (s.isEmpty()) return true;
        
        int l = 0, r = s.length() - 1;
        
        while (l < r) {
            char cl = s.charAt(l), cr = s.charAt(r);
            if (!Character.isLetterOrDigit(cl)) {
                l++;
            }
            else if (!Character.isLetterOrDigit(cr)) {
                r--;
            }
            else {
                if (Character.toLowerCase(cl) != Character.toLowerCase(cr)) {
                    return false;
                }
                l++;
                r--;
            }
        }
        
        return true;
    }
}