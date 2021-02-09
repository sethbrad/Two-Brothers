"""We import libraries to use functions that the Python team has made for us"""
import array

"""This opens a text file in write mode and declares an array. 
An array is simply a list of values, in this case of integers"""
file = open("file.txt", "w")
arr = array.array('i', [1,2,3,4,5])

"""Now we're going to iterate through the array so each value is written to the file"""
for i in range(0, len(arr)):
    file.write(str(arr[i]) + ".")

print("Success")