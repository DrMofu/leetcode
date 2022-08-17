class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        for word in words:
            morse_str = ""
            for char in word:
                morse_str += morse_code[ord(char)-ord("a")]
            ans.add(morse_str)
        return len(ans)