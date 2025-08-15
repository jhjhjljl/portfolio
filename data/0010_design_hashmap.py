class HashMap:

    def __init__(self) -> None:
        self.size = 2
        self.hm = [None] * self.size
        self.filled = 0

    def get_index(self, key: str) -> int:
        return hash(key) % self.size

    def resize(self) -> None:
        old_hm = self.hm
        self.size *= 2
        self.hm = [None] * self.size
        for data in old_hm:
            if data:
                for k, v in data:
                    self.set(k, v)

    def set(self, key: str, val: str) -> None:
        if self.filled / self.size > 0.5:
            self.resize()
        idx = self.get_index(key)
        if self.hm[idx] is None:
            self.hm[idx] = []
        for kv in self.hm[idx]:
            if kv[0] == key:
                kv[1] = val
                return
        self.hm[idx].append([key, val])
        self.filled += 1

    def get(self, key: str) -> str:
        idx = self.get_index(key)
        if self.hm[idx] is None:
            return None
        for k, v in self.hm[idx]:
            if k == key:
                return v

    def delete(self, key: str) -> None:
        idx = self.get_index(key)
        if self.hm[idx] is None:
            raise Exception("Key does not exist.")
        for i, (k, _) in enumerate(self.hm[idx]):
            if k == key:
                self.hm[idx].pop(i)
                self.filled -= 1

