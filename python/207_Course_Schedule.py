class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pre_list = {}
        for i in range(numCourses):
            pre_list[i] = []
            
        for item in prerequisites:
            pre_list[item[0]].append(item[1])
            
        for start_course in range(numCourses):
            course_set = set([start_course])
            course_queue = [start_course]
            while course_queue:
                course = course_queue.pop(0)
                pre_course_list = pre_list[course]
                for pre_course in pre_course_list:
                    # 优化，我们已知id<start_course的课程没有问题，其不会出现在循环中。所以直接忽略
                    if pre_course<start_course:
                        continue
                    if pre_course==start_course:
                        return False
                    if pre_course not in course_set:
                        course_set.add(pre_course)
                        course_queue.append(pre_course)
        return True
                