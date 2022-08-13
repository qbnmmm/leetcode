# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4 = [None] * 4
        self.cache = []  # 用来存储调用read4时未读取的字符

    def read(self, buf: list[str], n: int) -> int:
        while n > len(self.cache):
            cnt = read4(self.buf4)
            if cnt > 0:
                self.cache.extend(self.buf4[:cnt])  # 先把read4读取的字符放入缓存
            else:
                break
        toRead = len(self.cache[:n])
        buf[:toRead] = self.cache[:toRead]
        self.cache = self.cache[toRead:]
        return toRead
