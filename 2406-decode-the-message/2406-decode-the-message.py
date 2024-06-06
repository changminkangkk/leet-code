class Solution:
    def unique_everseen(self, iterable):
        seen = set(" ")
        for element in filterfalse(seen.__contains__, iterable):
            seen.add(element)
            yield element

    def decodeMessage(self, key: str, message: str) -> str:
        key_uniq = list(self.unique_everseen(key))
        d = dict(zip(key_uniq, ascii_lowercase)) | {" ": " "}
        return "".join(map(d.__getitem__, message))