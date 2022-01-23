# 参考: https://qiita.com/Kota-Y/items/396ab3c57830dad65cfb#5-%E6%8C%81%E3%81%A3%E3%81%A6%E3%82%8B%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA

from functools import reduce
from math import gcd


# 複数の数の最大公約数
def gcd_list(num_list: list) -> int:
    return reduce(gcd, num_list)


# 複数の数の最小公倍数
def lcm_base(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)


def lcm_list(num_list: list):
    return reduce(lcm_base, num_list, 1)


# 約数列挙
def make_divisors(n: int) -> list:
    return_list = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return_list.append(i)
            if i != n // i:
                return_list.append(n // i)

    return return_list


# 素因数分解
def prime_factorize(n: int) -> list:
    return_list = []
    while n % 2 == 0:
        return_list.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return_list.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        return_list.append(n)
    return return_list


# MOD用組み合わせ
def mod_cmb(n: int, k: int, p: int) -> int:
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    if (k > n - k):
        return mod_cmb(n, n - k, p)
    c = d = 1
    for i in range(k):
        c *= (n - i)
        d *= (k - i)
        c %= p
        d %= p
    return c * pow(d, p - 2, p) % p


# Union-Find木
class UnionFind:
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1] * (n + 1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rank = [0] * (n + 1)

    # ノードxのrootノードを見つける
    def find_root(self, x):
        if self.root[x] < 0:  # 根
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    # 木の併合、入力は併合したい各ノード
    def unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.find_root(x)
        y = self.find_root(y)
        # すでに同じ木に属していた場合
        if x == y:
            return
        # 違う木に属していた場合rankを見てくっつける方を決める
        if self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    # xとyが同じグループに属するか判断
    def is_some_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    # ノードxが属する木のサイズを返す
    def count(self, x):
        return -self.root[self.find_root(x)]
