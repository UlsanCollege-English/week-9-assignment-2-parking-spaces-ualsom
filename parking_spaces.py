"""
HW02 — Parking Spaces: Minimum Spots Needed

Implement min_parking_spots(intervals) -> int

Behavior:
- Given a list of (start, end) times, return the minimum number of parking spots
  so that no car waits. If a car leaves at time t and another arrives at time t,
  the same spot can be reused.
"""

import heapq

def min_parking_spots(intervals):
    if not intervals:
        return 0

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap (stores current cars by their leaving times)
    heap = []
    max_spots = 0

    for start, end in intervals:
        # Remove cars that already left before this car arrives
        while heap and heap[0] <= start:
            heapq.heappop(heap)

        # Add current car's leaving time
        heapq.heappush(heap, end)

        # Track the peak number of cars parked
        max_spots = max(max_spots, len(heap))

    return max_spots


if __name__ == "__main__":
    print(min_parking_spots([]))  # → 0
    print(min_parking_spots([(1, 2)]))  # → 1
    print(min_parking_spots([(1, 3), (2, 4), (3, 5)]))  # → 2
    print(min_parking_spots([(1, 2), (2, 3), (3, 4)]))  # → 1
    print(min_parking_spots([(1, 5), (2, 3), (4, 6)]))  # → 2
