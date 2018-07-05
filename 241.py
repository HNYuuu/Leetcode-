class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def traverse(formula, i, j):
            result = []
            if formula[i:j].isdigit():
                return [formula[i:j]]
            else:
                for index in range(i, j):
                    if not formula[index].isdigit():
                        lrs = traverse(formula, i, index)
                        rrs = traverse(formula, index+1, j)
                        for lr in lrs:
                            for rr in rrs:
                                result.append(str(eval(lr+formula[index]+rr)))
                return result.copy()

        result = traverse(input, 0, len(input))
        return [int(x) for x in result]

print(Solution().diffWaysToCompute("2"))