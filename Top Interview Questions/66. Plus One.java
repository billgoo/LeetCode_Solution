class Solution {
    public int[] plusOne(int[] digits) {
        
        int addition = 1;
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] + addition < 10) {
                digits[i] += addition;
                return digits;
            }
            else if (digits[i] + addition == 10) {
                digits[i] = 0;
            }
        }
        
        int[] re = new int[digits.length + 1];
        re[0] = 1;
        for (int i = 1; i < re.length; i++) {
            re[i] = digits[i-1];
        }
        return re;
        
    }
}