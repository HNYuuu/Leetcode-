# 给定一个N，找出所有长为N的并且符合 i%(index+1) == 0 or (index+1)%i == 0 
# 规则的排列个数。知道这道题一定使用回溯法，但是被题目忽悠了，因为它并不是真的需要
# 一个数组来存放目前的排列，它所要的只有一个数字，因此不需要构造一个数组，这样会造
# 成大数据的TLE，将回溯时的第二个参数改为一个常数，表示当前的索引即可

class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.count = 0
        store = {i for i in range(1, N+1)}

        def permutation(N, index):
            if index == N:
                self.count += 1
            else:
                for i in store:
                    if i%(index+1) == 0 or (index+1)%i == 0:
                        store.remove(i)
                        index += 1
                        permutation(N, index)
                        index -= 1
                        store.add(i)
        permutation(N, 1)
        return self.count

print(Solution().countArrangement(3))
