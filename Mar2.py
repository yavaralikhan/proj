class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = []
        for i in range(capacity):
            self.table.append([])


    def hashCode(self, data):
        idx = id(data) % self.capacity
        return idx

    def put(self, data):
        idx = self.hashCode(data)
        self.table[idx].append(data)
        print("Data {} inserted at index {}".format(data, idx))
        self.size += 1

    def iterate(self):
        for i in range(self.capacity):
            if len(self.table[i]) != 0:
                print("Data in Bucket", i)

                for data in self.table[i]:
                    print(data)


"""
class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = []
        for i in range(capacity):
            self.table.append(None)

    def hash(self, data):
        idx = data % self.capacity
        return idx

    def put(self, data):
        idx = self.hash(data)
        self.table[idx] = data
        print("Data {} inserted at index {}".format(data, idx))

    def find(self,data):
        idx = self.hash(data)
        if self.table[idx] == data:
            return idx
        else:
            return  -1


    def iterate(self):
        for i in range(self.capacity):
            if self.table[i] != None:
                print(self.table[i])


def main():


    htable1 = HashTable(12)
#htable2 = HashTable(12)

    htable1.put(20)
    htable1.put(12)
    htable1.put(13)
    htable1.put(14)
    htable1.put(52)


    print(htable1.table)

    htable1.iterate()

if __name__ == '__main__':
    main()
"""