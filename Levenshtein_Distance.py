import numpy as np

# 레벤슈타인 거리 구하기
def calc_distance(a, c):
    ''' 레벤슈타인 거리 계산하기 '''
    calc_leven = [] #레벤슈타인 값을 저장하는 배열 초기화
    for i in range(0,len(c)):#question 배열의 사이즈 만큼 for문돌기
        b = c[i]
        if a == b: return 0 # 같으면 0을 반환
        a_len = len(a) # a 길이
        b_len = len(b) # b 길이
        if a == "":  
            b_len
            continue #b의 길이 만큼 값을 추가 하고 continue로 다음 문장 검사
        if b == "": 
            calc_leven.append(a_len) #a의 길이 만큼 추가하고 continue로 다음 문장검사
            continue
        matrix = [[] for i in range(a_len+1)] # 리스트 컴프리헨션을 사용하여 1차원 초기화
        for i in range(a_len+1): # 0으로 초기화
            matrix[i] = [0 for j in range(b_len+1)]  # 리스트 컴프리헨션을 사용하여 2차원 초기화
        # 0일 때 초깃값을 설정
        for i in range(a_len+1):
            matrix[i][0] = i
        for j in range(b_len+1):
            matrix[0][j] = j
        # 표 채우기 --- (※2)
        # print(matrix,'----------')
        for i in range(1, a_len+1):
            ac = a[i-1]
            # print(ac,'=============')
            for j in range(1, b_len+1):
                bc = b[j-1] 
                # print(bc)
                cost = 0 if (ac == bc) else 1  #  파이썬 조건 표현식 예:) result = value1 if condition else value2
                matrix[i][j] = min([
                    matrix[i-1][j] + 1,     # 문자 제거: 위쪽에서 +1
                    matrix[i][j-1] + 1,     # 문자 삽입: 왼쪽 수에서 +1   
                    matrix[i-1][j-1] + cost # 문자 변경: 대각선에서 +1, 문자가 동일하면 대각선 숫자 복사
                ])
                # print(matrix)
            # print(matrix,'----------끝')'
        calc_leven.append(matrix[a_len][b_len]) #레벤슈타인값을 담은 배열에 값 추가
    
    print(calc_leven)
    return calc_leven

