class HashSet:

    def __init__(self) -> None:
        self.hs = [False] * 1000001

    def add(self, key: int) -> None:
        self.hs[key] = True

    def remove(self, key: int) -> None:
        self.hs[key] = False

    def contains(self, key: int) -> bool:
        return self.hs[key]


if __name__ == "__main__":
    hs = HashSet()
    hs.add(3)
    hs.remove(3)
    assert hs.contains(3) == False
