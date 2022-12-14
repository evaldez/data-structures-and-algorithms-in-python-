from collections import deque

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

    def breadthFirstSearch(self) -> list:
        current_node = self.root
        stop_condition = False
        queue = deque([])
        queue.append(current_node)
        counter=0
        result = []
        while queue:
            current_node = queue.popleft()
            result.append(current_node.value)
            if current_node.left: queue.append(current_node.left)
            if current_node.right: queue.append(current_node.right)
        return result

    def breadthFirstSearchR(self, queue=None, result=None ):
        if queue is None: 
            queue = deque([])
            queue.append(self.root)
        if result is None: result = []
        
        # base case
        if not queue: return result
        
        # recursive case
        current_node = queue.popleft()
        result.append(current_node.value)
        if current_node.left: queue.append(current_node.left)
        if current_node.right: queue.append(current_node.right)
        result = self.breadthFirstSearchR(queue, result )
        
        # return the result
        return result

    def dfs_preorder(self) -> list:
        current_node = self.root
        stop_condition = False
        stack = []
        stack.append(current_node)
        result = []
        while stack:
            current_node = stack.pop()
            result.append(current_node.value)
            if current_node.right: stack.append(current_node.right)
            if current_node.left: stack.append(current_node.left)
        return result

    def checkBFS(self) -> list:
        root= self.root
        current_node = root
        queue = deque([])
        data_current_node ={
            'heritage_trace':[
                #{
                #    'value':None, # node value 
                #    'brach_type': None # if comes from left or right
                #}
            ],
            'node' : current_node
        }
        queue.append(data_current_node)
        while queue:
            data_current_node = queue.popleft()
            current_node= data_current_node['node']
            heritage_trace= data_current_node['heritage_trace']
            if current_node.left: 
                if current_node.left.val >= current_node.val: return False
                data_left_child_node = {
                    'node':current_node.left
                }
                data_left_child_node['heritage_trace']=[]
                data_left_child_node['heritage_trace']+=heritage_trace
                # Set parent node data
                instant_parent_node_data ={
                    'value': current_node.val, # node value 
                    'brach_type': 'l' # if comes from left or right
                }
                data_left_child_node['heritage_trace'].append(instant_parent_node_data)
                queue.append(data_left_child_node)
            if current_node.right: 
                if current_node.right.val <= current_node.val: return False
                data_right_child_node = {
                    'node':current_node.right
                }
                data_right_child_node['heritage_trace']=[]
                data_right_child_node['heritage_trace']+=heritage_trace
                # Set parent node data
                instant_parent_node_data ={
                    'value': current_node.val, # node value 
                    'brach_type': 'r' # if comes from left or right
                }
                data_right_child_node['heritage_trace'].append(instant_parent_node_data)
                queue.append(data_right_child_node)
            
            # check for heritage trace
            if heritage_trace:
                for every_parent_node in heritage_trace:
                    if every_parent_node['brach_type'] == 'r':
                        if every_parent_node['value'] >=  current_node.val: return False
                    if every_parent_node['brach_type'] == 'l': 
                        if every_parent_node['value'] <=  current_node.val: return False
        return True

if __name__ == '__main__':

    test_bfs = False
    test_dfs_preorder = False
    test_remove = False
    test_check_bfs = True

    tree = BinarySearchTree()
    #nodes = [41,20,11,29,32,65,50,91,72,99]
    nodes = [9, 4, 6, 20, 170, 15, 1]
    for node in nodes:
        tree.insert(node)
    
    if test_check_bfs:
        valid_bfs = tree.checkBFS()
        print(f'valid_bfs: {valid_bfs} ')
    if test_bfs:
        bfs_order = tree.breadthFirstSearchR()
        print(bfs_order)
    
    if test_dfs_preorder:
        dfs_preorder_result = tree.dfs_preorder()
        print(dfs_preorder_result)

    if test_remove:
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