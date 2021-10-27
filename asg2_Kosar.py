# QUESTION 1
def evalPostfix(e):
    e = e.split()
    stack = []
    while len(e) != 0:
        for i in range(len(e)):
            if e[i].isdigit():
                stack.append(int(e[i]))
            else:
                if len(stack) < 2:
                    print("Error", stack)
                else:
                    if e[i] == '+':
                        first_num = stack.pop()
                        second_num = stack.pop()
                        stack.append(int(first_num) + int(second_num))
                    elif e[i] == '-':
                        first_num = stack.pop()
                        second_num = stack.pop()
                        stack.append(int(second_num) - int(first_num))
                    elif e[i] == '*':
                        first_num = stack.pop()
                        second_num = stack.pop()
                        stack.append(int(first_num) * int(second_num))
                    elif e[i] == '/':
                        first_num = stack.pop()
                        second_num = stack.pop()
                        stack.append(int(second_num) / int(first_num))
        break
    if len(stack) == 1:
        print(stack.pop())
    else:
        print ("Error", stack)

    
e = input("Enter your postfix notation: ")
evalPostfix(e)









# QUESTION 2
# the following code uses the insert_first and insert_last functions previously covered in tutorials 


class Node:
    def __init__(self,assign_value): # Constructor of the class 
        self.value = assign_value  # Assign a value to the value variable 
        self.next = None # Assign none to the address variable as their is no node we need point initially 

class linked_list:
    def __init__(self):
        self.head = None  # Head variable for accessing the linked list 
        self.tail = None 

        
    def insert_first(self,value): # Insert an element at the beginning of the linked list 
        new_node = Node(value) # Create a new node 
        if self.head == None and self.tail == None:  # Check if linked list is empty 
            self.head = new_node # For the first node head and tail will pointing at the same node 
            self.tail = new_node 
        else:
            temp = self.head # Put the current head into a temporary variable 
            new_node.next = temp # Point the new nodes next variable to current head 
            self.head = new_node # Change the current head to new node 
        print("Head node successfully added")
            
    def insert_last(self,value): # Insert an element at the end of the linked list 
        new_node = Node(value)
        if self.head == None and self.tail == None: # Checking if my linked list is empty or not 
            self.head = new_node  
            self.tail = new_node 
        else:
            temp = self.tail  # keep the current tail node into a temporary varialbe 
            temp.next = new_node  # Point the current tail nodes pointer to the new node  
            self.tail = new_node  # make the new node as the new tail 
        print("Tail node successfully added")
            
################################################################################################################            
            
            
    def add_element (self, target, value): # Insert an element in the middle after some target value 
        new_node = Node(value)
        temp = self.head
        if self.head == None and self.tail == None:
            print("The list is not initialized")
        while temp:# Iterate through the linked list 
            if temp.value == target:  # If my current nodes value is equal to my target value 
                new_node.next = temp.next # New nodes next pointer will point at temporary nodes next pointer
                temp.next = new_node # Temporary nodes next pointer will be pointing at new nodes address
                break # Break the loop after insertion
            
            else:
                temp = temp.next
        print("Node successfully added")
                
                
                
    def count_element(self, element): # print the count of elements in a singly linked list 
        # count the number of occurances of a value in a SLL 
        temp = self.head
        element_count = 0
        if self.head == None and self.tail == None:
            print("0 elements")
        while temp is not None:
            if temp.value == element:
                element_count += 1
            temp = temp.next 
        print("The count of the given value is: ", element_count) 
     
    
    
    def search_element(self, key): # determine whether a provided element exist in the list
        if self.head == None and self.tail == None:
            print("The list is not initialized")
        temp = self.head 
        while temp != None:
            if temp.value == key:
                #print("the entered value is within list boundaries") 
              
                return True # the node is found 
            
            temp = temp.next 
        return False # the node is not found 
    
    
    def delete_first(self):
        temp = self.head # point a temp variable to the current head
        temp = temp.next # move the temp var to the next node 
        self.head = temp # make the temp node which is now pointing at the second node of the linked list, the head
        print("Head node successfully removed")
        
        
        
    def delete_last (self):
        # change the one before the tail to null (not poinitng to anything anymore)
        # second thing - change tail variable pointing to this one
        # p = finding the variable before the tail node (the one we are deleting)
        # q = tail node of the list (the one being deleted)
        p = self.head # pointing at the head node
        q = self.head.next # pointing at teh immediate next node after the head
        
        while q: #this loop will iterate until q reaches the end where q is pointing at null
            p = p.next 
            q = q.next 
        p.next = None # making the P varibale (previous node of the current list) to null
        self.tail = p  #making P the new tail node
        print("Tail node successfully removed")
        
        
        
    def delete_value (self, value):
        # erasing q from linked list 
        # make p point to the node q is pointing at 
        p = self.head
        q = self.head.next 
        while q:
            if q.value == value:
                p.next = q.next # make p variable which is teh node previous to the node we want to delete, to the node q is currently pointing at
                break # break after finding the target position
            else:
                p = p.next 
                q = q.next 
        print("Node successfully removed")
        
    def print(self):
        if self.head == None: # check to see if linked list is empty
            print("Empty List")
        else:
            temp = self.head
            print('[', end ='')
            while temp:
                if temp.next != None: 
                    print(temp.value, end =',') # print the values 
                else:
                    print(temp.value,']')
                temp = temp.next  # change the temporary node to next node      




my_list = linked_list() 

# optional - looking for user input for head node, tail node, and other values to be inserted  
# user could also use the hashed code to enter the values for linked list manually (provide value for x and add as many lines as needed)

head_node_value = int(input("Enter the value of head node: "))
my_list.insert_first(head_node_value) 

tail_node_value = int(input("Enter the value of tail node: "))
my_list.insert_last(tail_node_value) 

element_value = int(input("Enter the value for the new node: "))
target_value = int(input("Enter the target value: "))
my_list.add_element(target_value, element_value)


# my_list.insert_first(x) 
# my_list.insert_last(x) 
# my_list.add_element (x,x)



search_element_value = int(input("Enter a value to be searched:"))
if my_list.search_element(search_element_value):
    print("The entered value is within list boundaries")
else:
    print("The entered value is not within list boundaries")


element_for_count = int(input("Enter the element to be counted:"))
my_list.count_element(element_for_count)

my_list.print() 

