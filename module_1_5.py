immutable_var = [21, "собака", 14, 7, "John"]
tuple=immutable_var
print(tuple)
# заменить элемент кортежа нельзя, а в нашем случае невозможно выделить часть списка внутри кортежа, поскольку кортежем является переменная immutable_var
mutable_list = [3,9,27, 'fox', 'elephant']
print(mutable_list)
mutable_list[2]='frog'
print(mutable_list)
mutable_list.append('cat')
print(mutable_list)