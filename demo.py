import psycopg2
def create():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="german",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE student( ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT)''')
    print('Table created!')
    conn.commit()
    conn.close()

def insert_data():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="german",host="localhost",port="5432")
    cur = conn.cursor()
    name = input("Enter name: ")
    age = input("Enter age: ")
    address = input("Enter address: ")
    query ='''INSERT INTO student(NAME,AGE,ADDRESS) VALUES(%s,%s,%s)'''
    cur.execute(query,(name,age,address))
    print('Info inserted!')
    conn.commit()
    conn.close()

insert_data()