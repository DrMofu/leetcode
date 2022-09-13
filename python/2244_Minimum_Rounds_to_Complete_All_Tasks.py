class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        task_counter = {}
        for task in tasks:
            task_counter[task] = task_counter.get(task,0)+1
            
        ans = 0
        for task_key in task_counter:
            task_num = task_counter[task_key]
            while task_num>4:
                ans+=1
                task_num-=3
            if task_num==4:
                ans+=2
            elif task_num==3 or task_num==2:
                ans+=1
            else:
                return -1
        return ans
            