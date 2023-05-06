size = int(input("enter the size of series: "))
numbers = []
print("enter the numbers: ")
for i in range(size):
    numbers.append(int(input()))
even_count = 0
odd_count = 0

for i in range(len(numbers)):
    if(numbers[i]%2==0):
        even_count = even_count+1
    else:
        odd_count = odd_count+1
        
print("number of even numbers",even_count)
print("number of odd numbers",odd_count)