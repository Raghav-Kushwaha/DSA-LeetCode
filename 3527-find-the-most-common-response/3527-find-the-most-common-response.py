from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count=Counter()
        for daily_responses in responses:
            for response in set(daily_responses):
                count[response]+=1
        max_freq=max(count.values())

        ans = None
        for response , freq in count.items():
            if freq==max_freq:
                if ans == None or response<ans:
                    ans = response
        
        return ans