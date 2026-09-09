# To print 'Hello world'
# START
# Show 'Hello world'
# END
print("Hello World", end="\t")
print("Thank you :)")


# To find whether a number is even or odd
# START
# if n%2 is 0
# show even
# else
# show odd
# END
n = 4
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# To find the number of pos, neg and zero
# START
# set pos = 0
# set neg = 0
# set zero = 0
# for each items
#     if item > 0 then increment pos counter by 1
#     if item < 0 then increment neg counter by 1
#     if item = 0 then increment zero by 1
# END
pos, neg, zero = 0, 0, 0
input = [1, 2, 0, -4]
for num in input:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print("Positive: ", pos, "\n", "Negative: ", neg, "\n", "Zeros: ", zero)


# To find the largest among three numbers
# START
# read a, b and c
# if a>b and a>c
#     show a is greater
# if b>a and b>c
#     show b is greater
# else
#     show c is greater
# END
num1 = 12
num2 = 23
num3 = 34
print("Greatest: ", end="")
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)
