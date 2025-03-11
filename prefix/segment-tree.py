from typing import List

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        # since we are doing 2 * i + 1 stuff below using 4 * self.n to ensure enough storage
        self.t = [0] * (4 * self.n)
        self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums: List[int], i: int, l: int, r: int):
        if l == r:
            self.t[i] = nums[l]
        else:
            m = (l + r) // 2
            # just the standard formula for left and right child
            # 2 * i + 1 => left child
            # 2 * i + 2 => right child
            self._build(nums, 2 * i + 1, l, m) 
            self._build(nums, 2 * i + 2, m + 1, r)
            self.t[i] = self.t[2 * i + 1] + self.t[2 * i + 2]

    def query(self, ql: int, qr: int) -> int:
        def _query(i: int, l: int, r: int) -> int:
            if qr < l or ql > r:
                return 0
            if ql <= l and r <= qr:
                return self.t[i]
            m = (l + r) // 2
            return _query(2 * i + 1, l, m) + _query(2 * i + 2, m + 1, r)
        return _query(0, 0, self.n - 1)

    def update(self, pos: int, delta: int):
        def _update(i: int, l: int, r: int):
            if pos < l or pos > r:
                return
            self.t[i] += delta
            if l != r:
                m = (l + r) // 2
                _update(2 * i + 1, l, m)
                _update(2 * i + 2, m + 1, r)
        _update(0, 0, self.n - 1)

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    print("Sum of range [1, 3]:", st.query(1, 3))
    st.update(1, 3)
    print("After update, sum of range [1, 3]:", st.query(1, 3))
