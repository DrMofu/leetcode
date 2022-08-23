class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ans_list = set()
        for email in emails:
            ans = ""
            meet_at = False
            meet_plus=False
            for char in email:
                if meet_at:
                    ans+=char
                    continue
                if char=="@":
                    meet_at = True
                    ans+=char
                    continue
                if meet_plus:
                    continue
                if char==".":
                    continue
                if char=="+":
                    meet_plus= True
                    continue
                ans+=char
                
            ans_list.add(ans)
        return len(ans_list)