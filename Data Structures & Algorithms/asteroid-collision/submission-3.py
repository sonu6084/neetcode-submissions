class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        rem = []
        for i in asteroids:
            if not rem:
                rem.append(i)
                continue
            
            
            while rem:
                first = rem.pop()
                if (first > 0 and i > 0) or (first < 0 and i < 0) or (first < 0 and i > 0): 
                    rem.append(first)
                    rem.append(i)
                    break
                elif abs(first) > abs(i):
                    rem.append(first)
                    break
                elif abs(first) < abs(i):
                    if not rem:
                        rem.append(i)
                        break
                elif abs(first) == abs(i):
                    break
            
        return rem