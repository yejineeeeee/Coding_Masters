from itertools import combinations

def calculate_difference(ingredients, combination):
    total_score = 0
    for i in range(len(combination)):
        for j in range(i+1, len(combination)):
            total_score += ingredients[combination[i]][combination[j]] + ingredients[combination[j]][combination[i]]
    return total_score

def minimize_nutrition_difference(N, ingredients):
    min_difference = float('inf')
    
    # 모든 식재료의 조합을 생성
    all_ingredients = list(range(N))
    half_N = N // 2
    
    for combination in combinations(all_ingredients, half_N):
        rest = set(all_ingredients) - set(combination)
        rest_combination = tuple(rest)
        
        # 영양 점수 계산
        score1 = calculate_difference(ingredients, combination)
        score2 = calculate_difference(ingredients, rest_combination)
        
        # 최소 차이 갱신
        min_difference = min(min_difference, abs(score1 - score2))
    
    return min_difference

# 입력 받기
N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = minimize_nutrition_difference(N, ingredients)
print(result)
