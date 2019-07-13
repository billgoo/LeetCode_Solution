class Solution {
    public List<String> letterCombinations(String digits) {
        String digitletter[] = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        List<String> re = new ArrayList<String>();
    
        if (digits.length()==0) return re;
        
        re.add("");
        
        for (int i = 0; i < digits.length(); i++) {
            re = concat(digitletter[digits.charAt(i) - '0'], re);
        }
        
        return re;
    }
    
    private List<String> concat(String digits, List<String> re) {
        ArrayList<String> r = new ArrayList<String>();
        
        for (int i = 0; i < digits.length(); i++) {
            for (String c : re)
                r.add(c + digits.charAt(i));
        }
        
        return r;
    }
}