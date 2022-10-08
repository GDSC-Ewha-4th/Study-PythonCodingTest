# BOJ 2805번 나무자르기
# 필요한 나무의 길이: M, 나무의 수: N, 자르는 높이: H

def solution():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    minH = 0; maxH = max(trees) 
    
    ans = 0
    while minH <= maxH :
        midH = (minH + maxH) // 2

        treeSum = 0
        for t in trees:
            if t-midH > 0:
                treeSum += (t - midH)

        # 자른 나무의 길이 >= 필요 길이 -> 덜 잘라도 됨
        if treeSum >= M :
            minH = midH + 1
            ans = midH
        # 자른 나무의 길이 < 필요 길이 -> 더 잘라야 함 
        else:
            maxH = midH - 1

    return ans

print(solution())
