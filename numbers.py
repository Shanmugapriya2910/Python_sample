def numbers(start, end):

    even= []
    odd = []
    prime = []

    def is_prime(num):

        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    for num in range(start, end + 1):
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

        if is_prime(num):
            prime.append(num)



    return {
        "even": even,
        "odd": odd,
        "prime": prime
    }

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(numbers(start, end))
result = numbers(start, end)


with open("numbers.txt", "w") as file:
    file.write("Even Numbers: " + str(result["even"]) )
    file.write("Odd Numbers: " + str(result["odd"]))
    file.write("Prime Numbers: " + str(result["prime"]) )

