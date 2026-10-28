class TimeMap:

    def __init__(self):
        self.timekey = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timekey[key].append([value,timestamp])
    


    def get(self, key: str, timestamp: int) -> str:
        
        keylist = self.timekey[key]

        l,r = 0,len(keylist)-1
        res = 0

        if not keylist:
            return ""

        if keylist[0][1] > timestamp:
            return ""

        while l<=r:
            m = (l+r)//2
            mid = keylist[m][1]
            if mid <= timestamp:
                res = m
                l = m+1
            else:
                r = m-1


        return keylist[res][0]
