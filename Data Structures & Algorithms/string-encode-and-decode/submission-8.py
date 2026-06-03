class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_msg = ""
        for i in strs:
            encode_msg = encode_msg + str(len(i)) + "#" + i
        
        print(encode_msg)

        return encode_msg

    def decode(self, s: str) -> List[str]:
        decode_msg = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            encoder = s[i:j]
            
            decode_msg.append(s[j+1:j+1+int(encoder)])
            
            i=j+1+int(encoder)

        return decode_msg

