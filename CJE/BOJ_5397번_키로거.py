# BOJ 5397번 키로거

def solution():
    T = int(input())    # 테스트 케이스의 개수

    # 입력 키의 경우: 알파벳 대소문자, 숫자, 백스페이스, 화살표
    # 스택을 2개 사용
    for t in range(T):
        keyLoger = input()
        Left = []
        Right = []

        for key in keyLoger:
            if key == "<":  # 왼쪽으로 이동: Left 맨 끝 -> Right 맨 끝
                if Left:    # 왼쪽 스택이 비어있지 않음을 확인
                    Right.append(Left.pop())
            elif key == ">":    # 오른쪽으로 이동: Right 맨 끝 -> Left 맨 끝
                if Right:       # 오른쪽 스택이 비어있지 않음을 확인
                    Left.append(Right.pop())
            elif key == "-":    # 지우기
                if Left:    # 지금 커서의 왼쪽에 지울 문자가 있음을 확인
                    Left.pop()            
            else:   # 알파벳 대소문자, 숫자
                Left.append(key)    # 지금 들어온 문자들은 일단 다 왼쪽 스택에 넣어두기

        Right = reversed(Right)
        Left.extend(Right)
        
        ans = ""
        for L in Left:
            ans += L
        print(ans)

solution()
