#Loop FizzBuzz con el número ingresado
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz multiplo de 3 y 5")
    elif i%3==0:
        print("Fizz multiplo de 3")
    elif i%5==0:
        print("Buzz multiplo de 5")
    else:
        print(i, "no es multiplo de 3 o 5")
        
        
        