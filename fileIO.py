import array

f = open("file.txt", "w")
arr = array.array('i', [1,2,3,4,5])

for i in range(0, len(arr)):
    f.write(str(arr[i]) + " ")

print("Success")