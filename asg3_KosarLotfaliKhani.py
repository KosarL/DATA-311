class BST: 
    def __init__(self, value = None): # Define the nodes of BST 
        self.value = value 
        self.left = None 
        self.right = None 
        
    
    
    def insert(self, value): # Inserts an element into BST  
        if not self.value: # Self is equivalent to current_node 
            self.value = value 
            return      
        
        if self.value == value: 
            return 
        
        if value < self.value: 
            if self.left: # Checking if the left node is empty or not 
                self.left.insert(value) 
                return 
            self.left = BST(value) # Create a new left node if the left node is empty
            return 
        
        if value > self.value: 
            if self.right:
                self.right.insert(value)
                return 
            self.right = BST(value)  # Creating a new right node if empty 
    
    
    
    def min_val (self): # gets the lowest value of the BST nodes 
        current_node = self 
        while current_node.left is not None: # checking for the left-most node 
            current_node = current_node.left 
        return current_node.value 
    

    def max_val (self): # gets the highest value of BST nodes
        current_node = self 
        while current_node.right is not None: #checking for the right-most node 
            current_node = current_node.right
        return current_node.value
    
    
    
    def sum_nodes(self, output_list, given_value = None): # calculates the sum of nodes lower than an input number
        
        if self.left is not None: # using inorder traversal to sort the node values from lowest to highest and appending onto output_list
            self.left.sum_nodes(output_list)
        if self.value is not None:
            output_list.append(self.value)
        if self.right is not None:
            self.right.sum_nodes(output_list)
        
        cur_sum = 0
        for i in output_list: #looping through the output_list to sum all the values < given_value 
            if given_value is not None: 
                if i < given_value:
                    cur_sum += i
                else:
                    return cur_sum
        return cur_sum
        
    
    
    def num_nodes (self): # calculates the number of nodes in the BST   
        if self.value is None: # checking to see if BST is empty 
            return 0
        else:
            count = 1
            if self.left is not None: 
                count += self.left.num_nodes() # adding the left nodes to the count
            if self.right is not None:
                count += self.right.num_nodes() # adding the right nodes to the count
            return count 
  


bst_example= BST()

# for user: input the node values you wish to add to the BST
nodes = [1,2,3,4,5,6,7,8,9,10]
for node in nodes:
    bst_example.insert(node)

print("The minimum value of the BST is:", bst_example.min_val())  
print("The maximum value of the BST is:", bst_example.max_val())  
print("The number of nodes of the BST is:", bst_example.num_nodes())

print("The sum of the nodes lower than the input value is:", bst_example.sum_nodes(output_list = [], given_value = 10))
   