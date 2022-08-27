class Node(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.list_len = 0
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.node_hash = {}
        
    def remove_from_list(self,node):        
        # remove from the node_list
        pre_node = node.prev
        next_node = node.next
        pre_node.next = next_node
        next_node.prev = pre_node
        
    def move_to_head(self,node):
        # add to the head
        after_head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = after_head
        after_head.prev = node 

    def remove_tail_node(self):
        last_node = self.tail.prev
        before_last_node = last_node.prev
        before_last_node.next = self.tail
        self.tail.prev = before_last_node
        self.node_hash.pop(last_node.key)
        del last_node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_hash:
            return -1
        
        node = self.node_hash[key]
        self.remove_from_list(node)
        self.move_to_head(node)
        
        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if already exist
        if key in self.node_hash:
            node = self.node_hash[key]
            self.remove_from_list(node)
            self.move_to_head(node)
            node.val = value
        else:
            # not exist
            node = Node()
            node.key = key
            node.val = value
            self.node_hash[key]=node
            
            # add to list
            if self.list_len<self.capacity:
                self.list_len+=1
                self.move_to_head(node)
            # remove old node
            else:
                self.remove_tail_node()
                self.move_to_head(node)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)