def sub(n, m):
    if m == 0:
        return n
    else:
        return sub(n, m - 1) - 1


print(sub(5, 2))


def mult(n,m):
    if m == 0:
        return 0
    else:
        return n + mult(n, m - 1)

print(mult(2, 8), " <----- mult")


def are_eq(m,n):
    if n == 0 and m == 0:
        return True

    elif (n == 0 and m != 0) or (n != 0 and m == 0):
        return False

    else:
        return are_eq(n - 1, m - 1)


print(are_eq(3,3))


def div(n,m):
    if n < m:
        return 0

    return 1 + div(n - m, m)

print(div(10, 3))


def rem(n, m):
    if n < m:
        return n
    else:
        return div(n - m, m) - 1

print(rem(10, 5), " <------ rem")


def is_leq(n, m):
    if n  == 0:
        return True
    elif m == 0:
        return False
    else:
        return is_leq(n-1, m-1)

print (is_leq(3, 5))


def is_less(n, m):
    return is_leq(n, m) and not is_leq(m, n)

print(is_less(3, 4), " <------ is_less")

# def power(n, m):
#     if m == 0:
#         return 1
#     elif rem(n, m) == 0:
#         return mult(power(n, div(m, 2)), power(n, div(m, 2)))
#     else:
#         return mult(n, power(n, m - 1))
#
# print(power(2, 4))

def power(n, m):
    if m == 0:
        return 1
    elif n == 0 and m == 0:
        return None
    else:
        return n * power(n, m - 1)

print(power(0, 0), " <-------- power")

def get_factorial(n):
    if n == 0:
        return 1
    else:
        return mult(n, get_factorial(n - 1))

print(get_factorial(5), " <------- fact!")

#cela cast druhe odmopcniny cisla

def sqrt(n):
    if n == 0 or n == 1:
        return n
    else:
        x = sqrt(n // 4) * 2
        if (x + 1) * (x + 1) <= n:
            return x + 1
        else:
            return x
print(sqrt(17), " <----- sqrt")


def get_gcd(n, m):
    if m == 0:
        return n
    else:
        return get_gcd(m, n % m)

print(get_gcd(12, 8), " <------- GCD")