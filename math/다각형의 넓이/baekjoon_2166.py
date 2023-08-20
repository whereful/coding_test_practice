'''
https://my-coding-notes.tistory.com/258

https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0#:~:text=%EC%A0%95%EB%8B%A4%EA%B0%81%ED%98%95%EC%9D%98%20%EB%84%93%EC%9D%B4%EB%A5%BC%20%EA%B5%AC,%EC%9D%98%20%EC%A4%91%EC%8B%AC%EC%9C%BC%EB%A1%9C%20%EB%AA%A8%EC%9D%B4%EB%8A%94%20%EC%84%A0%EB%B6%84

'''

import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

A = sum([arr[i][0] * arr[(i + 1) % n][1] for i in range(0, n - 1 + 1)])
B = sum([arr[i][1] * arr[(i + 1) % n][0] for i in range(0, n - 1 + 1)])

print(abs(A - B) / 2)
