class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append([value, timestamp])
        else:
            self.data[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        table = self.data[key]
        n = len(table)
        left = 0
        right = n - 1
        res = -1
        while(left <= right):
            mid = (left + right) // 2
            if (table[mid][1] <= timestamp):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        if res == -1:
            return ""
        else:
            return table[res][0]


        
