def build_binary_tree(arr):
    n = len(arr)
    tree = [[0] * n for _ in range(n)]
    
    def build(node, start, end):
        if start == end:
            tree[node][start] = arr[start]
        else:
            mid = (start + end) // 2
            left_node = node * 2
            right_node = node * 2 + 1
            build(left_node, start, mid)
            build(right_node, mid + 1, end)
            for i in range(start, end + 1):
                tree[node][i] = tree[left_node][i] + tree[right_node][i]

    build(1, 0, n - 1)
    return tree

def print_binary_tree(tree, n):
    for i in range(n):
        row = " ".join(str(tree[i][j]) for j in range(n) if tree[i][j] != 0)
        print(row)

n = int(input())
elements = list(map(int, input().split()))

tree = build_binary_tree(elements)

for i in range(n):
    print_binary_tree(tree, n)
