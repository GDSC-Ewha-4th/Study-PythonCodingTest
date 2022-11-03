# BOJ 1182번 부분수열의 합
# 정수의 개수: N, 부분수열의 합인 정수: S

global ans;     # 가능한 모든 경우의 인덱스 set의 배열
# 수열 [-7, -3, -2, 5, 8]이고, S=0인 경우: ans=[(1, 2, 3)]

def Backtrack(arr, visited, curIdx, N, S, sumSet): 
    global ans;

    visited[curIdx] = True
    sumSet.add(curIdx)

    sumAns = 0
    for s in sumSet:
        sumAns += arr[s]
    if sumAns==S : 
        ans+=1

    for i in range(curIdx+1, N):    # 이번 정답 배열에 넣을 수 있는 나머지 수
        if visited[i]==False:
            Backtrack(arr, visited, i, N, S, sumSet)
            visited[i] = False
            sumSet.remove(i)    # set에서는 지울 요소를 직접 입력

def solution():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    global ans;
    ans = 0

    # 부분 수열의 맨 앞 idx
    for n in range(N):  # 0~N-1
        #print("=========================")
        Backtrack(arr, [False for _ in range(N)], n, N, S, set())
        #print(ans)
    
    print(ans)
    #print(len(ans))

solution()
