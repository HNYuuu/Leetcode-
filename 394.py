class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        times = []
        done = [0]

        def traverse(sub, i, j):
            k = i
            while k < j:
                if s[k].isdigit():
                    num_i = s.find('[', k)
                    times.append(int(s[k:num_i]))
                    sub += traverse('', num_i+1, j)
                    k = done[0]+1
                elif s[k] == ']':
                    done[0] = k
                    return (times.pop())*sub
                else:
                    sub += s[k]
                    k += 1
            return sub

        return traverse("", 0, len(s))

print(Solution().decodeString("2[abc]3[cd]ef"))