class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.data)


# Example usage:
arr = Array(5)  # Creating an array of size 5
print("Array length:", len(arr))

# Setting values
arr[0] = 1
arr[1] = 2
arr[2] = 3
arr[3] = 4
arr[4] = 5

print("Array:", arr)

# Getting values
print("Element at index 2:", arr[2])
