class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
                 ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
                 ".--","-..-","-.--","--.."]
        diff_forms = dict()
        
        for word in words:
            transfer = ""
            for char in word:
                transfer += morse[ord(char) - 97]
            diff_forms[transfer] = word
        
        return len(diff_forms)