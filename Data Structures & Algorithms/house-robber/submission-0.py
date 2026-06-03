class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = []
        rob.append(0)
        rob.append(0)
        rob = rob + nums


        for i in range(2,len(rob)):
            rob[i] = max(rob[i-1],rob[i]+rob[i-2])

        
        print(rob)
        return rob[-1]