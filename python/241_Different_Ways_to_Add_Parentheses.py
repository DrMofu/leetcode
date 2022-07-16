class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        results = []
        for i,char in enumerate(expression):
            if char in ["-","*","+"]:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if char=="-": results.append(l-r)
                        elif char=="*": results.append(l*r)
                        else: results.append(l+r)
                            
        if not len(results): 
            return [int(expression)]
                
        return results
            