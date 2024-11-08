#!/usr/bin/env python3

def array_of_names(name_book: dict):
    array_name = []
    for name in name_book:
        array_name.append(str(name[0]).upper()+name[1:]
                          +' '
                          +str(name_book[name][0]).upper()+name_book[name][1:]
                          )
        
    return array_name

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))