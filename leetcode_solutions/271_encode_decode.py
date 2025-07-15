class Solution:
    def encode(self, strs: list[str]) -> str:
        if strs == [""]:
            return "<EMPTY_STRING_LIST>"  # special token
        if strs == []:
            return "<EMPTY_LIST>"
        delimiter = "(*&^%$#@!|:L"
        return delimiter.join(strs)

    def decode(self, s: str) -> list[str]:
        if s == "<EMPTY_STRING_LIST>":
            return [""]
        if s == "<EMPTY_LIST>":
            return []
        delimiter = "(*&^%$#@!|:L"
        return s.split(delimiter)