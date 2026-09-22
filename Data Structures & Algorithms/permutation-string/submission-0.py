class Solution:
    def makeDict(self,s1:str) -> dict:
        dictionary_s1 = {}
        for i in s1:
            dictionary_s1[i] = dictionary_s1.get(i,0)+1
        return dictionary_s1 

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dictionary_s1 = self.makeDict(s1)
        
        k = len(s1)
        for r in range(0,len(s2)):
            window = s2[r:r+k]
            dictionary_s2 = self.makeDict(window)
            if dictionary_s2 == dictionary_s1:
                # print(dictionary_s2.keys())
                # print(dictionary_s1.keys())
                return True
            
        return False
            