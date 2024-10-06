import time
try:
    num1=int(input("nım1:"))
    num2=int(input("nım2:"))

    sum=num1+num2

    print(sum)
except ValueError:
    print("Error: Division by zero is not allowed")


finally:
    counter = 5

    for i in range(5):
        time.sleep(1)
        print("countdown:", counter)
        counter-=1
        if counter ==0:
            print("Blast off!")