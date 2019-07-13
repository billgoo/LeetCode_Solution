class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        
        StringBuilder sBuilder = new StringBuilder(strs[0]);
        // int l = sBuilder.length();
        
        for (int i = 0; i < strs.length; i++) {
            for (int j = 0; j < sBuilder.length(); j++) {
                if (j >= strs[i].length()) {
                    sBuilder.delete(j, sBuilder.length());
                    break;
                }
                if (sBuilder.charAt(j) != strs[i].charAt(j)) {
                    sBuilder.delete(j, sBuilder.length());
                    break;
                }
            }
        }
        
        return sBuilder.toString();
    }
}