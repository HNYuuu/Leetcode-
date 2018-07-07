class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if len(preorder) == 1 and preorder[0] == '#':
            return True
        elif preorder[0] == '#' or preorder[-1] != '#':
            return False

        preorder = preorder.split(',')[:-1]
        count = 0
        for node in preorder:
            if node.isdigit():
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        if count == 0:
            return True
        else:
            return False

print(Solution().isValidSerialization("#,1"))