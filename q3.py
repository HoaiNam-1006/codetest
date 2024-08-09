import json
import sqlite3
from datetime import datetime
json_file = 'employees.json'
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY,
    name VARCHAR[50],
    department VARCHAR[50],
    salary INT,
    join_date DATE
)
''')
def trf_date(date_str):
    if date_str is None:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print(f"Error: Wrong date format :{date_str}")
        return None
with open(json_file, 'r') as f:
    data = json.load(f)
for extract in data:
    id = extract.get('id')
    name = extract.get('name')
    department = extract.get('department')
    salary = extract.get('salary')
    join_date_str = extract.get('join_date')
    join_date = trf_date(join_date_str)
    if id =="" or name=="" or department=="" or salary =="" or join_date =="":
        print(f"Missing data: {extract}")
        continue
    cursor.execute(''' INSERT OR REPLACE INTO employees (id, name, department, salary, join_date) VALUES (?, ?, ?, ?, ?) '''
                   , (id, name, department, salary, join_date))
conn.commit()
conn.close()
print ("ETL process completed successfully")
