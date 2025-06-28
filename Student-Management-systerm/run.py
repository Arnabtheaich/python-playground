import streamlit as st
import json
import pandas as pd
from pathlib import Path

DATA_FILE = "data.json"
students = []

# Load existing data
st.markdown(
    "<p style='font-size: 14px;'><a href='https://github.com/Arnabtheaich' target='_blank'>Creator's Github</a></p>",
    unsafe_allow_html=True
)
if Path(DATA_FILE).exists():
    with open(DATA_FILE, "r") as f:
        students = json.load(f)
    st.success(" Loaded previous data from data.json")
else:
    st.warning("⚠ No previous data found. Starting fresh.")

# Save updated data
def save_to_file():
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)
    st.success(" Data saved successfully.")

# Add new student
def add_new():
    st.subheader(" Add New Student")
    name = st.text_input("Enter name")
    roll = st.number_input("Enter roll", step=1, format="%d")
    subject = st.text_input("Enter subject")

    if st.button("Add Student"):
        if not name or not subject:
            st.error("Name and subject cannot be empty.")
            return
        for s in students:
            if s["roll"] == roll:
                st.error("Roll number already exists.")
                return
        students.append({"name": name, "roll": roll, "subject": subject})
        save_to_file()

# View all students
def show_all():
    st.subheader(" All Students")
    if students:
        df = pd.DataFrame(students)
        st.dataframe(df)
    else:
        st.info("No students in the system.")

# Search options
def search_students():
    st.subheader(" Search Students")
    search_type = st.radio("Search by", ["Name", "Roll", "Subject"])

    if search_type == "Name":
        name = st.text_input("Enter name")
        if name and st.button("Search"):
            result = [s for s in students if s["name"].lower() == name.lower()]
            if result:
                st.dataframe(pd.DataFrame(result))
            else:
                st.error("No student found.")
    elif search_type == "Roll":
        roll = st.number_input("Enter roll", step=1, format="%d")
        if st.button("Search"):
            result = [s for s in students if s["roll"] == roll]
            if result:
                st.dataframe(pd.DataFrame(result))
            else:
                st.error("No student found.")
    else:
        subject = st.text_input("Enter subject")
        if subject and st.button("Search"):
            result = [s for s in students if s["subject"].lower() == subject.lower()]
            if result:
                st.dataframe(pd.DataFrame(result))
            else:
                st.error("No student found.")

# Delete a student
def delete_student():
    st.subheader(" Delete Student")
    roll = st.number_input("Enter roll to delete", step=1, format="%d")
    if st.button("Delete"):
        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                save_to_file()
                st.success("Student deleted.")
                return
        st.error("No student found with this roll.")

# Edit student info
def edit_student():
    st.subheader(" Edit Student Info")
    roll = st.number_input("Enter roll to edit", step=1, format="%d")
    matching = [s for s in students if s["roll"] == roll]

    if matching:
        student = matching[0]
        new_name = st.text_input("New name", value=student["name"])
        new_subject = st.text_input("New subject", value=student["subject"])
        new_roll = st.number_input("New roll", value=student["roll"], step=1, format="%d")

        if st.button("Update"):
            student["name"] = new_name
            student["subject"] = new_subject
            student["roll"] = new_roll
            save_to_file()
            st.success("Student information updated.")
    else:
        st.info("Enter a valid roll to load existing student data.")

# Main menu (not in sidebar)
st.title("Student Management system by ARNAB")
menu = st.selectbox("Menu", ["Add Student", "Show All", "Search", "Edit", "Delete", "Exit"])

if menu == "Add Student":
    add_new()
elif menu == "Show All":
    show_all()
elif menu == "Search":
    search_students()
elif menu == "Edit":
    edit_student()
elif menu == "Delete":
    delete_student()
elif menu == "Exit":
    st.info("Thanks for using Arnab's Student Management System.")
