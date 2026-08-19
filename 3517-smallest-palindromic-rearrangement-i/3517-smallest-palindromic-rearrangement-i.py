class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l=len(s)
        lefthalf=s[0:l//2]
        sortedlefthalf="".join(sorted(lefthalf))
        righthalf=sortedlefthalf[::-1]
        if l%2==0:
            return sortedlefthalf+righthalf
        else:
            midd=s[l//2]
            return sortedlefthalf+midd+righthalf