"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        value = 0
        id2e = {e.id: e for e in employees}
        queue = []
        queue.append(id)
        while queue:
            eid = queue.pop(0)
            if eid in id2e.keys():
                value += id2e[eid].importance
                for sub in id2e[eid].subordinates:
                    queue.append(sub)
        return value

print(Solution().getImportance([[1,2,[2]],[2,3,[]]], 2))