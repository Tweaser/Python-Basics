Numbers  = [45,-22,77,88,11,5000,77]	#Array of integers
if len(Numbers) == 0:
    print("Array numbers is empty")
else:
    biggest = Numbers[0]            #integer
    smallest = Numbers[0]           #integer
    for x in range(0,len(Numbers)):
        if Numbers[x] > biggest:
            biggest = Numbers[x]
        if Numbers[x] < smallest:
            smallest = Numbers[x]
    print("biggest:",biggest)
    print("smallest:",smallest)