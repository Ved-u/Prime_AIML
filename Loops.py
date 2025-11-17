lambda a,b : a+b

def factorial(n):
    ans = 1
    while n>0:
        ans *= n
        n-=1
    return ans

def vowel(word):
    vowel = 0
    for char in word:
        if(char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'
        or char == 'a' or char == 'e' or char == 'i'or char == 'o' or char == 'u'):
            vowel += 1
    return vowel

def rangeEven(a,b):
    for i in range(a,b+1):
        if(i%2==0):
            print(i)

def digits(n):
    n = int(n)
    count = 0
    while(n>0):
        count+=n%10
        n//=10 #Integer division
    return count

def user_in():
    while True:
        _input = input("Enter number: or Quit:")
        if(_input == "Quit"):
            break
        else:
            _input = int (_input)
        print("even" if(_input%2==0 )else "odd" )

def calc(_num1, _num2, operation):
    match operation:
        case '+':
            print(_num1+_num2)
        case '-':
            print(_num1-_num2)
        case '*':
            print(_num1*_num2)
        case '/':
            print(_num1/_num2)
        case _:
            print("Invalid operation")
        
def isPrime(n):
    n = int(n)
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def Prime_range(n):
    n = int(n)
    for i in range(n+1):
        if(isPrime(i)):
            print(i)

# print(vowel("Apna College Prime AIML Batch"))
# print(factorial(5))
# print(rangeEven(1,10))
# print(digits(123456789))
# user_in()
# _num1 = float(input("Enter 1st num:"))
# _num2 = float(input("Enter 2nd num:"))
# operation = input("Enter the operation:")
# calc(_num1,_num2,operation)

Prime_range(100)