def super_fizz_buzz(n):

    F = "Fizz"
    B = "Buzz"
    if(n % 9 == 0 and n % 25 ==0):
        return F+F+B+B
    elif(n % 3 == 0 and n % 5 ==0):
        return F+B
    elif(n % 25 == 0):
        return B+B
    elif(n % 9 == 0):
        return F+F
    elif(n % 5 == 0):
        return B
    elif(n % 3 == 0):
        return F
    else:
        return "NoFizzBuzz"
