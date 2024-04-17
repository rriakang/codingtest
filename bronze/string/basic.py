

# import sys
# n = int(sys.stdin.readline())
# for i in range(n):
#     s= str(sys.stdin.readline())
#     a = s[0]
#     b = s[-2]
#     print(f"{a}{b}")



# sys.stdin.readlin을 통해서 입력받는 경우 개행문자가 맨 마지막에 붙여서 입력된다.
# 따라서 s[-1]을 하면 s'마지막 문자인 '\n'이 출력이된다.
    
n = int(input())
for i in range(n):
    s = input()
    a = s[0]
    b = s[-1]
    print(f"{a}{b}")



# 파이썬에서는 ord()와 chr() 함수를 통해 아스키코드로, 아스키코드를 문자로 변환시킬수있음
    
n = input()

print(ord(n))

