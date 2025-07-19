# Calculation: If input = 4

# 1³ + 2³ + 3³ + 4³
# = 1 + 8 + 27 + 64
# = 100

n = int(input("Enter a Number: "))

i = 1
sum = 0 
while(i<=n):
     sum = sum + i**3
     i = i+1
print(sum)
    