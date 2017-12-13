class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '' and b == '':
            return '0'
        elif a == '':
            return b
        elif b == '':
            return a

        if len(a) > len(b):
            b = b.zfill(len(a)+1)
            a = a.zfill(len(a)+1)
        elif len(b) > len(a):
            a = a.zfill(len(b)+1)
            b = b.zfill(len(b)+1)
        else:
            a = a.zfill(len(a)+1)
            b = b.zfill(len(b)+1)

        length = len(a)
        alist = [i for i in a]
        blist = [i for i in b]

        i = length-1
        carry = False
        result = ['0']*length
        while i >= 0:
            if blist[i] == '1' and alist[i] == '1' and carry:
                result[i] = '1'
            elif blist[i] == '1' and alist[i] == '1' and not carry:
                result[i] = '0'
                carry = True
            elif (blist[i] == '1' or alist[i] == '1') and carry:
                result[i] = '0'
            elif (blist[i] == '1' or alist[i] == '1') and not carry:
                result[i] = '1'
            elif carry:
                result[i] = '1'
                carry = False
            else:
                result[i] = '0'
            i -= 1
        
        if result[0] == '0':
            return "".join(result[1:])
        else:
            return "".join(result)


print(Solution().addBinary('1111', '1111'))
