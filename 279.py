class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # use dp
        exponent = []
        i = 1
        while i*i <= n:
            exponent.append(i*i)
            i += 1
        exponent.reverse()

        store = {}
        results = []
        def tryit(n, i, count):
            if n in store.keys():
                # print('hit')
                return store[n]+count
            for index in range(i, len(exponent)):
                # if now n is smaller than exponent[index]
                if n < exponent[index]:
                    continue
                # if exponent[index] | n, it's the minimum of n and store it
                if n % exponent[index] == 0:
                    results.append(count+(n//exponent[index]))
                    store[n] = (n//exponent[index])
                    return store[n]+count
                else:
                    # get the remainder and recursive
                    temp = tryit(n-(n//exponent[index])*exponent[index], index+1, count+(n//exponent[index]))
                    results.append(temp)

        tryit(n, 0, 0)
        return min(results)

print(Solution().numSquares(1))