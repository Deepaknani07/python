def is_prime(number):
    if number>1:
        for num in range(2,number):
            if number%num==0:
                return False
        return True
    return False
print(is_prime(3))
