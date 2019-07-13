class Solution {
    public int countPrimes(int n) {
        if (n <= 2) return 0;
        
        boolean sieve[] = new boolean[n];
        for (int i = 2; i < n; i++) {
            sieve[i] = true;
        }
        
        int count = 0;
        for (int i = 2; i * i < n; i++) {
            if (sieve[i]) {
                for (int j = i * i; j < n; j += i) {
                    sieve[j] = false;
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (sieve[i]) {
                count++;
            }
        }
        return count;
    }
}