# >>>>> Lists <<<<<
names = ['Sri', 'Gadgeter', 'Sridhar', 'Srigadgeter']
print(names)
print(names[1])
print(names[1:3])
print(names[-2])
print(names[-2:])
print(names[:3])
print(names[:])
names[3] = 'SriGadgeter'
print(names)

print(names[2][1])
print(names[1][1:])
print(names[0][-2:])
print(names[2][:2])
# =========================================
# >>>>> 2D Lists <<<<<
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])
print(matrix[1:])
print(matrix[-1:])
print(matrix[:])

print(matrix[0][0])
print(matrix[2][2])
print(matrix[1][2])

print(matrix[0][1:])

names = [
    ['abc', 'def', 'ghi', 'jkl'],
    ['mno', 'pqr', 'stu', 'vwx'],
    ['yz~', '!@#', '$%^', '&*-']
]
print(names)
print(names[2])
print(names[1][2:])

print(names[2][1])
print(names[1][:2])

print(names[1][0][-1])
print(names[1][3][1:])
print(names[1][1][-3:-1])
# =========================================
# >>>>> List Methods <<<<<
numbers = [3, 4, 9, 0, 2, 6, 4]

numbers.append(8)  # Add a new element @ last
numbers.insert(0, 8)  # Add a new element @ the given position
numbers.insert(4, 8)
numbers.remove(9)  # Remove first occurrance of the value given
numbers.pop()  # Remove the last element
numbers.pop(2)  # Remove the element based on index
numbers.sort()  # Sort A -> Z
numbers.sort(reverse=True)  # Sort Z -> A (Reverse Sort)
numbers.reverse()  # Reverse the list
print(numbers)
numbers.clear()  # Remove all the elements in the list
print(numbers)

numbers = [3, 4, 9, 0, 2, 6, 4]
numbers2 = numbers.copy()
numbers3 = numbers[:]
numbers.append(32)
print(numbers, numbers2, numbers3)

print(numbers.index(4))  # Prints the first occurrence of the given element
print(numbers.index(5))  # And it will throw an ValueError if there is no such element in the list
print(4 in numbers, 5 in numbers)
print(numbers.count(4))  # Prints the number of occurrences of the given element
print(numbers.count(9))
print(numbers.count(5))
