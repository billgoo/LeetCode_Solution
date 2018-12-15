class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        n = K- len(S) % K
        S = '*' * (n if n < K else 0) + S
        return '-'.join(S[i: i+K] for i in range(0, len(S), K)).replace('*', '')