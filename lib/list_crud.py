def create_an_empty_list():
    return []

def create_a_list():
    list = ["a", 2, "c", "orange"]
    return list
# test case
my_list = create_a_list()
print(my_list)




def add_element_to_end_of_list(l, element):
    l.append(element)
    return l
    

new_list = [1,2,3]
element = 5

add_element_to_end_of_list(new_list, element)
print(new_list)





def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l
    

my_list = [1,2,3]
element = 12

add_element_to_start_of_list(my_list, element)
print(my_list)



def remove_element_from_end_of_list(l):
    l.pop()
    return l
    

my_list = [1, 2, 3, 4]    

remove_element_from_end_of_list(my_list)
print(my_list)




def remove_element_from_start_of_list(l):
    if len(l) > 0:
        del l[0]
    return l    
    

my_list = [1, 2, 3, 4]

remove_element_from_start_of_list(my_list)
print(my_list)





def retrieve_first_element_from_list(l):
    if len(l) > 0:
        return l[0]
    else:
        return None
    

my_list = [5, 2, 3, 4]    

first_element = retrieve_first_element_from_list(my_list)
print(first_element)
    



def retrieve_element_from_index(l, index):
    if 0 <= index < len(l):
        return l[index]
    else:
        return None
    

my_list = [20, 35, 43, 65] 
index_to_retrieve = 2   

number = retrieve_element_from_index(my_list, index_to_retrieve)

print(number)





def retrieve_last_element_from_list(l):
    if len(l) > 0:
        return l[-1]
    else:
        return None
    

my_list = [2, 3, 5, 6]

last_element = retrieve_last_element_from_list(my_list)

print(last_element)
