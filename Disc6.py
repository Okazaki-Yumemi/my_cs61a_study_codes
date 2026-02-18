def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

#next(filter(lambda n: n > 2024, gen_fib()))

def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    prev=next(t)
    for curr in t:
        yield curr-prev
        prev =curr


def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(m)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for p in partition_gen(n-m,m):
            yield p+" + "+str(m)
    if m > 1:
        "*** YOUR CODE HERE ***"
        yield from partition_gen(n,m-1)


# ============================
#  CS61A 生成器（Generator）常用技巧总结
# ============================

# 1. 基本结构：使用 yield 而不是 return
def simple_gen():
    yield 1
    yield 2
    yield 3
# 使用 next 或 for 循环来取值


# 2. 生成器是“惰性”的：只有在 next 时才前进
# next(gen) 会让生成器向前移动一步，不会回头


# 3. 使用一个变量保存“前一个值”
def differences(t):
    prev = next(t)          # 先取第一个
    for curr in t:          # for 会自动 next(t)
        yield curr - prev
        prev = curr         # 更新 prev


# 4. yield from：把另一个生成器的所有值依次 yield 出来
def flatten(gen):
    yield from gen          # 等价于 for x in gen: yield x


# 5. 递归生成器：像 partitions 一样逐层 yield
def partition_gen(n, m):
    if n == m:
        yield str(m)
    if n - m > 0:
        for p in partition_gen(n - m, m):
            yield p + " + " + str(m)
    if m > 1:
        yield from partition_gen(n, m - 1)


# 6. 生成器 vs 列表：生成器不会一次性计算所有结果
# 列表会占用大量内存，而生成器按需生成，非常适合无限序列
def gen_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# 7. filter/map 等高阶函数可以与生成器组合使用
# 例如：找出第一个大于 2024 的斐波那契数
next(filter(lambda x: x > 2024, gen_fib()))


# 8. 生成器表达式（generator expression）
# 类似列表推导式，但用 () 而不是 []
squares = (x * x for x in range(5))
# next(squares) 会依次返回 0, 1, 4, 9, 16


# 9. 生成器不会自动重置
# 如果需要重新遍历，必须重新创建生成器对象
g = gen_fib()
next(g)  # 0
next(g)  # 1
# 想重新从头开始：g = gen_fib()


# 10. 生成器非常适合：
# - 无限序列（fib、自然数、随机数…）
# - 大数据流（逐行读取文件）
# - 树形递归（partitions）
# - 惰性计算（按需生成）
