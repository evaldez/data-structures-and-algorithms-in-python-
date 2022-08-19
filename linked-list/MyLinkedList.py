from contextlib import nullcontext


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:
    def __init__(self, head_value):
        new_node = Node(head_value)
        self.head = new_node
        self.tail = self.head
        self.length=1
        return

    def appendRecursive(self, value, current_node=None, previous_node=None, ):
        if not current_node : current_node  = self.head 

        if current_node.next: 
            # pointer found
            self.appendRecursive(value, current_node.next)
        else:
            # found a node with empty pointer
            new_node = Node(value)
            current_node.next = new_node
            self.length += 1
            self.tail = new_node
        return

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return self
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self 

    def get_node_values(self):
        node_values=[]
        tmp_node = self.head
        while tmp_node != None:
            node_values.append(tmp_node.value)
            tmp_node = tmp_node.next
            if not tmp_node: break
        return node_values
    
    def insert(self, index, value):
        if index > self.length-1: raise IndexError(f'Index {index} out of bound')
        # insert in head
        if index == 0: 
            self.prepend(value)
            return self
        # insert in tail
        if index == self.length-1 : 
            self.append(value)
            return self
        
        new_node = Node(value)
        tmp_index=1
        previous_node = self.head
        current_node = self.head.next
        while tmp_index < self.length :
            if index == tmp_index:
                new_node.next = current_node
                previous_node.next = new_node
                self.length+=1
                break
            else:
                tmp_index+=1
                previous_node = current_node
                current_node = current_node.next

    def remove(self, index):
        if index > self.length-1: raise IndexError(f'Index {index} out of bound')
        
        # remove head
        if index == 0:
            self.head = self.head.next
            self.length-=1
            return
        # otherwise
        tmp_index = 1
        previous_node = self.head
        current_node = self.head.next
        while tmp_index < self.length :
            if index == tmp_index:
                previous_node.next = current_node.next
                self.length-=1
                break
            else:
                tmp_index+=1
                previous_node = current_node
                current_node = current_node.next        
        return

    def invert(self):
        if not self.head.next: return self.head
        first = self.head
        self.tail = self.head
        second = self.head.next
        while(second):
            tmp = second.next
            second.next = first
            first=second
            second = tmp
        
        self.tail.next=None
        self.head = first
        
        return self

if __name__ == '__main__':
    head_value=10
    linked_list= MyLinkedList(10)
    linked_list.append(6)
    linked_list.append(8)
    linked_list.append(123)
    linked_list.append(23123)
    linked_list.prepend(1990)
    print(linked_list.get_node_values())
    linked_list.insert(1, 88)
    print(linked_list.get_node_values())
    linked_list.remove(3)
    print(linked_list.get_node_values())
    linked_list.remove(0)
    print(linked_list.get_node_values())
    invertedLinked = linked_list.invertV2()
    print(invertedLinked.get_node_values())