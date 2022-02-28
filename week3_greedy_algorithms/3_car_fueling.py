# python3
import sys


def compute_min_refills(distance, tank, stops):
    # Let us implement a greedy algorithm that chooses to refill the 
    # tank only if it is not possible to reach at the next gas station

    # these are added to to check if it possible to reach at distance 
    # from the last gas stop. The first one is to check whether to stop 
    # right before distance, while the second one is to check if it 
    # possible to reach at the  distance from the last stop

    stops.extend([distance, distance])
    last_pit = 0 
    refills = []
    for i in range(len(stops)-1):
        drive_range = last_pit + tank 
        if stops[i] <= drive_range:
            if stops[i+1] > drive_range:
                last_pit = stops[i] 
                refills.append(last_pit)
        else:
            return -1
    return refills 



if __name__ == '__main__':
    # d, m, _, *stops = map(int, sys.stdin.read().split())
    d = 11
    m = 3
    stops = [1, 2, 5, 7, 9]
    print(compute_min_refills(d, m, stops))
