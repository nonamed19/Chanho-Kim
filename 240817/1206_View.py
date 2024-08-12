T = 10                                      # 총 10개의 테스트케이스가 주어진다.

for _ in range(T):
    n = int(input())                        # 건물의 개수 N이 주어진다. (4 ≤ N ≤ 1000)
    lst = list(map(int, input().split()))   # (0 ≤ 각 건물의 높이 ≤ 255)
    num_building = 0

    for i in range(2, n-2): # 가장 왼쪽 & 오른쪽 2칸은 building X
        building_height = 0

        # i 위치의 building 기준 가장 높은 위치를 building height로 설정
        if lst[i-2] > building_height:
            building_height = lst[i-2]
        if lst[i-1] > building_height:
            building_height = lst[i-1]
        if lst[i+1] > building_height:
            building_height = lst[i+1]
        if lst[i+2] > building_height:
            building_height = lst[i+2]

        # i 위치의 building height가 나머지 4개의 building 보다 높으면, 조망권 확보가 가능함
        if lst[i] > building_height:
            num_building += lst[i] - building_height

    print('#%d %d' %(_+1, num_building))