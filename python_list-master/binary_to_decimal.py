# num = [1, 0, 0, 1, 1, 0, 1, 1]
# sum=0
# for i in range(len(num)):
#     sum+=num[-i]*(2**i)
#     print(sum)

binary = []
while num != 0:
    bit = num % 2
    binary.insert(0, bit)
    num = num / 2
    print(binary)