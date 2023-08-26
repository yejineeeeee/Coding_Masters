def build_cumulative_tree(arr):
    tree = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        idx = i + 1
        tree[idx] = arr[i]
        while idx > 1:
            idx //= 2
            tree[idx] += tree[i + 1]

    return tree

def print_cumulative_tree(tree, N):
    power_of_2 = 1
    idx = 1

    while idx < len(tree):
        for _ in range(power_of_2):
            if idx <= N:
                print(tree[idx], end=' ')
                idx += 1
            else:
                break
        print()
        power_of_2 *= 2


N = int(input())

elements = list(map(int, input().split()))


cumulative_tree = build_cumulative_tree(elements)


print_cumulative_tree(cumulative_tree, N)
