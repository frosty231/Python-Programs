
myList=list(map(int, input("enter values separated by spaces").split(" ")))
print("original list: ",myList)
myList=list(set(myList))
t=tuple(myList)
print("tuple ",t)
print("unique list",myList)
print("maximum value is ", max(myList))
print("minimum value is ", min(myList))
myList.sort(reverse=True)
print("ascending orer ",myList)