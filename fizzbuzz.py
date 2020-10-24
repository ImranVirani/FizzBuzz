counter = 1
maxNum = 100
while (counter <= 100):
    if ((counter % 15) == 0):
        print("FizzBuzz")
    elif ((counter % 5) == 0):
        print("Buzz")
    elif ((counter % 3) == 0):
        print("Fizz")
    else:
        print(counter)
    counter+=1
