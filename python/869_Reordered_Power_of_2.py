class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_list = []
        while n:
            num_list.append(n%10)
            n = n//10
        
        length = len(num_list)
        num_list.sort()
        
        
        # permutation I
#         def backtrack(index,num):
#             if index==length:
#                 return num &(num-1)==0
            
#             for i in range(index,length):
#                 if index==0 and num_list[i]==0:
#                     continue
#                 num_list[index],num_list[i] = num_list[i],num_list[index]                
#                 if backtrack(index+1,num*10+num_list[index]):
#                     return True
#                 num_list[index],num_list[i] = num_list[i],num_list[index]
#             return False


        # permutation II
        visited = [False]*length
        def backtrack(counter,num):
            if counter==length:
                return num &(num-1)==0
            
            for i in range(length):
                if visited[i]:
                    continue
                if num==0 and num_list[i]==0:
                    continue                    
                if i>0 and num_list[i]==num_list[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                if backtrack(counter+1,num*10+num_list[i]):
                    return True
                visited[i] = False
            return False
        
        return backtrack(0,0)