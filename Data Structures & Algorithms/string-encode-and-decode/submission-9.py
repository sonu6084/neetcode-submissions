class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
        enc = "#$%###########".join(strs)
        print(enc)
        return enc

    def decode(self, s: str) -> List[str]:

        print(s)
        if s == "":
            return [""]
        if s == "None":
            return []

        dec = s.split("#$%###########")
        return dec
