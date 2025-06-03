def Calculate_average(numbers): 
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        print("input harus berupa angka desimal")
 
result = Calculate_average([5,7,7,8])
print(result)
