class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 1:
            return 0 if gas[0] > cost[0] else -1
        get_gas = [0 for _ in range(len(gas))]
        for i in range(len(gas)):
            if gas[i] - cost[i] > 0:
                get_gas[i] = 1

        def tryIt(i):
            temp = i
            gas_now = gas[i]
            gas_now -= cost[i]
            i = (i + 1) % len(gas)
            while i != temp:
                gas_now += gas[i]
                gas_now -= cost[i]
                if gas_now < 0:
                    return False
                i = (i + 1) % len(gas)
            return True

        for i in range(len(gas)):
            if get_gas[i] == 1 and get_gas[i - 1] != 1:
                if tryIt(i):
                    return i

        return -1


print(Solution().canCompleteCircuit([4], [5]))
