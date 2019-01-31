def solution(S, E):
    # write your code in Python 3.6
    A = [[0] * len(S)] * 1000
    counter = 0
    for k in range(len(S)):
        print(S[k], E[k])
        for i in range(S[k], E[k]):
            A[i - 1][k] = 1
    for j in range(1000):
        counter = max(counter, A[j].count(1))
    return counter

if __name__ == '__main__':
    solution([1, 2, 6, 5, 3], [5, 5, 7, 6, 8])