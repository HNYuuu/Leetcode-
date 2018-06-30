class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')

        while len(version1) > 0 and int(version1[-1]) == 0:
            del version1[-1]
        while len(version2) > 0 and int(version2[-1]) == 0:
            del version2[-1]

        i,j = 0, 0
        while i < len(version1) and j < len(version2):
            if int(version1[i]) < int(version2[j]):
                return -1
            elif int(version1[i]) > int(version2[j]):
                return 1
            else:
                i += 1
                j += 1
        if i == len(version1) and j == len(version2):
            return 0
        elif i == len(version1):
            return -1
        else:
            return 1