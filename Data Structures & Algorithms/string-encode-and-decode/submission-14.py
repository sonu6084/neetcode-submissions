class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        for i in strs:
            encode_string = encode_string + str(len(i)) + "#" + i

        print(encode_string)
        return encode_string

    def decode(self, s: str) -> List[str]:

        decoded_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            decode_num = s[i:j]
                
            decoded_list.append(s[j+1:j+1+int(decode_num)])
            # print(decoded_list)
            
            i=j+1+int(decode_num)
            
            
        return decoded_list



