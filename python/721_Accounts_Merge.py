class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # make set
        n = len(accounts)
        parent = list(range(n))
        id2email = {}
        for i,item in enumerate(accounts):
            id2email[i] = set(item[1:])     
            
        def find_group(index):
            while index!=parent[index]:
                index = parent[index]
            return index
        
        # generate union commands
        email2group = {}
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email not in email2group:
                    email2group[email] = []
                email2group[email].append(i)
                
        union_command = set()        
        for email in email2group:
            group_len = len(email2group[email])
            for i in range(group_len-1):
                union_command.add((email2group[email][i],email2group[email][i+1]))
                
        # print(union_command)
        # find union
        for command in union_command:            
            first_group = find_group(command[0])
            second_group = find_group(command[1])
            if first_group!=second_group:
                parent[second_group] = first_group
                id2email[first_group] = id2email[first_group].union(id2email[second_group])
                id2email[second_group] = set()
        
        # generate ans
        ans = []
        for i,group_id in enumerate(parent):
            if i==group_id:
                tmp = [accounts[i][0]]
                tmp = tmp+ sorted(list(id2email[i]))
                ans.append(tmp)
        return ans
        