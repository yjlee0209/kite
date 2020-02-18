# random module 사용
import random as r
from math import floor as f

print('# random module 사용')

# random() : 0.0 <= num < 1.0 float 테이터를 반환
print('random.random() :', r.random(), '/', f(r.random()))

# uniform(a,b) : a에서 b 범위의 float 데이터를 반환
print('random.uniform(10,20) :', r.uniform(10,20), '/', f(r.uniform(10,20)))

# randrange(a) : 0~a-1 범위의 정수형 데이터를 반환
# randrange(a,b) : a~b 범위의 정수형 데이터를 반환
print('random.randrange(10) :', r.randrange(10))
print('random.randrange(10,20) :', r.randrange(10,20))

member_num = [0,1,2,3,4,5,6,7,8,9]
print('random.choidc(memeber_num) :', r.choice(member_num))
r.shuffle(member_num)
print('random.shuffle(mamber_num) :', member_num)

# sample(seq or list, k=개수) : 리스트중 개수만큼 추철해서 리스트로반환
print(r.sample(member_num, k=2))