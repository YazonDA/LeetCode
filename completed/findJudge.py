class Solution:
    # def findJudge(self, N: int, trust: List[List[int]]) -> int:
    def findJudge(self, N, trust):
        # the special variant
        if N == 1 and len(trust) == 0: return 1
        # list of people who trust someone
        trust_from = list(set(i[0] for i in trust))
        print(trust_from)
        # list of people someone trust
        judge_suppose = [i[1] for i in trust if i[1] not in trust_from]
        print(judge_suppose)
        # list of prospective judges
        judge_prospective = [i for i in list(set(judge_suppose)) if judge_suppose.count(i) == N - 1]
        print(judge_prospective)
        if len(judge_prospective): return judge_prospective[0]
        return -1

a = Solution
print(a.findJudge(a, 4, [[1,3],[1,4],[2,3]]
))

''' GOOD SOLUTION
		counter_array = [0] * (N + 1)
        if len(trust) == 0 and N < 2:
            return 1
        if len(trust) == 0 and N > 1:
            return -1
        for item in trust:
            counter_array[item[1]] += 1
            counter_array[item[0]] -= 1
        judge = max(counter_array)
        if judge == N - 1:
            return counter_array.index(judge)
        return -1
'''