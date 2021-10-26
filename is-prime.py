n = int(input("Enter a number to check if its prime: "))


def prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


print("")
print(prime(n))
