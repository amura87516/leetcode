#
# @lc app=leetcode id=2709 lang=python3
#
# [2709] Greatest Common Divisor Traversal
#

# @lc code=start
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # edge case, O(nlogn)
        # [1], [1, 1], [2, 2]
        boolean_filter = set(nums)
        non_duplicated_nums = list(set(nums))
        if non_duplicated_nums[0] == 1 and len(nums) > 1:
            return False
        elif len(non_duplicated_nums) == 1:
            return True
        nums = non_duplicated_nums

        # get maximum index
        maximun_index = 0
        for i in range(1, len(nums)):
            if nums[maximun_index] < nums[i]:
                maximun_index = i

        # build prime table
        level = len(str(nums[maximun_index]))
        is_odd_primes = [True] * (int(10 ** level) // 2) 
        primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,]
        i = 0
        while i < len(primes):
            factor = 3
            prime_index = (primes[i] * factor - 1) // 2
            while prime_index < len(is_odd_primes):
                is_odd_primes[prime_index] = False

                factor += 2
                prime_index = (primes[i] * factor - 1) // 2
            i += 1

        # Early return
        # if num is prime and no num's muplican in nums, return False
        maximum = nums[maximun_index]
        for num in nums:
            if num == 2 or num & 1 and is_odd_primes[(num - 1) // 2]:
                factor = 2
                is_multiply_in_nums = False
                while num * factor <= maximum:
                    if num * factor in boolean_filter:
                        is_multiply_in_nums = True
                        break
                    factor += 1
                if not is_multiply_in_nums:
                    return False

        def factorizes(num):
            res = set()
            while num & 1 == 0:
                num //= 2
                res.add(2)
            
            i = 1
            prime = i * 2 + 1
            while i < len(is_odd_primes) and prime <= num:
                if num % prime == 0:
                    while num % prime == 0:
                        num //= prime
                    res.add(prime)
                prime = i * 2 + 1
                i += 1
            return res
            
        # BFS, O(n^2)
        # try to connect all nodes from root
        base_prime_factors = factorizes(nums[0])
        q = [0]
        not_visited_indexes = [i for i in range(len(nums)) if i != 0]
        while len(q):
            current_index = q[0]
            q = q[1:]

            i = 0
            while i < len(not_visited_indexes):
                candidate_inedx = not_visited_indexes[i]
                candidate_factors = factorizes(nums[candidate_inedx])
                if base_prime_factors.intersection(candidate_factors):
                    base_prime_factors = base_prime_factors.union(candidate_factors)
                    q.append(candidate_inedx)
                    del not_visited_indexes[i]
                else:
                    i += 1

        # check if there are still some node that cannot be connected
        return len(not_visited_indexes) == 0        
# @lc code=end

