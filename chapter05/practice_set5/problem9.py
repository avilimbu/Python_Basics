# Can you change the value inside the list which contained in a set S,
# s = {8, 7, 12, "harry", [1,2]} 

s = {8, 7, 12, "harry", [1,2]} 

# print(s) || cannot be performed as 
# TypeError: cannot use 'list' as a set element (unhashable type: 'list')

# set is immutable so we cannot change value either it is hashable