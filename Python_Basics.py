import math

# ass-1
user_name = input("Enter User Name:")
user_age = input("Enter Age:")
print("Hello", user_name, "you are" , user_age ,"years old!")

# ass-2
num_1 = float(input("Enter 1st num:"))
num_2 = float(input("Enter 2nd num:"))
print("sum:",num_1+num_2)
print("diff:",num_1-num_2)
print("mul:",num_1*num_2)
print("quotient:",num_1/num_2)

# ass-3
_int = float(input("Enter 1st int:"))
_int_2 = float(input("Enter 1st int:"))
_float = float(input("Enter float:"))
print("avg:",(_int+_int_2+_float)/3)
print("type:",type(_int+_int_2+_float))

# ass-4
input = input("Enter num String:")
_int = int(input)
_float = float(input)
print(_int,type(_int))
print(_float,type(_float))
print(input,type(input))

# ass-5 
print("answer 22, because BODMAS")

# ass-6
num_1 = int(input("Enter 1st num:"))
num_2 = int(input("Enter 2nd num:"))
# 3rd cariable
temp = num_1
num_1 = num_2
num_2 = temp
print(num_1)
print(num_2)
# without 3rd (XOR)
num_1 = num_1 ^ num_2
num_2 = num_1 ^ num_2
num_1 = num_1 ^ num_2
print(num_1)
print(num_2)
# arthmatic
num_1 = num_1 + num_2
num_2 = num_1 - num_2
num_1 = num_1 - num_2
print(num_1)
print(num_2)

# Ass-7
_celcius = float(input("Enter 1st int:"))
_farenheight = _celcius*9/5 + 32
print("farenhirt", _farenheight)

# Ass-8
_radius = float(input("Radius:"))
PI = 3.142
print("Area:",PI*_radius**2)

# Ass-9
_principle = float(input("principle:"))
_ROT = float(input("ROT:"))
_Time = float(input("Time:"))
print("Simple Interest:",_principle*_ROT*_Time/100)

# Ass-10
_num = float(input("Num:"))
_dec = math.floor(_num)
_fraction = _num - _dec
_fraction = round(_fraction, 2)
print("Integer part",_dec)
print("Fraction part",_fraction)