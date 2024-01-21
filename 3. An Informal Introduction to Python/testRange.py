# x = range(0,8)
#
# for i in x:
#     print(i)
#
#
#
# words = ['cat', 'window', 'dog']
#
#
# for w in words:
#     print(w)
#
#
# for i in range(0, len(words)):
#     print(i, words[i])
#
# for i in range(0, 21):
#     if i % 2 == 1:
#         print('odd numbers::', i)
#


def printsEvenOrOdd(input):
    # print('this is even number!!')

    if input % 2 == 0:
        print("number is even")

    elif input % 2 == 1:
        print("number is odd")

    # else print("number is odd")


printsEvenOrOdd(19)
# printsEvenOrOdd(13)

status = 700

match status:
    case 400:
        print('this is http code 400')
    case 500:
        print('this is http code 500')
    case _:
        print('everything else!!')


def calculator(x, y, opr):
    ans = 0
    match opr:
        case "+":
            ans = x + y
        case "*":
            ans = x * y
        case "-":
            ans = x - y
        case "/":
            ans = x / y

    print('the answer of x, y, opr::', ans)
    return ans



a = calculator(12, 13, '*')

print(a)
