import numpy as np

arr = np.array([])


while len(arr) < 5:
    number = int(input("Enter a number: "))
    arr = np.append(arr, number)

print(f"The mean of the entered numbers is : {round(np.mean(arr),2)}.")
print(f"The variance of the entered numbers is : {round(np.var(arr),2)}")
print(f"The median of the entered numbers is : {np.median(sorted(arr))}")
print(f"The standard deviation of the entered numbers is : {round(np.std(arr),2)}")

arr_even = arr[arr%2 == 0]

arr_odd = arr[arr%2 != 0]

print(f"Even numbers : {arr_even}")
print(f"Odd numbers : {arr_odd}")

prime_arr = []

for number in arr:
    num = int(number)
    if num > 1:
        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            prime_arr.append(num)

print(f"Prime numbers: {prime_arr}")
