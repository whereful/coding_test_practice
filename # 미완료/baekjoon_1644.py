'''
# comment

41 - 1. 41 자체 소수
2. 2 + 39   // 39를 3부터 시작하는 누적합으로 나타낼 수 있는가 == 39 + 2(41)를 2부터 시작하는 누적합으로 나타낼 수 있는가 
3. 3 + 38   // 38을 5부터 시작하는 누적합으로 나타낼 수 있는가 == 38 + 2 + 3(41 + 2)를 2부터 시작하는 누적합으로 나타낼 수 있는가
4. 5 + 36   // 36을 7부터 시작하는 누적합으로 나타낼 수 있는가 == 36 + 2 + 3 + 5(41 + 2 + 3)를 2부터 시작하는 누적합으로 나타낼 수 있는가
5. 7 + 34   // 34를 11부터 시작하는 누적합으로 나타낼 수 있는가 == 34 + 2 + 3 + 5 + 7(41 + 2 + 3 + 5)를 2부터 시작하는 누적합으로 나타낼 수 있는가

prime_list[i] + n - prime_list[i] // n + (2 + 3 + ... prime_list[i - 1])를 2부터 시작하는 누적합으로 나타낼 수 있는가

'''

'''
에라토스테네스의 체
부분합
투 포인터?

https://velog.io/@guri_coding/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8A%A4%ED%84%B0%EB%94%94-%EB%B0%B1%EC%A4%80-1644%EB%B2%88-%EC%86%8C%EC%88%98%EC%9D%98-%EC%97%B0%EC%86%8D%ED%95%A9-feat.-Python

'''


# n에 대한 에라토스테네스의 체 배열을 설정하는 함수




from math import sqrt
def eratos():
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if is_prime[i] == True:
            mul = 2
            while i * mul <= n:
                is_prime[i * mul] = False
                mul += 1

    return is_prime


# arr 원소에 대한 누적합 배열을 설정하는 함수
def prefix_list(arr):
    s = 0
    prefix = []
    for a in arr:
        s += a
        prefix.append(s)

    return prefix


n = int(input())
is_prime = eratos()

# 에라토스테네스의 체를 통해 n 이하의 소수를 저장하는 배열
prime_list = [i for i in range(2, n + 1) if is_prime[i] == True]

prefix = prefix_list(prime_list)

# 누적합을 집합으로 설정
prefix_set = set(prefix)

# n 자체가 소수인지를 저장
answer = int(is_prime[n])
pre = 0

for p in prime_list:

    if p >= n // 2 + 1:
        break

    # comment의 내용을 구현
    answer += int(n + pre in prefix_set)

    pre += p

print(answer)
