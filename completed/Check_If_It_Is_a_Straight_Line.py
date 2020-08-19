#class Solution:
def checkStraightLine(coordinates) -> bool:
    if len(coordinates) <= 2: return True
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    if x1 == x2:
        # x = const = x1
        for x, y in coordinates[2:]:
            if x != x1: return False
    elif y1 == y2:
        # y = const = y1
        for x, y in coordinates[2:]:
            if y != y1: return False
    else:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
    for x, y in coordinates[2:]:
        if y != x * k + b: return False
    return True


# a = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# a = [[1,1],[2,2],[7,7]]
a = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

print(f'a == {a}\n\t ==> answer == {checkStraightLine(a)}')

'''
I like this solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
                return False
        return True	
'''