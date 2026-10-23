"""
Problem: Second Highest Salary (LeetCode #176)
SQL & Python Pandas/SQLite Simulation
"""

import sqlite3

def get_second_highest_salary():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE Employee (id INT, salary INT)")
    cur.executemany("INSERT INTO Employee VALUES (?, ?)", [(1, 100), (2, 200), (3, 300)])

    query = """
    SELECT MAX(salary) AS SecondHighestSalary
    FROM Employee
    WHERE salary < (SELECT MAX(salary) FROM Employee);
    """
    cur.execute(query)
    res = cur.fetchone()[0]
    conn.close()
    return res

if __name__ == "__main__":
    assert get_second_highest_salary() == 200
    print("✅ All Database tests passed!")
