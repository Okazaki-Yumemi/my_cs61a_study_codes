def has_path(t, p):
    """Return whether tree t has a path from the root with labels p.

    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> has_path(t1, [5, 6])        # This path is not from the root of t1
    False
    >>> has_path(t2, [5, 6])        # This path is from the root of t2
    True
    >>> has_path(t1, [3, 5])        # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t1, [3, 5, 6])     # This path goes to a leaf
    True
    >>> has_path(t1, [3, 4, 5, 6])  # There is no path with these labels
    False
    """
    if label(t) != p[0]:
        return False
    if len(p) == 1:
        return True
    for b in branches(t):
        if has_path(b, p[1:]):
            return True
    return False
def find_path(t, x):
    """
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> find_path(t1, 5)
    [3, 5]
    >>> find_path(t1, 4)
    [3, 4]
    >>> find_path(t1, 6)
    [3, 5, 6]
    >>> find_path(t2, 6)
    [5, 6]
    >>> print(find_path(t1, 2))
    None
    """
    if label(t) == x:
        return [x]
    for b in branches(t):
        path = find_path(b, x)
        if path is not None:
            return [label(t)] + path
    return None

"""树状递归模板——查找类"""
def fn(t):
    # 1. 处理当前节点
    if base_case:
        return True or False

    # 2. 对每个分支递归
    for b in branches(t):
        if fn(b):
            return True

    # 3. 所有分支都不满足
    return False
"""树状递归模板——路径,列表类"""
def fn(t):
    # 1. 当前节点命中
    if label(t) == target:
        return [label(t)]

    # 2. 递归到分支
    for b in branches(t):
        path = fn(b)
        if path is not None:
            return [label(t)] + path

    # 3. 找不到
    return None
"""树状递归模板——累加类"""
def fn(t):
    total = process(label(t))  # 当前节点贡献

    for b in branches(t):
        total += fn(b)

    return total
"""树状递归模板——构造新树类"""
def fn(t):
    new_label = process(label(t))
    new_branches = [fn(b) for b in branches(t)]
    return tree(new_label, new_branches)
