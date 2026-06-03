class Solution:
    def rob(self, packages: List[int]) -> int:
        if not packages:
            return 0
        
        if len(packages) < 3:
            return max(packages)
            
        pack1 = packages[0]
        pack2 = packages[1]
        pack2 = max(pack1,pack2)
        
        for i in range(2,len(packages)):
            temp = pack2
            pack2 = max(pack2,packages[i]+pack1)
            pack1 = temp
            # packages[i] = max(packages[i-1],packages[i] + packages[i-2])
            
        return pack2