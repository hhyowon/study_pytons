# package == module(python)

# 기본 function 구성
def function_name() :
     pass   
     return 0

function_name()
pass

# 평범한 params 이용한 결과값 받기 
def add(first,second):
     sum = first + second
     return sum

result_sum = add(4,6)
pass

# set defualt value with params
def minus(first,second=0):
     result = first - second
     return result

minus(3,5)  # -2 
minus(3)    # 3

# return tuple datatype
def multiply(first,second=1):
     multiply = first * second
     # [multiply,first,second]
     return (multiply,first,second)

result_multiply = multiply(3,4)
multiply,first,second = multiply(4)
result_multiply, resule_first = multiply(4)
pass

