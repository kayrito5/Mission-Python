for i in range(101):
    message = ""
    if i % 3 == 0:
        message += "Fizz"
    if i % 5 == 0:
        message += "Buzz"
    if message == "":
        message = i
    print(message)