class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) return new ArrayList<List<String>>();
        
        HashMap<String, List<String>> m = new HashMap<String, List<String>>();
        
        for (String s: strs) {
            char[] c = s.toCharArray();
            Arrays.sort(c);
            
            String key = String.valueOf(c);
            if (!m.containsKey(key)) m.put(key, new ArrayList<String>());
            m.get(key).add(s);
        }
        
        return new ArrayList(m.values());
    }
}