# n = 123
#
# res = 0
#
# while n >= 1:
#     res += n % 10
#     n = n // 10
#
# print(f"n = {n} -> res = {res}")

# n = int(60)
# p = int(n / 6)
# print(f"{p} {p * 4} {p}")
#
# n = 123456
# left = 0
# right = 0
#
# while n >= 1000:
#     right += n % 10
#     n = n // 10
# else:
#     while n >= 1:
#         left += n % 10
#         n = n // 10
#
# if left == right:
#     print("yes")
# else:
#     print("no")

# Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# Выведите yes или no соответственно.

# c дб кратно a или b

a = 2
b = 3
c = 5
if c % a == 0 or c % b == 0:
    print("yes")
else:
    print("no")
