from typing import List

class PrefixMaxSegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.t = [0] * (4 * self.n)
        self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums: List[int], i: int, l: int, r: int):
        if l == r:
            self.t[i] = nums[l]
        else:
            m = (l + r) // 2
            self._build(nums, 2 * i + 1, l, m)
            self._build(nums, 2 * i + 2, m + 1, r)
            self.t[i] = max(self.t[2 * i + 1], self.t[2 * i + 2])

    def query(self, ql: int, qr: int) -> int:
        def _query(i: int, l: int, r: int) -> int:
            if qr < l or ql > r:
                return float('-inf')
            if ql <= l and r <= qr:
                return self.t[i]
            m = (l + r) // 2
            return max(_query(2 * i + 1, l, m), _query(2 * i + 2, m + 1, r))
        return _query(0, 0, self.n - 1)

    def update(self, pos: int, val: int) -> None:
        def _update(i: int, l: int, r: int) -> None:
            if pos < l or pos > r:
                return
            if l == r:
                self.t[i] = val
            else:
                m = (l + r) // 2
                _update(2 * i + 1, l, m)
                _update(2 * i + 2, m + 1, r)
                self.t[i] = max(self.t[2 * i + 1], self.t[2 * i + 2])
        _update(0, 0, self.n - 1)

if __name__ == '__main__':
    arr = [2, 5, 1, 4, 9, 3]
    st = PrefixMaxSegmentTree(arr)
    print("Max in range [1, 4]:", st.query(1, 4))
    st.update(3, 10)
    print("After update, max in range [1, 4]:", st.query(1, 4))
