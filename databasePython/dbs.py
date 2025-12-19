import sqlite3
# s = sqlite3.connect("mo.db")
# cursor = s.cursor()
# cursor.execute(""" 
# create table if not exists persons(
 #     person_id Integer primary_key ,
#     first_name varchar(30) not null,
#     last_name varchar(30),
#     age Integer )
# """)
# cursor.execute("insert into persons values(1, 'mohamed', 'ramadan', 42);")
# cursor.execute("select * from persons")
# rows = cursor.fetchall()
# print(rows)
# s.commit()
# s.close()
class person: 
    def __init__(self,id_num = -1,first = "",last= "",age= 0 ):
        self.id_num = id_num
        self.first = first
        self.last = last 
        self.age = age 
        self.connection = sqlite3.connect("mo.db")
        self.cursor = self.connection.cursor()
    def load_person(self,id_number):
        
        self.cursor.execute(f'select * from person where id ={id_number}')
        row = self.cursor.fetchone()
        self.id_num = id_number
        self.first =row[1]
        self.last = row[2]
        self.age = row[3]
        print(self.first)            
# connection = sqlite3.connect('mo.db')
# cursor = connection.cursor()
# cursor.execute("create table if not exists person(id integer primary key, first_name varchar(30) ,last_name varchar(30),age integer ); ")
# cursor.execute("insert into person values (1,'mohamed','ramadan',22)")
# connection.commit()
# connection.close()
person1 = person()
person1.load_person(1)