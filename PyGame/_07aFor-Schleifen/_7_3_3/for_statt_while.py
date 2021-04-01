x = int(input("Eine Zahl bitte! "))

# Original while-Schleife
# i = 1
# while i <= 1000:
#     if i % x == 0:
#         print(i)
#     i += 1

# Umgewandelte for-Schleife
for i in range(1, 1001):
    if i % x == 0:
        print(i)
