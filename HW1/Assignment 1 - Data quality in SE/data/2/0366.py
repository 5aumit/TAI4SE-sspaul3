# 우선 순위 큐
# '우선순위가 가장 높은 데이터를 가장 먼저 삭제'하는 자료구조다
# EX) 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인하는 경우에 우선 순위 큐

#  자료구조    -추출되는 데이터-
# Stack -> 가장 나중에 삽입된 데이터
# Queue -> 가장 먼저 삽입된 데이터
# Priority Queue -> 가장 운선순위가 높은 데이터

"""
Heap(힙)
---> 우선 순위 큐를 구현하기 위해 사용하는 자료구조 중 하나
Min Heap( 값이 낮은 데이터 부터 먼저 ) / Max Heap ( 값이 높은 데이터 먼저 ) ---> 추출
-> 다 익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용

우선순위 큐 구현 방식    삽입시간    삭제시간
    리스트             O(1)        O(N)
    힙(Heap)         O(logN)     O(lonN)
"""

import heapq  # minheap으로 , 우선순위 낮은 것 부터 차례대로 --> 오름 차순!!


# heappush ( 특정리스트에, 데이터 넣기)
# heappop (리스트 ) ---> 데이터를 꺼내자

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# 최대 힙을 쓰려면 -value, -heapq 에서 반대로!