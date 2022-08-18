class MyHashMap:
    def __init__(self, size):
        self.size = size
        self.array = [[]] * size


    def hash(self, key):
        return len(key) % self.size

    def set(self, key, value):
        hash_address = self.hash(key)
        if self.array[hash_address] :
            self.array[hash_address].append([key, value])
        else:
            self.array[hash_address] = [[key, value]]

        return

    def get(self, key):
        hash_address = self.hash(key)
        address_content = self.array[hash_address]
        for content in address_content:
            if key == content[0]: return content[1]
        else:
            raise Exception('key not found in hash map')

    def keys(self):
        keys=[]
        for els in self.array:
            for key in els:
                if key: keys.append(key[0])
        return keys

if __name__ == '__main__':
    myHashMap = MyHashMap(50)

    myHashMap.set('grapes', 100)
    myHashMap.set('apples', 100)
    myHashMap.set('pineapple', 300)
    myHashMap.set('strawberry', 200)
    print(myHashMap.get('grapes'))
    print(myHashMap.get('apples'))
    print(myHashMap.get('pineapple'))
    print(myHashMap.get('strawberry'))
    print(f'keys: {myHashMap.keys()} ' )