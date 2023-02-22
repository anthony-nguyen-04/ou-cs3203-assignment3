def addList(list):
    sum = 0
    for element in list:
        sum = sum + element

    return sum

def multiplyList(list):
    product = 1
    for element in list:
        product = product * element

    return product

def reverseList(list):
    return list[::-1]

def main():
    input_numbers = input("Input your numbers on one line\n")
    string_array = input_numbers.strip().split(" ")

    numbers = [int(number_string) for number_string in string_array]

    print("Sum is: " + str(addList(numbers)))
    print("Product is: " + str(multiplyList(numbers)))
    print("Reversed List is: " + str(reverseList(numbers)))

if __name__ == "__main__":
    main()