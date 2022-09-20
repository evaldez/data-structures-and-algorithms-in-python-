class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def is_leaf(self):
        if (not self.left) and (not self.right):  return True
        return False
            

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        
        stop_condition = False
        current_node = self.root
        parent_node = None
        link_type = None

        while not stop_condition:
            
            if getattr(current_node, 'value', False):
                if current_node.value == new_node.value:
                    raise ValueError('Duplicated value in node not allowed')
            
            if not current_node:
                current_node = new_node
                if link_type == 'right':
                    parent_node.right = current_node
                else: 
                    parent_node.left = current_node
                break

            if new_node.value > current_node.value:
                # go to right
                parent_node = current_node
                current_node = current_node.right
                link_type = 'right'
            else:
                # go to left
                parent_node = current_node
                current_node = current_node.left
                link_type = 'left'
        return
    
    def lookup(self,value):
        trace = []
        stop_condition = False
        current_node = self.root
        parent_node = None
        while not stop_condition:

            if not current_node:
                return Node(), Node(), trace

            if current_node.value == value:
                return  current_node, parent_node, trace

            if value > current_node.value:
                # go to right
                trace.append({'value':current_node.value, 'link':'r'})  
                parent_node = current_node     
                current_node = current_node.right
                continue
            if value < current_node.value:
                # go to left
                trace.append({'value':current_node.value, 'link':'l'})  
                parent_node = current_node     
                current_node = current_node.left
                continue
            
        return

    def remove(self, value):
        if not self.root:
            return False

        node_to_delete, parent_node, trace = self.lookup(value)
        is_root_node=False
        parent_link=None
        if not parent_node:
            is_root_node=True
        else:
            parent_link = trace[-1]['link']
       
        # is leaf node, delete it
        if node_to_delete.is_leaf():
            if not is_root_node:
                if parent_link == 'l': 
                    parent_node.left = None
                else:
                    parent_node.right = None
                return
            else:
                self.root=None
        
        # if node has a single child
        if bool(node_to_delete.left) != bool(node_to_delete.right):
            # IS a root node
            if not is_root_node:
                if node_to_delete.left:
                    if parent_link == 'l': 
                        parent_node.left = node_to_delete.left
                    else:
                        parent_node.right = node_to_delete.left
                    return
                else:
                    if parent_link == 'l': 
                        parent_node.left = node_to_delete.right
                    else:
                        parent_node.right = node_to_delete.right
                    return
            # IS NOT a root node
            else:
                if node_to_delete.left:
                    self.root = node_to_delete.left
                    return
                if node_to_delete.right:
                    self.root = node_to_delete.right
                    return       

        # if node has a two childs, 
        # find the inorder succesor in the right sub-tree
        sub_tree_starting_node = node_to_delete.right
        in_order_succesor = self.find_in_order_successor(sub_tree_starting_node)
        # copy value of in-order sucesor
        # in inorder successor will never have a left child
        in_order_succesor_value = in_order_succesor.value
        self.remove(in_order_succesor.value)
        node_to_delete.value = in_order_succesor.value

    def find_in_order_successor(self, sub_tree_starting_node):
        current_node = sub_tree_starting_node
        stop_condition = False
        counter=0
        while not stop_condition:
            if current_node.is_leaf() : return current_node
            if not current_node.left: return current_node
            current_node = current_node.left
            if counter==1:
                raise Exception('debugging')
            counter+=1
        return


if __name__ == '__main__':
    tree = BinarySearchTree()
    nodes = [41,20,11,29,32,65,50,91,72,99]
    for node in nodes:
        tree.insert(node)
    found_tree, parent_node, trace  = tree.lookup(99)
    print(f'found_tree.value {found_tree.value}')
    print(f'trace {trace} ')
    tree.remove(41)
    found_tree, parent_node, trace  = tree.lookup(99)
    print('AFTER REMOVE {41} ')
    print(f'found_tree.value {found_tree.value}')
    print(f'trace {trace} ')
    tree.remove(50)
    found_tree, parent_node, trace  = tree.lookup(32)
    print('AFTER REMOVE  {50}')
    print(f'found_tree.value {found_tree.value}')
    print(f'trace {trace} ')