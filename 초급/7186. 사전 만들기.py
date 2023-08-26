N = int(input())

words = []

for _ in range(N):
    word = input().strip()
    words.append(word)

# 길이가 짧은 단어부터, 길이가 같다면 사전순으로 정렬
sorted_words = sorted(words, key=lambda x: (len(x), x))

# 중복을 제거한 단어들을 출력
unique_words = []
for word in sorted_words:
    if word not in unique_words:
        print(word)
        unique_words.append(word)
