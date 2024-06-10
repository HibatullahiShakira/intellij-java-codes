import collections


class Task:
    def __init__(self, collection):
        self.collection = collection

    def length_return(self, collection):
        count = 0
        for number in collection:
            count += 1
        return count


#tuple1 = (0, "ojo", 2.5, [])
#tuple1[3].extend([1, 3, "kent"])
#names = ["affeez", "eniola", "janet"]
#names += tuple1
#names = tuple(names)
#print(tuple1)
#print(names.index("afeez"))
#print(names)

#Set
#declaring empty set in pyhon
y = set()
#declaring a set with element in it
x = {1, 1, 2, 3, 2, 2, 4, 5, 1}
#x = [1, 1, 2, 3, 2, 2, 4, 5, 1]
# cast a set to array before to get the length of the set
print(len(set(x)))
y = {1, 3, 7, 9,10,2}
print(x.union(y))
print(x.difference(y))
print(x.intersection(y))
print(x.issubset(y))
print(x.symmetric_difference(y))

#Stack Data Structure
