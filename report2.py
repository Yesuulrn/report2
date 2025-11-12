# Report 2 - 동치 관계 판별 프로그램
# 작성자: 예슐렌(20233571)

# 1. 관계행렬 입력받기
n = 5
relation = []
print("5x5 관계행렬의 각 행을 입력하세요 (0과 1로 구분, 공백으로 띄우기):")
for i in range(n):
    row = list(map(int, input(f"{i+1}번째 행: ").split()))
    relation.append(row)

# 2. 반사성(Reflexive) 검사
def is_reflexive(mat):
    for i in range(n):
        if mat[i][i] != 1:
            return False
    return True

# 3. 대칭성(Symmetric) 검사
def is_symmetric(mat):
    for i in range(n):
        for j in range(n):
            if mat[i][j] != mat[j][i]:
                return False
    return True

# 4. 추이성(Transitive) 검사
def is_transitive(mat):
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                for k in range(n):
                    if mat[j][k] == 1 and mat[i][k] == 0:
                        return False
    return True

# 5. 판별 및 출력
ref = is_reflexive(relation)
sym = is_symmetric(relation)
tra = is_transitive(relation)

print("\n출력 결과:")
print(f"반사성 : {'있음' if ref else '없음'}")
print(f"대칭성 : {'있음' if sym else '없음'}")
print(f"추이성 : {'있음' if tra else '없음'}")

if ref and sym and tra:
    print("\n 이 관계는 동치 관계입니다!")
else:
    print("\n동치 관계가 아닙니다.")
1

