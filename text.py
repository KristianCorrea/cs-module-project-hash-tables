arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
total = 0
for inner_arr in arr: #inner arrays in the array.
    minimum = inner_arr[0] #Capture first number and set as minimum
    for number in inner_arr: #Compare every number in the inner array to minimum. If less than current minimum then new minimum.
        if number < minimum:
            minimum = number
    total = total + minimum # Add minimum to current total.

print(total)