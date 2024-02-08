#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capitals: List[int]) -> int:
        # sort by capital
        sorted_capital_and_profit = []
        for i in range(len(profits)):
            sorted_capital_and_profit.append((capitals[i], profits[i]))
        sorted_capital_and_profit.sort()
        start = 0

        
        q = []
        while k > 0:
            # insert all qualified profit to heap
            while start < len(sorted_capital_and_profit) and sorted_capital_and_profit[start][0] <= w:
                heappush(q, -sorted_capital_and_profit[start][1])
                start += 1
            
            # get max profit
            if len(q):
                w += -heappop(q)
                k -= 1
            else:
                break
            
        return w
# @lc code=end

10\n0\n[1,2,3]\n[0,1,2]
1\n2\n[1,2,3]\n[1,1,2]
