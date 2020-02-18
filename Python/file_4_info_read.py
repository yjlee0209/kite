with open('info.txt', 'r', encoding='utf-8') as file:
    # 라인 단위로 읽기
    for line in file:
        #line_info = line.split().split(', ')
        #name = line_info[0]
        #weight = line_info[1]
        #height = line_info[2]
        (name, weight, height) = line.strip().split(', ')

        if not name or not weight or not height:
            continue
            
        #bmi 연산
        bmi = int(weight)/(int(height)*int(height)) *10000

        result = ''
        if bmi >= 25:
            result = '과체중'
        elif bmi >= 18.5:
            result = '정상체중'
        else:
            result = '저체중'

        print('\n이름: {} \n몸무게: {} \n키: {} \nBMI: {} \n결과: {}'.format(name, weight, height, bmi, result))