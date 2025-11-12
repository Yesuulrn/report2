# Report 2 - 5x5 숫자를 입력받아 정렬 및 통계 출력 프로그램
# 작성자: (여기에 이름 작성)

# 1. 사용자로부터 5x5 숫자 입력 받기
arr = []  # 숫자를 저장할 리스트
print("5x5 행렬의 25개 숫자를 입력하세요:")

for i in range(5):
    row = list(map(int, input(f"{i+1}번째 줄 (숫자 5개): ").split()))
    while len(row) != 5:
        print("⚠️ 숫자 5개를 입력해야 합니다!")
        row = list(map(int, input(f"{i+1}번째 줄을 다시 입력하세요: ").split()))
    arr.append(row)

# 2. 2차원 배열을 1차원으로 바꾼 뒤 정렬하기
flat = [num for sub in arr for num in sub]
sorted_list = sorted(flat)

# 3. 통계값 계산하기
max_val = max(sorted_list)
min_val = min(sorted_list)
avg_val = sum(sorted_list) / len(sorted_list)
median_val = sorted_list[len(sorted_list)//2]

# 4. 결과 출력하기
print("\n입력한 행렬:")
for row in arr:
    print(row)

print("\n정렬된 리스트:")
print(sorted_list)

print("\n📊 통계 결과:")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"평균: {avg_val:.2f}")
print(f"중앙값: {median_val}")
