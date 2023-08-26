def build_cumulative_tree(arr):
    n = len(arr)
    tree = [0] * (n * 2)  
    
    # 맨 아래에 입력값
    for i in range(n):
        tree[n + i] = arr[i]
    
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]
    
    return tree

def print_cumulative_tree(tree, n):
    idx = 1  
    level = 1  
    count = 0  
    
    for i in range(1, n * 2):
        if count == level:  # 현재 레벨에서 출력한 원소의 개수가 레벨과 같으면 줄바꿈
            print()
            level *= 2
            count = 0
        
        print(tree[i], end=' ')
        count += 1
        idx += 1
        if idx > n:  # 출력할 원소의 개수가 입력된 원소의 개수보다 많으면 종료
            break

n = int(input())  
elements = list(map(int, input().split()))  

cumulative_tree = build_cumulative_tree(elements)
print_cumulative_tree(cumulative_tree, n)
