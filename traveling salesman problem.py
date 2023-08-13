import itertools

#경로의 거리를 계산하는 함수
def calculate_distance(path, graph):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i+1]]
    distance += graph[path[-1]][path[0]]  #마지막 도시에서 출발 도시로 돌아오는 거리 추가
    return distance

#외판원 문제를 브루트포스 방식으로 푸는 함수
def tsp_bruteforce(graph):
    num_cities = len(graph)
    min_distance = float('inf')  #초기 최단 거리를 무한대로 설정
    min_path = None

    #모든 가능한 경로의 순열 생성
    for path in itertools.permutations(range(num_cities)):
        distance = calculate_distance(path, graph)
        if distance < min_distance:
            min_distance = distance
            min_path = path

    return min_path, min_distance

#예시
graph = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

#최단 경로와 거리 계산
min_path, min_distance = tsp_bruteforce(graph)

#결과 출력
print("최단 경로:", min_path)
print("최단 거리:", min_distance)
