import streamlit as st
import sqlite3
import pandas as pd

# 1. Database Connection & Setup
def init_db():
    conn = sqlite3.connect('college.db')
    c = conn.cursor()
    # Create Table if not exists
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll_no TEXT UNIQUE,
            subject TEXT,
            marks INTEGER,
            grade TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Calculate Grade automatically
def calculate_grade(marks):
    if marks >= 90: return 'O (Outstanding)'
    elif marks >= 80: return 'A+ (Excellent)'
    elif marks >= 70: return 'A (Very Good)'
    elif marks >= 60: return 'B (Good)'
    elif marks >= 50: return 'C (Pass)'
    else: return 'F (Fail)'

# --- SQL Functions ---
def add_student(name, roll_no, subject, marks):
    conn = sqlite3.connect('college.db')
    c = conn.cursor()
    grade = calculate_grade(marks)
    try:
        c.execute('INSERT INTO students (name, roll_no, subject, marks, grade) VALUES (?,?,?,?,?)', 
                  (name, roll_no, subject, marks, grade))
        conn.commit()
        st.success(f"Student {name} Added Successfully!")
    except sqlite3.IntegrityError:
        st.error("Error: Roll Number already exists!")
    conn.close()

def view_students():
    conn = sqlite3.connect('college.db')
    df = pd.read_sql_query("SELECT * FROM students", conn)
    conn.close()
    return df

def delete_student(roll_no):
    conn = sqlite3.connect('college.db')
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()
    conn.close()
    st.warning(f"Roll No {roll_no} Deleted Successfully!")

# --- APP UI ---
def main():
    st.title("🎓 Student Result Management System")
    st.markdown("### Built with Python & SQL")

    # Initialize DB
    init_db()

    # Sidebar Menu
    menu = ["Add Student", "View Results", "Delete Student"]
    choice = st.sidebar.selectbox("Menu", menu)

    # 1. ADD STUDENT PAGE
    if choice == "Add Student":
        st.subheader("Enter Student Details")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Student Name")
            roll_no = st.text_input("Roll Number (Example: 20A51)")
        with col2:
            subject = st.selectbox("Subject", ["Python", "SQL", "Data Science", "Java"])
            marks = st.number_input("Marks (0-100)", min_value=0, max_value=100)
        
        if st.button("Save Result"):
            if name and roll_no:
                add_student(name, roll_no, subject, marks)
            else:
                st.error("Please fill all fields")

    # 2. VIEW RESULTS PAGE
    elif choice == "View Results":
        st.subheader("All Students Database")
        result_df = view_students()
        st.dataframe(result_df)
        
        # Simple Analysis
        if not result_df.empty:
            st.info(f"Total Students: {len(result_df)}")
            st.bar_chart(result_df.set_index('name')['marks'])

    # 3. DELETE STUDENT PAGE
    elif choice == "Delete Student":
        st.subheader("Delete Record")
        roll_to_delete = st.text_input("Enter Roll Number to Delete")
        if st.button("Delete"):
            delete_student(roll_to_delete)

if __name__ == '__main__':
    main()