# https://velog.io/@qlwb7187/%EB%AA%A8%EB%93%88%EB%9F%AC-%EC%97%B0%EC%82%B0Modular-arithmetic

# https://ohgym.tistory.com/13

a = int(input())
b = int(input())
m = int(input())

(a + b) % m == (a % m + b % m) % m

(a * b) % m == (a % m * b % m) % m

(a / b) % m == (a % m * (b ^ -1) % m) % m


(b ^ -1) % m == (b ^ (m - 2)) % m  # b와 m이 서로소인 경우 성립


'''
(x + y) % k = 0
x % k = i

y % k = (k - i) % k


'''
