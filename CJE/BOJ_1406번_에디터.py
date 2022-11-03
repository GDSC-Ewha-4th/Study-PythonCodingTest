# BOJ 1406번 에디터

import sys
input = sys.stdin.readline

def solution():
    Left = list(input().rstrip())
    Right = []
    
    M = int(input())    # 명령어의 개수 M
    for m in range(M):
        cmd = input().split()
        if cmd[0]=='L': # <-
            if Left:
                Right.append(Left.pop())

        elif cmd[0]=='D':   # ->
            if Right:
                Left.append(Right.pop())

        elif cmd[0]=='B':   # 커서의 왼쪽 문자 삭제
            if Left:
                Left.pop()
        elif cmd[0]=='P':   # 커서의 왼쪽에 문자를 추가
            add = cmd[-1]
            Left.append(add)
    
    Right = reversed(Right)
    Left.extend(Right)
            
    ans = ""
    for L in Left:
        ans += L
    print(ans)

solution()
