class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [set() for _ in range(target + 1)]
        dp[0].add((0,))

        for t in range(target + 1):
            for n in nums:
                if t - n < 0:
                    continue
                for sum_l in dp[t - n]:
                    new_sl = sorted([*sum_l, n])
                    dp[t].add(tuple(new_sl))
        return [[a for a in s if a != 0] for s in dp[target]]

    def combinationSumA(self, nums: List[int], target: int) -> List[List[int]]:
        t_result = set()

        def combo_traverse(combo, target):
            csum = sum(combo)
            if csum > target:
                return
            elif csum == target:
                t_result.add(tuple(sorted(combo)))
                return
            for n in nums:
                n_combo = combo[:]
                n_combo.append(n)
                combo_traverse(n_combo, target)

        combo_traverse([], target)
        return [list(t) for t in t_result]
