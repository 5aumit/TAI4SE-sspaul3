# https://www.acmicpc.net/problem/20540

# 각 지표의 반대되는 지표를 저장한 dictionary
MBTI_reverse_index = {
    'E': 'I',
    'I': 'E',
    'S': 'N',
    'N': 'S',
    'T': 'F',
    'F': 'T',
    'J': 'P',
    'P': 'J'
}

# 연길이의 MBTI 4글자를 대문자로 입력
yeongil_MBTI = input()

# 연길이 MBTI의 각 지표에 반대되는 지표를 출력
for i in yeongil_MBTI:
    print(MBTI_reverse_index[i], end='')