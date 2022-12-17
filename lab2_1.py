# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 01:10:36 2022

@author: Polina <3
"""

# import pymongo
# from pymongo import MongoClient

# # Create the client
# client = MongoClient('localhost', 27017)

# # Connect to our database
# db = client['test']6

# # Fetch our series collection
# series_collection = db['users']

# print(db.list_collection_names())
# print(series_collection.find_one())


import tkinter as tk
from pymongo import MongoClient


document = {}


def add_to_document():
    # . - вложенный ключ
    keys = entry1.get().split('.')
    print(keys)
    link = document
    flag = False

    if len(keys) > 1:
        flag = True

    for key in keys:
        if len(keys) > 1:
            if key == keys[-1] and key not in link:
                link[key] = []
                flag = True

            else:
                if key not in link:
                    link[key] = {}

            link = link[key]


       

    if flag:
        #link.append({keys[-1]:entry2.get()})
        link.append(entry2.get())

    else:
        link[keys[-1]] = entry2.get()
    
    print(document)

    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)


def send_to_server():
    global document
    db.polina.insert_one(document)
    document = {}


def view_info():
    # table_of_document.delete(0, table_of_document.size() - 1)
    table_of_document.delete(1.0, tk.END)
    line = 1.0
    i = 0
    
    #########
    # ЗДЕСЬ НУЖНО ДОДЕЛАТЬ, ЧТОБЫ КРАСИВО ВЫВОДИЛ!!!!!
    #########
    for doc in db.polina.find():
        
        doc.pop('_id', None)
        print(doc)
        table_of_document.insert(line, doc)
        line+=1.0
        table_of_document.insert(line,"\n")   

        # table_of_document.insert(line, f"{i}\n")
        # line += 1.0
        # print(doc.keys())
        # for val in doc.keys():
        #     if val == 'Стартовый состав' or val == 'Запасные' or val == 'Нарушение правил' or val == 'Забитые мячи' or val == 'Пенальти' or val == 'Удары по воротам':   
        #         # ЗДЕСЬ СДЕЛАТЬ КАКУЮ-ТО ПРОВЕРКУ, ЧТОБЫ НЕ ВЫВОДИЛ ДВАЖДЫ ОДИНАКОВЫЕ АГРЕГАТЫ {"Игрок" {"Игрок":...}
        #         znach = "{" + val + " " + str(doc[val]) + "}"
        #         #print("!!!!!!!   ", znach)
        #         table_of_document.insert(line, znach)
        #          line += 1.0
        #         table_of_document.insert(line, "\n")  
        #         line += 1.0
        #     else:
        #       #  print("&&&&&&", doc[val])
        #         znach = doc[val]
        #         table_of_document.insert(line, znach)
        #         line += 1.0
        #         table_of_document.insert(line, "\n")               
        #         line += 1.0
            

        line += 1.0
        table_of_document.insert(line, "\n")
        line += 1.0
        i += 1

# Create the client
client = MongoClient('localhost', 27017)
db = client["polina"]

root = tk.Tk()

root.title("Футбол")
root.geometry("650x500")


# lbl1 = Label(frame1, text="Заголовок", width=10)
# lbl1.pack(side=LEFT, padx=5, pady=5)

# entry1 = Entry(frame1)
# entry1.pack(fill=X, padx=5, expand=True)

lbl1 = tk.Label(root,text='Ключ', width=10)
lbl1.grid(row=0, column=0)

entry1 = tk.Entry(root,width=35)
entry1.grid(row=0,column=1,columnspan=2,sticky='w')

# lbl3 = Label(frame3, text="Отзыв", width=10)
# lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)        
 
# txt = Text(frame3)
# txt.pack(fill=BOTH, pady=5, padx=5, expand=True)


lbl2 = tk.Label(root,text='Значение',width=10)
lbl2.grid( row=1,column=0)

entry2 = tk.Entry(root, width=35)
entry2.grid(row=1, column=1,columnspan=2,sticky='w')

button1 = tk.Button(root, text='Добавить ключ-значение', command=add_to_document)
button1.grid(row=1,column=3)

button2 = tk.Button(root, text='Сохранить документ', command=send_to_server)
button2.grid(row=3, column=1,padx=(5,10), pady=(10,10))

# lbl3 = tk.Label(text='')
# lbl3.pack(side ='top', padx=5, pady=5, anchor=tk.N)

button3 = tk.Button(root, text='Показать документы', command=view_info)
button3.grid(row=3,column=2, pady=(10,10))


# table_of_document = tk.Listbox(root, selectmode=tk.EXTENDED, font=("Comic Sans MS", 10))
table_of_document = tk.Text(root,width=400, wrap=tk.WORD)
table_of_document.grid(row=4,column=0, columnspan=4)

scrollbar = tk.Scrollbar(root,  orient='vertical')
scrollbar.grid(row=4, column=4, sticky=tk.N+tk.S)

table_of_document.config(yscrollcommand=scrollbar.set,width=50,height=20)
scrollbar.config(command=table_of_document.yview)





root.mainloop()