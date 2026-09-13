class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1

        res = 0
        while l <= r:
            remain = limit - people[r] 
            res += 1
            if people[l] <= remain:
                l+= 1
            r-=1
        
        return res

        # 1 2 2 3 3

        # l     r 
        # res = 1