# Dynamic Typing
Types are determined automatically at runtime, not in response to declarations in your code.

- Assign a name to an object such as`a = 3`:
    1. Create object to represent the value 3
    2. Create the variable a, if it does not yet exist
    3. Link the variable a to the new object 3

- Variables and objects are stored in different parts of memory and are associated by links (_reference_. Variables 
always link to objects and never to other variables, but larger objects may link to other objects 
(for instance, a list object has links to the objects it contains). A _reference_ is a pointer in memory. So:
    1. Variables are entries in a system table, with spaces for links to objects
    2. Objects are pieces of allocated memory, with enough space to represent the values for which they stand
    3. References are automatically followed pointers from variables to objects
    
- Types Live with Objects, Not Variables. Names have no types, types live with objects, not names so you can
assign a variable to many objects sequentially and it changes the type by changing the reference:

    `>>> a = 3             # It's an integer`
    
    `>>> a = 'spam'        # Now it's a string`
    
    `>>> a = 1.23          # Now it's a floating point`
    
- Objects contains 2 headers, one that tags the object with its type and a reference counter (Garbage collector
works by reclaiming space taken by unreferenced objects by other name or object automatically)
