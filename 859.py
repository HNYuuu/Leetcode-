class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        a_dict, b_dict = {}, {}
        dif = 0
        for i in range(len(A)):
            a_dict[A[i]] = 1 if A[i] not in a_dict.keys() else 1+a_dict[A[i]]
            b_dict[B[i]] = 1 if B[i] not in b_dict.keys() else 1+b_dict[B[i]]
            if A[i] != B[i]:
                dif += 1

        for key in a_dict.keys():
            if key not in b_dict.keys():
                return False
            if a_dict[key] != b_dict[key]:
                return False

        if dif == 2:
            return True
        elif dif == 0 and len(set(list(A))) < len(A):
            return True
        else:
            return False

print(Solution().buddyStrings('bc', 'ab'))