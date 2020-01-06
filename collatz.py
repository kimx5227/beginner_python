def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2)
    else:
        print(3 * number + 1)
        return(3 * number + 1)
while True:
        try:
            user_int = int(input('Choose an Integer: '))
            break
        except:
            print('Print a integer')
if user_int !=0:
    while user_int != 1:
        user_int = collatz(user_int)
else:
    print("0 goes on for infinity")
