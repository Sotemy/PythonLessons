def myfun(z):
    result = []
    i=0
    while i < z:
        print(f"в начале i = {i}")
        result.append(i)
        
        i += 1
        print("текущие значения: ", result)
        print(f"в конце i = {i}")
    return result

numbers = myfun(6)

print("Значения: ")

for num in numbers:
    print(num)