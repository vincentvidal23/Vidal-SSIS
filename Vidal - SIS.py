from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter.ttk as ttk
import csv
import os

# Define Variables
class Student:
    
    def __init__ (self,root):
        self.root = root
        blank_space = ""
        self.root.title(200 * blank_space + "Student Information System")
        self.root.geometry("1350x575+0+0")
        self.root.resizable(False,False)
        self.data = dict()
        self.temp = dict()
        self.filename = "Studentdata.csv"
        
        Student_First_Name = StringVar()
        Student_Middle_Initial = StringVar()
        Student_Last_Name = StringVar()
        Student_IDNumber = StringVar()
        Student_YearLevel = StringVar()
        Student_Gender = StringVar()
        Student_Course = StringVar()
        searchbar = StringVar()
        
        if not os.path.exists('Studentdata.csv'):
            with open('Studentdata.csv', mode='w') as csv_file:
                fieldnames = ["Student ID Number", "Last Name", "First Name", "Middle Initial","Gender", "Year Level", "Course"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
        
        else:
            with open('Studentdata.csv', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["Student ID Number"]] = {'Last Name': row["Last Name"], 'First Name': row["First Name"], 'Middle Initial': row["Middle Initial"], 'Gender': row["Gender"],'Year Level': row["Year Level"], 'Course': row["Course"]}
            self.temp = self.data.copy()
        
        
         
# Create Update Delete List (CRUDL)
        
        def iExit():
            iExit = tkinter.messagebox.askyesno(" Student Information System","Do you really want to exit?")
            if iExit > 0:
                root.destroy()
                return
            
        def addStudent():
            with open('Studentdata.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if Student_IDNumber.get()=="" or Student_First_Name.get()=="" or Student_Middle_Initial.get()=="" or Student_Last_Name.get()=="" or Student_YearLevel.get()=="":
                    tkinter.messagebox.showinfo("Student Information System","Fill in the information")
                else:
                    self.data[Student_IDNumber.get()] = {'Last Name': Student_Last_Name.get(), 'First Name': Student_First_Name.get(), 'Middle Initial': Student_Middle_Initial.get(), 'Gender': Student_Gender.get(),'Year Level': Student_YearLevel.get(), 'Course': Student_Course.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("Student Information System", "Student Added Successfully!")
                Clear()
                displayData()
                    
        
        def Clear():
            Student_IDNumber.set("")
            Student_First_Name.set("")
            Student_Middle_Initial.set("")
            Student_Last_Name.set("")
            Student_YearLevel.set("")
            Student_Gender.set("")
            Student_Course.set("")
        
        
        
        def displayData():
            tree.delete(*tree.get_children())
            with open('Studentdata.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    IDNumber=row['Student ID Number']
                    LastName=row['Last Name']
                    FirstName=row['First Name']
                    MiddleInitial=row['Middle Initial']
                    YearLevel=row['Year Level']
                    Course=row['Course']
                    Gender=row['Gender']
                    tree.insert("",END, values=(IDNumber, LastName, FirstName, MiddleInitial, Gender, YearLevel, Course))
                    
      
        
        def deleteData():
            if tree.focus()=="":
                tkinter.messagebox.showerror("Student Information System","Select a Student Record from the Table")
                return
            id_no = tree.item(tree.focus(),"values")[0]
            
            self.data.pop(id_no, None)
            self.saveData()
            tree.delete(tree.focus())
            tkinter.messagebox.showinfo("Student Information System","Student Record Deleted Successfully!")
            
        
        
        def searchData():
            if self.searchbar.get() in self.data:
                vals = list(self.data[self.searchbar.get()].values())
                tree.delete(*tree.get_children())
                tree.insert("",0, values=(self.searchbar.get(), vals[0],vals[1],vals[2],vals[3],vals[4],vals[5]))
            elif self.searchbar.get() == "":
                displayData()
            else:
                tkinter.messagebox.showerror("Student Information System","Student not found!")
                return
            
               
        
        def editData():
            if tree.focus() == "":
                tkinter.messagebox.showerror("Student Information System", "Select a Student Record from the Table")
                return
            values = tree.item(tree.focus(), "values")
            Student_IDNumber.set(values[0])
            Student_Last_Name.set(values[1])
            Student_First_Name.set(values[2])
            Student_Middle_Initial.set(values[3])
            Student_Gender.set(values[4])
            Student_YearLevel.set(values[5])
            Student_Course.set(values[6])
       
    
       
        def updateData():
            with open('Studentdata.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if Student_IDNumber.get()=="" or Student_First_Name.get()=="" or Student_Middle_Initial.get()=="" or Student_Last_Name.get()=="" or Student_YearLevel.get()=="":
                    tkinter.messagebox.showinfo("Student Information System","Select a Student Record from the Table")
                else:
                    self.data[Student_IDNumber.get()] = {'Last Name': Student_Last_Name.get(), 'First Name': Student_First_Name.get(), 'Middle Initial': Student_Middle_Initial.get(), 'Gender': Student_Gender.get(),'Year Level': Student_YearLevel.get(), 'Course': Student_Course.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("Student Information System", "Updated Successfully!")
                Clear()
                displayData()     

# FRAMES
        
        MainFrame = Frame(self.root, bd=7, width=1300, height=750, relief=RIDGE, bg="gray")
        MainFrame.grid()
        
        BotFrame = Frame(MainFrame,  width=1330, height=130, relief=RIDGE,bg="gray")
        BotFrame.grid(row=2, column=0)
        
        TitleFrame = Frame(MainFrame, bg="gray", width=1340, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        
        MidFrame = Frame(MainFrame, bd=5,bg="dark cyan", width=1340, height=450, relief=RIDGE)
        MidFrame.grid(row=1, column=0)
        
        SearchFrame = Frame(MainFrame, width = 1340, height = 100, relief = RIDGE)
        SearchFrame.grid(row =3, column =0)
        
        RightFrame = Frame(MidFrame, bd=5, width=1350, height=400, padx=2, bg="cyan", relief=RIDGE)
        RightFrame.pack(side=RIGHT)

        LeftFrame = Frame(MidFrame, bd=5, width=600, height=400, padx=2, bg="cyan", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        
        RightFrame1 = Frame(RightFrame, bd=5,bg="green", width=600, height=300, padx=2, pady=4, relief=RIDGE)
        RightFrame1.pack(side=TOP, padx=0, pady=0)
        
        
        
# Title
        
        self.lblTitle = Label(TitleFrame, font=('Comic Sans MS',40,'bold'), text="STUDENT MANAGEMENT SYSTEM",bg="gray",fg="cyan",bd=7)
        self.lblTitle.grid(row=0, column=0, padx=135)
        

# Variables in GUI        
        
        self.lblStudentID = Label(RightFrame1, font=('Courier',12,'bold'), text="STUDENT ID:",bg="green", bd=5 , anchor=W)
        self.lblStudentID.grid(row=0, column=0, sticky=W, padx=5)
        self.txtStudentID = Entry(RightFrame1, font=('Times',12,'bold'), width=40, justify='left', textvariable = Student_IDNumber)
        self.txtStudentID.grid(row=0, column=1)
        
        self.lblLastName = Label(RightFrame1, font=('Courier',12,'bold'), text="LAST NAME:",bg="green",bd=7, anchor=W)
        self.lblLastName.grid(row=1, column=0, sticky=W, padx=5)
        self.txtLastName = Entry(RightFrame1, font=('Times',12,'bold'), width=40, justify='left', textvariable = Student_Last_Name)
        self.txtLastName.grid(row=1, column=1)
        
        self.lblFirstName = Label(RightFrame1, font=('Courier',12,'bold'), text="FIRST NAME:",bg="green", bd=7, anchor=W)
        self.lblFirstName.grid(row=2, column=0, sticky=W, padx=5)
        self.txtFirstName = Entry(RightFrame1, font=('Times',12,'bold'), width=40, justify='left', textvariable = Student_First_Name)
        self.txtFirstName.grid(row=2, column=1)
        
        self.lblMiddleInitial = Label(RightFrame1, font=('Courier',12,'bold'), text="MIDDLE INITIAL:", bg="green",bd=7, anchor=W)
        self.lblMiddleInitial.grid(row=3, column=0, sticky=W, padx=5)
        self.txtMiddleInitial = Entry(RightFrame1, font=('Times',12,'bold'), width=40, justify='left', textvariable = Student_Middle_Initial)
        self.txtMiddleInitial.grid(row=3, column=1)
        
        self.lblCourse = Label(RightFrame1, font=('Courier',12,'bold'), text="COURSE:",bg="green", bd=7, anchor=W)
        self.lblCourse.grid(row=4, column=0, sticky=W, padx=5)
        self.txtCourse = Entry(RightFrame1, font=('Times',12,'bold'), width=40, justify='left', textvariable = Student_Course)
        self.txtCourse.grid(row=4, column=1)
        
        self.lblGender = Label(RightFrame1, font=('Courier',12,'bold'), text="GENDER:", bg="green",bd=7, anchor=W)
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5)
        
        self.cboGender = ttk.Combobox(RightFrame1, font=('Courier',12,'bold'), state='readonly', width=39, textvariable = Student_Gender)
        self.cboGender['values'] = ('Female', 'Male')
        self.cboGender.grid(row=5, column=1)
        
        self.lblYearLevel = Label(RightFrame1, font=('Courier',12,'bold'), text="YEAR LEVEL:", bg="green",bd=7, anchor=W)
        self.lblYearLevel.grid(row=6, column=0, sticky=W, padx=5)
        
        self.cboYearLevel = ttk.Combobox(RightFrame1, font=('Courier',12,'bold'), state='readonly', width=39, textvariable = Student_YearLevel)
        self.cboYearLevel['values'] = ('1st Year', '2nd Year', '3rd Year', '4th Year')
        self.cboYearLevel.grid(row=6, column=1)
        
        self.searchbar = Entry(self.root, font=('Courier',12,'bold'), textvariable = searchbar, width = 29 )
        self.searchbar.place(x=880,y=108)
        
        
        
# GUI Buttons
        
        self.btnAddNew=Button(self.root, pady=1,bd=4,font=('Courier',16,'bold'), padx=12, width=8,fg="green", text='ADD', command=addStudent)
        self.btnAddNew.place(x=80,y=480)
        
        self.btnClear=Button(self.root, pady=1,bd=4,font=('Courier',16,'bold'), padx=2, width=8,fg="green", text='CLEAR', command=Clear)
        self.btnClear.place(x=250,y=480)
        
        self.btnUpdate=Button(self.root, pady=1,bd=4,font=('Courier',16,'bold'), padx=2, width=8,fg="green", text='UPDATE', command=updateData)
        self.btnUpdate.place(x=400,y=480)

        self.btnEdit=Button(self.root, pady=1,bd=4,font=('Courier',16,'bold'), padx=2, width=8,fg="green", text='EDIT', command = editData)
        self.btnEdit.place(x=550,y=480)

        self.btnDisplay=Button(self.root, pady=1,bd=4, font=('Courier', 16, 'bold'),padx=2,width=8, fg="green",text="DISPLAY" , command=displayData)
        self.btnDisplay.place(x=700,y=480)

        self.btnDelete=Button(self.root, pady=1,bd=4,font=('Courier',16,'bold'), padx=2, width=8,fg="red", text='DELETE',command = deleteData)
        self.btnDelete.place(x=850,y=480)

        self.btnExit=Button(self.root, pady=1,bd=4,font=('Courier',16,'bold'), padx=2, width=8,fg="red",bg="gray", text='EXIT',command = iExit)
        self.btnExit.place(x=1150,y=480)

        self.btnSearch=Button(self.root, pady=1,bd=4,font=('Courier',9,'bold'), padx=2, width=13, text='Search by ID:',fg="cyan",bg="gray", command = searchData)
        self.btnSearch.place(x=770,y=104)

        
        
# Tree View

        scroll_y=Scrollbar(LeftFrame, orient=VERTICAL)
        
        tree = ttk.Treeview(LeftFrame, height=15, columns=("Student ID Number", "Last Name", "First Name", "Middle Initial", "Gender", "Year Level", "Course"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_y.config(command=tree.yview)

        tree.heading("Student ID Number", text="Student ID Number")
        tree.heading("Last Name", text="Last Name")
        tree.heading("First Name", text="First Name")
        tree.heading("Middle Initial", text="Middle Initial")
        tree.heading("Gender", text="Gender")
        tree.heading("Year Level", text="Year Level")
        tree.heading("Course", text="Course")
        tree['show'] = 'headings'

        tree.column("Student ID Number", width=120)
        tree.column("Last Name", width=100)
        tree.column("First Name", width=100)
        tree.column("Middle Initial", width=100)
        tree.column("Gender", width=70)
        tree.column("Year Level", width=70)
        tree.column("Course", width=80)
        tree.pack(fill=BOTH,expand=1)
        
        displayData()

# Saving the Data to csv
    def saveData(self):
        temps = []
        with open('Studentdata.csv', "w", newline ='') as update:
            fieldnames = ["Student ID Number","Last Name","First Name","Middle Initial","Gender","Year Level","Course"]
            writer = csv.DictWriter(update, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp ={"Student ID Number": id}
                for key, value in val.items():
                    temp[key] = value
                temps.append(temp)
            writer.writerows(temps)
            

if __name__ =='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()

