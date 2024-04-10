# Creating a new stack
stack = []

# adding elements to a stack
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print("stack:",stack)
# pop
element = stack.pop()
print("pop:",element)
#peek/top
topElement = stack[-1]
print ("peek:",topElement)

#size
print("size:",len(stack))
