a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))          #곱한 수를 문자로 변환

for i in range(10):           # 0 부터 10 까지
    print(result.count(str(i)))       # 문자열로 바뀐 수들 비교후 출력
