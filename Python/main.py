#import module_basic.test_module as test
from module_basic.test import test_module as test

r = test.number_input()
print('원의 둘레 값은 :', test.get_circumference(r))
print('원의 면적 값은 :', test.get_circle_area(r))



# print(test.__package__)
# print(test.__name__)
# print(test.__doc__)
# print(test.__file__)