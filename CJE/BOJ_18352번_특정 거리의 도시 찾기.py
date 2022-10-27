# BOJ 18352번 특정 거리의 도시 찾기

from collections import deque
import sys
input = sys.stdin.readline

def solution():
    N, M, K, X = map(int, input().split())

    # 인덱스를 1부터 시작하기 위해 N+1
    graph=[[] for _ in range(N+1)]
    for m in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)

    dist=[-1]*(N+1)    # 시작 노드와의 거리, 방문하지 않은 노드는 -1
    dist[X] = 0 # 자기 자신의 거리는 0

    Q = deque()
    Q.append(X)

    while Q:
        # 방문 처리
        v = Q.popleft()

        # v와 붙어있는 노드 방문
        for nextV in graph[v]:
            if dist[nextV]==-1:
                Q.append(nextV)
                dist[nextV]=dist[v]+1

    if K in dist:
        for n in range(N+1):
            if dist[n]==K:
                print(n)
    else: 
        print(-1)

solution()
