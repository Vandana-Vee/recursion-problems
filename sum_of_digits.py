
n = 123451
def digits(n):
    if n//10==0:
        return n
    return n%10 + digits(n//10)

print(digits(n))