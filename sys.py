import sys
 
inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
# sys를 쓰는 이유는 input 보다 실행속도가 빠르고 메모리 참조가 덜함
#sys.stdin.readline() 만 사용할경우 문자나 정수 다양한 언어 리스트 저장
# map 함수로 int로 바꿔서 받아준다
