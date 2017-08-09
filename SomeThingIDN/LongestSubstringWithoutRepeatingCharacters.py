'''Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=len(s)
        if length==1:
            return 1
        longest=0
        lenofSubstr=0
        i=0
        while i <length:
            if longest>length - i:
                break
            lenofSubstr=0
            for j in range(i+1,length):
                lenofSubstr +=1

                tmp=s[i:j]
                index =tmp.find(s[j])
                if index !=-1:
                    i +=index
                    k = j+1
                    while(k<length) and (s[1+i==s[k]]):
                        i +=1
                        k +=1
                    if longest <lenofSubstr:
                        longest=lenofSubstr
                    break
                if j == length -i:
                    lenofSubstr =lenofSubstr +1
                    break
            i +=1
        return longest
    def lengthOfLongestSubString(self, s):
        longest, start, visited = 0, 0, [False for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest