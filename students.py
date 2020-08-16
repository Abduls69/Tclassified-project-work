from tkinter import *
from tkinter import ttk
import sqlite3

class StudentDB:

    
    # will hold the database connection
    db_conn = 0
    # A Cursor is used to traverse the records of a result
    theCursor = 0
    # will store the current student selected
    curr_student = 0

    # set up the database
    def setup_db(self):
        # open or create a database
        self.db_conn = sqlite3.connect('student.db')
        # The cursor traverses the records
        self.theCursor = self.db_conn.cursor()
        # create the table if it dosn't exist
        try:
            self.db_conn.execute("CREATE TABLE if not exists Students(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, fName TEXT NOT NULL, lName TEXT NOT NULL);")
            self.db_conn.commit()
        except sqlite3.OperationalError:
            print("Error : Table not Created")

    # Submit button function
    def stud_submit(self):
        # Insert students in the database
        self.db_conn.execute("INSERT INTO Students (FName, LName) " + "VALUES ('" + self.fn_entry_value.get() + "', '" + self.ln_entry_value.get() + "')")

        # Clear the entry boxes
        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")

        # Update the Listbox with the students list
        self.update_listbox()

    def update_listbox(self):
        # Delete items in the listbox
        self.list_box.delete(0, END)

        # Get the students from the database
        try:
            result = self.theCursor.execute("SELECT ID, FName, LName FROM Students")
            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]

                # Put the students in the list box
                self.list_box.insert(stud_id, stud_fname + " " + stud_lname)

        except sqlite3.OperationalError:
            print("The Table Dosnt Exist")

        except:
            print("1: Couldnt Retrieve data from database")

    # Load listbox selected student into the entrie(textbox)
    def load_student(self, event = None):
        # Get index selected which is the student id
        lb_widget = event.widget
        index = str(lb_widget.curselection() [0] + 1)

        # Store the current student index
        self.curr_student = index

        # Retrieve student List from the database
        try:
            result = self.theCursor.execute("SELECT ID, FName, LName FROM Students WHERE ID = " + index)
            # you recieve a list of lists that hold the result
            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]

                # Set values in the entries
                self.fn_entry_value.set(stud_fname)
                self.ln_entry_value.set(stud_lname)

        except sqlite3.OperationalError:
            print("The table dosnt Exist")

        except:
            print("2 : Couldnt retrieve data from the database")

    # Update student info
    def update_student(self, event = None):
        # Update student records with change made in entry
        try:
            self.db_conn.execute("UPDATE Students SET FName = '" + self.fn_entry_value.get() + "', LName = '" + self.ln_entry_value.get() + "' WHERE ID =" + self.curr_student)
            self.db_conn.commit()

        except sqlite3.OperationalError:
            print("Database couldnt not be updated")

        # Clear the entry boxes
        self.fn_entry.delete(0, "end")    
        self.ln_entry.delete(0, "end")

        # Update list box with student list
        self.update_listbox()
    
    def __init__(self, root):
        root.title('Student Management Database System')
        root.geometry('300x400')

        # Add widgets

        # First Row
        fn_label = Label(root, text = 'First Name')
        fn_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)

        self.fn_entry_value = StringVar(root, value = '')
        self.fn_entry = ttk.Entry(root, textvariable = self.fn_entry_value)
        self.fn_entry.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = W)

        # Second Row
        ln_label = Label(root, text = 'Second Name')
        ln_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)

        self.ln_entry_value = StringVar(root, value = '')
        self.ln_entry = ttk.Entry(root, textvariable = self.ln_entry_value)
        self.ln_entry.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = W)

        # Third Row
        self.submit_button = ttk.Button(root, text = 'Submit', command = lambda: self.stud_submit())
        self.submit_button.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)

        self.update_button = ttk.Button(root, text = 'Update', command = lambda: self.update_student())
        self.update_button.grid(row = 2, column = 1, padx = 10, pady = 10)

        
        # Fourth Row
        scrollbar = Scrollbar(root)
        self.list_box = Listbox(root)
        self.list_box.bind('<<ListboxSelect>>', self.load_student)

        self.list_box.insert(1, 'Students will appear Here')
        self.list_box.grid(row = 3, column = 0, columnspan = 4, padx = 10, pady = 10, sticky = W+E)

        # Call for the database to be created
        self.setup_db()

        # Update the Listbox with Students List
        self.update_listbox()

       




root = Tk()
studDB = StudentDB(root)
root.mainloop()