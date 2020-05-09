class Solution {
    public int firstUniqChar(String s) {
        int l = s.length();
        Map<Character, Integer> m = new HashMap(l);
        for (int i = 0; i < l; i++) {
            int v = 0;
            if (m.containsKey(s.charAt(i))) {
                v = m.get(s.charAt(i));
            }
            v++;
            m.put(s.charAt(i), v);
        }
        
        
        for (int i = 0; i < l; i++) {
            if (m.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        
        return -1;
    }
}