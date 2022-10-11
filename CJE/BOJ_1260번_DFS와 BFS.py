# BOJ 1260번 DFS와 BFS
# 정점의 개수: N, 간선의 개수: M, 탐색을 시작할 정점의 번호: V

from collections import deque


def DFS(graph, v, ans, visited):
    # 이번 노드(v) 방문 처리
    visited[v] = True
    ans.append(v)

    # 이번 노드(v)와 가까운 노드에 방문
    for next_V in graph[v]:
        if visited[next_V]==False:  # 방문한 적 없어야 함
            DFS(graph, next_V, ans, visited)
    
    return ans


def BFS(graph, v, visited):
    # 스택에 방문할 노드를 쌓아 넣기
    Q = deque()
    
    ans = []

    # 첫 방문 노드 방문 & 주변 노드를 큐에 넣기
    visited[v] = True
    ans.append(v)
    for next_V in graph[v]:
        Q.append(next_V)

    while Q:    
        # 큐의 앞부터 방문
        v = Q.popleft()
        visited[v] = True
        ans.append(v)

        # 이번에 방문한 노드의 주변 노드를 큐에 넣기
        for next_V in graph[v]:
            if visited[next_V]==False and next_V not in Q: # 아직 방문한 적 없어야 함
                Q.append(next_V)
        
    return ans


def solution():
    # input 받기
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for m in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for g in graph:
        g.sort()

    ans = DFS(graph, V, [], [False for _ in range(N+1)])
    answer = ""
    for a in ans:
        answer += str(a) + " "
    print(answer)

    ans = BFS(graph, V, [False for _ in range(N+1)])
    answer = ""
    for a in ans:
        answer += str(a) + " "
    print(answer)

solution()

### 문제 접근 방식 ###
# 단순 DFS와 BFS 알고리즘 사용...

### 해법을 찾는데 결정적이었던 깨달음 ###
# 딱히 없음... 대놓고 DFS, BFS 알고리즘을 쓰라고 해서...

### 문제 풀이 로직 ###
# DFS
# 첫 노드 V1에 방문 - 방문 처리
# V1와 붙어있는 노드 V2에 방문
# V2와 붙어있는 노드 V3에 방문...
# -> 재귀 방식 사용
# 다음 노드에 방문하기 전 아직 방문한 적 없는 노드인지 체크

# BFS
# 방문해야할 노드들을 큐에 넣어둠
# 첫 노드 V1부터 큐에 넣음
# 큐의 맨 앞부터 꺼냄 - 꺼낸 노드에 방문, 방문한 노드와 붙어있는 노드를 큐에 넣음 (방문했는지 여부 체크)
# 더이상 방문해야할 노드가 남아있지 않으면 while문 종료 (=큐가 비게 됨)