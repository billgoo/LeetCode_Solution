class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) {
            return 0;
        }
        
        if (haystack.length() == 0 || haystack.length() < needle.length()) {
            return -1;
        }
        
        for (int i = 0; i <= haystack.length() - needle.length(); ) {
            int count = 0;
            int j = 0;
            while (j < needle.length() && haystack.charAt(i) == needle.charAt(j)) {
                count++;
                i++;
                j++;
            }
            
            if (count == needle.length()) {
                return i - count;
            } else {
                i = i - count + 1;
            }
        }
        
        return -1;
    }
}