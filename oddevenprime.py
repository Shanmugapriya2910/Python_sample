import unittest
import math

def numbers(start, end):
    even = []
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

if __name__ == "__main__":

    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    result = numbers(start, end)
    print(result)

    with open("numbers.txt", "w") as file:
        file.write("Even Numbers: " + str(result["even"]) + "\n")
        file.write("Odd Numbers: " + str(result["odd"]) + "\n")
        file.write("Prime Numbers: " + str(result["prime"]) + "\n")

# Unit Tests
class TestNumbers(unittest.TestCase):
    def test_even_numbers(self):
        result = numbers(1, 10)
        self.assertEqual(result["even"], [2, 4, 6, 8, 10])

    def test_odd_numbers(self):
        result = numbers(1, 10)
        self.assertEqual(result["odd"], [1, 3, 5, 7, 9])

    def test_prime_numbers(self):
        result = numbers(1, 10)
        self.assertEqual(result["prime"], [2, 3, 5, 7])

if __name__ == "__main__":
    unittest.main()
