# BOJ 1541번 잃어버린 괄호

def solution():
    # 55 - 50 + 40
    exp = input().split('-')    # 묶인 애들은 숫자 1개이거나 +로 더해진 수들

    num = []    # 나누어진 수들의 합을 저장할 배열

    for e in exp:
        sum = 0
        tmp = e.split('+')
        for t in tmp:
            sum += int(t)
        num.append(sum)    
    
    ans = num[0]
    for i in range(1, len(num)):
        ans -= num[i]
    
    print(ans)

solution()
