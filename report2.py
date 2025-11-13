# 관계행렬 기반 동치관계 판정 및 폐포 생성 프로그램
# 집합 A = {1,2,3,4,5}

A = [1, 2, 3, 4, 5]
N = 5

# ------------------------------
# 추가 기능: True/False → 참/거짓 변환
# ------------------------------
def tf_to_kor(val):
    return "참" if val else "거짓"

# ------------------------------
# 1. 관계행렬 입력
# ------------------------------
def read_matrix():
    print("5×5 관계행렬을 입력하세요 (0 또는 1):")
    R = []
    for i in range(N):
        row = list(map(int, input(f"{i+1}행: ").split()))
        if len(row) != N:
            raise ValueError("각 행에는 반드시 5개의 값이 있어야 합니다.")
        R.append(row)
    return R

# ------------------------------
# 2. 반사 / 대칭 / 추이 판정
# ------------------------------
def is_reflexive(R):
    return all(R[i][i] == 1 for i in range(N))

def is_symmetric(R):
    return all(R[i][j] == R[j][i] for i in range(N) for j in range(N))

def is_transitive(R):
    return all(
        not (R[i][j] and R[j][k]) or R[i][k]
        for i in range(N) for j in range(N) for k in range(N)
    )

# ------------------------------
# 3. 동치류 계산
# ------------------------------
def equivalence_class(R, x):
    idx = x - 1
    return [A[j] for j in range(N) if R[idx][j] == 1]

# ------------------------------
# 추가 기능 2: 동치류를 분할 구조로 변환하여 출력
# ------------------------------
def equivalence_partition(R):
    visited = set()
    parts = []
    for x in A:
        if x not in visited:
            eq = equivalence_class(R, x)
            parts.append(eq)
            visited.update(eq)
    return parts

# ------------------------------
# 4. 폐포 생성 (Reflexive / Symmetric / Transitive)
# ------------------------------
def reflexive_closure(R):
    R2 = [row[:] for row in R]
    for i in range(N):
        R2[i][i] = 1
    return R2

def symmetric_closure(R):
    R2 = [row[:] for row in R]
    for i in range(N):
        for j in range(N):
            if R[i][j] == 1:
                R2[j][i] = 1
    return R2

def transitive_closure(R):
    R2 = [row[:] for row in R]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if R2[i][k] and R2[k][j]:
                    R2[i][j] = 1
    return R2

# ------------------------------
# 행렬 출력
# ------------------------------
def print_matrix(R):
    for row in R:
        print(" ".join(map(str, row)))
    print()

# ------------------------------
# 메인 실행
# ------------------------------
def main():
    R = read_matrix()

    print("\n[입력된 관계 행렬]")
    print_matrix(R)

    # 관계 판정
    refl = is_reflexive(R)
    symm = is_symmetric(R)
    trans = is_transitive(R)

    print(f"반사적: {tf_to_kor(refl)}")
    print(f"대칭적: {tf_to_kor(symm)}")
    print(f"추이적: {tf_to_kor(trans)}")

    # 동치 여부
    if refl and symm and trans:
        print("\n→ 이 관계는 동치 관계입니다.\n")
        print("[동치류]")
        for x in A:
            print(f"E({x}) = {equivalence_class(R, x)}")

        # 추가 기능: 동치류 분할 형태 출력
        print("\n[동치류 분할(partition) 출력 - 추가 기능]")
        parts = equivalence_partition(R)
        print(parts)

    else:
        print("\n→ 이 관계는 동치 관계가 아닙니다.\n")

    print("\n[폐포 생성 결과]\n")

    # 반사 폐포
    R_refl = reflexive_closure(R)
    print("[반사 폐포]")
    print_matrix(R_refl)

    # 대칭 폐포
    R_symm = symmetric_closure(R)
    print("[대칭 폐포]")
    print_matrix(R_symm)

    # 추이 폐포
    R_trans = transitive_closure(R)
    print("[추이 폐포]")
    print_matrix(R_trans)

    # 최종 관계 (반사 + 대칭 + 추이)
    R_final = transitive_closure(symmetric_closure(reflexive_closure(R)))

    print("[최종 폐포 적용 후 관계]")
    print_matrix(R_final)

    # 최종 판정
    refl2 = is_reflexive(R_final)
    symm2 = is_symmetric(R_final)
    trans2 = is_transitive(R_final)

    print(f"반사적: {tf_to_kor(refl2)}")
    print(f"대칭적: {tf_to_kor(symm2)}")
    print(f"추이적: {tf_to_kor(trans2)}")

    if refl2 and symm2 and trans2:
        print("→ 폐포 적용 후: 동치 관계입니다.\n")
        print("[동치류]")
        for x in A:
            print(f"E({x}) = {equivalence_class(R_final, x)}")

        print("\n[최종 동치류 분할(partition) - 추가 기능]")
        print(equivalence_partition(R_final))

    else:
        print("→ 폐포 적용 후에도 동치 관계가 아님.")


main()


