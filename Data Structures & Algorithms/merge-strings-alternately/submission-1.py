class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        l1,l2 = len(word1),len(word2)
        newword = []
        while (i < l1) and (j < l2):
            newword.append(word1[i])
            newword.append(word2[j])

            i+=1
            j+=1

        if l1 > l2:
            while i < l1:
                newword.append(word1[i])
                i+=1
        else:
            while j < l2:
                newword.append(word2[j])
                j+=1

        return "".join(newword)