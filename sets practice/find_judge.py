def findJudge(n, trust):
    judgeCandidates = set(range(1, n + 1))
    notJudges = set()
    trusted = {}

    for pair in trust:
        notJudges.add(pair[0])
        if pair[1] in trusted:
            trusted[pair[1]] += 1
        else:
            trusted[pair[1]] = 1
    
    judgeCandidates = judgeCandidates - notJudges

    for candidate in judgeCandidates:
        if candidate not in trusted:
            trusted[candidate] = 0
        
        if trusted[candidate] == n -1:
            return candidate
               
    return -1

# n=2
# trust = [[1,2]]

# print(findJudge(n, trust)) # 2

# n=3
# trust = [[1,3],[2,3]] # 3

# print(findJudge(n, trust))

# n=3
# trust = [[1,3],[2,3],[3,1]]

# print(findJudge(n, trust)) #-1

# n = 4
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# print(findJudge(n, trust)) #3

n = 1
trust = []
print(findJudge(n, trust)) #-1