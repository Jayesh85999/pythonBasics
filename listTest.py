basicList = ["jan", "feb", "may", "jan"]
basicList.pop()
basicList.append("june")
basicList.append("july")
basicList.append("aug")

print(basicList)

monthEndList = ["sept", "oct", "nov", "dec"]

basicList.extend(monthEndList)
print(basicList)


def greeting_function(input_name):
    print("Hello:" + input_name + "!!!")


greeting_function("SHYAM")


# def multiplNumber(multiplication_number):
#
# num= input("enter number 1")
#
# num2 = input("enter number 2")
#
#
#      multiplication_number=
#
#     print("number1" +"*"  +"number2" +"=" + a)


def multiplication_number(number1, number2):
    a = number1 * number2
    print("number1" + "*" + "number2" + "=" + str(a))
    return a


print(multiplication_number(4, 6))




numberDictionary = {

    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six"

}



def sample_function(input_number):
    return "Hello!! "+numberDictionary.get(input_number)



print(sample_function(1))


print(greeting_function(sample_function(2)))



def compare_numbers(inputnumber1, inputnumber2, inputnumber3,):
    if(inputnumber1>inputnumber2 and inputnumber1 >inputnumber3):
        print(inputnumber1)

    elif(inputnumber2>inputnumber3 and inputnumber2>inputnumber1):
        print(inputnumber2)

    elif(inputnumber3>inputnumber2 and inputnumber3>inputnumber1):
        print(inputnumber3)


print(compare_numbers(66,5,6))
