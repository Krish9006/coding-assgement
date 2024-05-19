class DynamicArray:
    def __init__(self, resize_factor=2):
        self.array = []
        self.resize_factor = resize_factor

    def insert_at_index(self, index, value):
        self.array.insert(index, value)

    def delete_at_index(self, index):
        if 0 <= index < len(self.array):
            self.array.pop(index)
        else:
            raise IndexError("Index out of bounds")

    def size(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def rotate_right(self, k):
        n = len(self.array)
        if n == 0:
            return
        k %= n
        self.array = self.array[-k:] + self.array[:-k]

    def reverse(self):
        self.array.reverse()

    def append(self, value):
        self.array.append(value)

    def prepend(self, value):
        self.array.insert(0, value)

    def merge(self, other):
        self.array.extend(other.array)

    def interleave(self, other):
        merged_array = []
        len_self = len(self.array)
        len_other = len(other.array)
        min_length = min(len_self, len_other)
        
        for i in range(min_length):
            merged_array.append(self.array[i])
            merged_array.append(other.array[i])

        merged_array.extend(self.array[min_length:])
        merged_array.extend(other.array[min_length:])
        self.array = merged_array

    def find_middle(self):
        if not self.array:
            return None
        mid_index = len(self.array) // 2
        return self.array[mid_index]

    def index_of(self, value):
        try:
            return self.array.index(value)
        except ValueError:
            return -1

    def split_at_index(self, index):
        if not (0 <= index <= len(self.array)):
            raise IndexError("Index out of bounds")
        first_half = DynamicArray(self.resize_factor)
        second_half = DynamicArray(self.resize_factor)
        first_half.array = self.array[:index]
        second_half.array = self.array[index:]
        return first_half, second_half

    def resize(self, new_size):
        if new_size < len(self.array):
            raise ValueError("New size must be greater than current size")
        self.array.extend([None] * (new_size - len(self.array)))

    def __str__(self):
        return str(self.array)

# Example usage
if __name__ == "__main__":
    da = DynamicArray()
    da.append(1)
    da.append(2)
    da.append(3)
    print("Original array:", da)

    da.insert_at_index(1, 4)
    print("After insert:", da)

    da.delete_at_index(2)
    print("After delete:", da)

    print("Size:", da.size())
    print("Is empty:", da.is_empty())

    da.rotate_right(2)
    print("After rotate:", da)

    da.reverse()
    print("After reverse:", da)

    da.append(5)
    da.prepend(0)
    print("After append and prepend:", da)

    da2 = DynamicArray()
    da2.append(6)
    da2.append(7)
    da.merge(da2)
    print("After merge:", da)

    da3 = DynamicArray()
    da3.append(8)
    da3.append(9)
    da.interleave(da3)
    print("After interleave:", da)

    print("Middle element:", da.find_middle())
    print("Index of 4:", da.index_of(4))

    first_half, second_half = da.split_at_index(3)
    print("First half:", first_half)
    print("Second half:", second_half)

    da.resize(10)
    print("After resize:", da)
