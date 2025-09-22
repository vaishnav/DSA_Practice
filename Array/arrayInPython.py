from array import array

# arr = array.array(typecode, initializer)
# typecode → defines the type of elements stored (like C datatypes).
# initializer → an optional list/iterable to initialize the array.


arr = array('i', [10, 20, 30, 40])

arr.append(50)        # Add element at end
arr.insert(1, 15)     # Insert at index
arr.remove(20)        # Remove first occurrence
val = arr.pop()       # Remove and return last item
print(arr[2])         # Access by index
arr[0] = 5            # Modify element


# “In Python, the array module provides a space-efficient sequence of uniform type values, unlike lists which can hold mixed types. 
# Arrays are closer to C-style arrays, storing elements in contiguous memory for better performance. 
# They’re useful when you need type restrictions and memory efficiency, though in practice, NumPy arrays are preferred for heavy numerical computing.”


# “Both Python list and array.array are dynamic arrays that over-allocate memory when resized. 
# They don’t grow one element at a time; instead, CPython uses an amortized growth factor of about 1.125×. 
# This gives O(1) amortized append performance while keeping memory overhead low.”