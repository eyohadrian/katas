def lastStoneWeight(stones: List[int]) -> int:
    stones = [-x for x in stones]
    heapq.heapify(stones)

    while(len(stones) > 1):
        x,y = heapq.heappop(stones), heapq.heappop(stones)

        new_stone = x - y

        if new_stone != 0:
            heapq.heappush(stones, new_stone)

    return 0 if len(stones) == 0 else -stones[0]
