import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import sqlite3

def db_check():
    try:
        conn = sqlite3.connect('MYDB.db')
        cursor = conn.execute("SELECT * FROM students")
        print('DB found')
        conn.commit()
        conn.close()

        
    except:
        conn = sqlite3.connect('MYDB.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS students (
                            sid INTEGER PRIMARY KEY,
                            name TEXT,
                            contact TEXT,
                            status TEXT);
                 ''')
        print('DB Created')
        conn.commit()
        conn.close()

def print_data():
    conn = sqlite3.connect('MYDB.db')
    cursor = conn.execute("SELECT sid,name,contact,status FROM students")
    for row in cursor.fetchall():
        print(f"sid:{row[0]} name:{row[1]} contact:{row[2]} \t status:{row[3]}")
    conn.commit()
    conn.close()

def add_data(sid,name,contact,status):
    conn = sqlite3.connect('MYDB.db')    
    conn.execute(f"INSERT INTO students (sid,name,contact,status) \
            VALUES ({sid},'{name}', '{contact}', '{status}')")
    conn.commit()
    conn.close()

def delete_data(sid):
    conn = sqlite3.connect('MYDB.db')
    conn.execute("DELETE FROM students WHERE sid = ?", (sid,))
    conn.commit()
    conn.close()

def update_data(sid, name, contact, status):
    conn = sqlite3.connect('MYDB.db')
    conn.execute("UPDATE students SET name=?, contact=?, status=? WHERE sid=?", (name, contact, status, sid))
    conn.commit()
    conn.close()

db_check()
add_data(1027,'Pradip','8735809219','active')
add_data(1029,'Sandip','8735809219','alumni')
add_data(1043,'Sandip','8735809219','active')
print_data()
delete_data(1027)
print_data()
update_data(1029,'Sandip','8735809219','active')
print_data()