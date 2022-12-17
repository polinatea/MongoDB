# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 01:10:36 2022

@author: Polina <3
"""

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
    table_of_document.delete(1.0, tk.END)
    line = 1.0
    i = 0
    

    #########
    for doc in db.polina.find():
        
        doc.pop('_id', None)
        print(doc)
        table_of_document.insert(line, doc)
        line+=1.0
        table_of_document.insert(line,"\n")   
         

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

lbl1 = tk.Label(root,text='Ключ', width=10)
lbl1.grid(row=0, column=0)

entry1 = tk.Entry(root,width=35)
entry1.grid(row=0,column=1,columnspan=2,sticky='w')


lbl2 = tk.Label(root,text='Значение',width=10)
lbl2.grid( row=1,column=0)

entry2 = tk.Entry(root, width=35)
entry2.grid(row=1, column=1,columnspan=2,sticky='w')

button1 = tk.Button(root, text='Добавить ключ-значение', command=add_to_document)
button1.grid(row=1,column=3)

button2 = tk.Button(root, text='Сохранить документ', command=send_to_server)
button2.grid(row=3, column=1,padx=(5,10), pady=(10,10))

button3 = tk.Button(root, text='Показать документы', command=view_info)
button3.grid(row=3,column=2, pady=(10,10))

table_of_document = tk.Text(root,width=400, wrap=tk.WORD)
table_of_document.grid(row=4,column=0, columnspan=4)

scrollbar = tk.Scrollbar(root,  orient='vertical')
scrollbar.grid(row=4, column=4, sticky=tk.N+tk.S)

table_of_document.config(yscrollcommand=scrollbar.set,width=50,height=20)
scrollbar.config(command=table_of_document.yview)


root.mainloop()