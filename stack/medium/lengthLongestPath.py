# https://leetcode.com/problems/longest-absolute-file-path/description/

import re


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ans = 0
        stack = []

        for s in input.split('\n'):
            count = s.count('\t')

            if stack:
                if stack[-1].count('\t') < count:
                    stack.append(s)
                else:
                    while stack and stack[-1].count('\t') >= count:
                        stack.pop()

                    stack.append(s)
            else:
                stack.append(s)

            if (re.match('[\t]*[A-Za-z0-9\s]*.[.]+', stack[-1])):
                path = []

                for i in stack:
                    path.append(re.sub('[\n\t]*', '', i))

                ans = max(len("\\".join(path)), ans)

        return ans


print(Solution().lengthLongestPath(
    input="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))  # 20
print(Solution().lengthLongestPath(
    input="dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))  # 32
