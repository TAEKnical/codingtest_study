# 몸풀기 문제: 배열 정렬하기
def solution(arr):
    arr.sort()
    
    return arr

print(solution([1, -5, 2, 4, 3]))    # [-5, 1, 2, 3, 4]
print(solution([2, 1, 1, 3, 2, 5, 4]))    # [1, 1, 2, 2, 3, 4, 5]
print(solution([6, 1, 7]))    # [1, 6, 7]