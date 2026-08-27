def solution(name):
    Len = len(name)
    nameList = [name[i] for i in range(Len)]
    nameField = ['A' for i in range(Len)]
    answer = 0
    
    # 정방향
    for i in range(Len):
        a = ord(nameField[i])
        b = ord(nameList[i])
        if b-a <= 13 :            # 절반 이하면 그냥 더하고
            answer += b-a
        else :                    # 절반 넘으면 26에서 빼기
            answer += 26 - (b-a)
        
        nameField[i] = nameList[i] # name "A"가 들어간게 있을수도 있으니
        if nameField == nameList : # 값 바꿔주고 전체 체크!!
            break

        answer +=1                 # 이동가중치 ++
    dap = answer
    
    # 정방향 + 역방향
    t = (int)(Len/2)
    for i in range(t):             # 0~전체길이/2
        nameField = ['A' for i in range(Len)]
        answer = i
        
        for j in range(i+1):       #정방향
            a = ord(nameField[j])
            b = ord(nameList[j])
            if b-a <= 13 :
                answer += b-a
            else :
                answer += 26 - (b-a)

            nameField[j] = nameList[j]
            if nameField == nameList :
                break

            answer +=1
        

        for j in range(Len-1,i,-1): #역방향
            a = ord(nameField[j])
            b = ord(nameList[j])
            if b-a <= 13 :
                answer += b-a
            else :
                answer += 26 - (b-a)

            nameField[j] = nameList[j]
            if nameField == nameList :
                break

            answer +=1
        
        dap = min(dap,answer)
        
    return dap


'''
중복코드로 많아 함수로 빼고싶었지만..패쓰!

정방향의 가중치와
정방향으로 0~길이/2 만큼까지 가고 + 역방향 가면서
원하는 name만들어졌는지 계속 체크!

최소가중치를 구해서 출력!!
'''