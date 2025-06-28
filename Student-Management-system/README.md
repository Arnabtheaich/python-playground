# Student Management System

This is a web-based Student Management System built using Python and Streamlit. It allows you to manage student records such as name, roll, and subject through an interactive user interface.

## Features

- Add new students
- View all student records in a table
- Search students by:
  - Name
  - Roll
  - Subject
- Edit and update student information
- Delete student records
- Data is saved persistently in `data.json`

## Technologies Used

- Python
- Streamlit
- Pandas
- JSON

## Live App

You can access the deployed application here:  
**[Student Management System - Live](https://python-playground-studentmanagementsystembyarnab.streamlit.app/)**

## Project Structure

```
Student-Management-systerm/
├── data.json              # Stores student data
├── requirements.txt       # Python dependencies
└── run.py                 # Main Streamlit application
```

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Arnabtheaich/python-playground.git
cd python-playground/Student-Management-systerm
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run run.py
```

## Author

Developed by [Arnabtheaich](https://github.com/Arnabtheaich)