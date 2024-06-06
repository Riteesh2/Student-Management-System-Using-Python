'''student management system project in python using tkinter and mysql'''

from functools import partial
from tkinter import *
from tkinter import messagebox
import pymysql
import custom as cs
import credentials as cr

class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Student Management System")
        self.window.geometry("1000x460")
        self.window.config(bg = "white")

        # Customization
        self.color_1 = cs.color_1
        self.color_2 = cs.color_2
        self.color_3 = cs.color_3
        self.color_4 = cs.color_4
        self.font_1 = cs.font_1
        self.font_2 = cs.font_2

        # User Credentials
        self.host = cr.host
        self.user = cr.user
        self.password = cr.password
        self.database = cr.database

        # Left Frame
        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=0, width=540, relheight = 1)

        # Right Frame
        self.frame_2 = Frame(self.window, bg = self.color_2)
        self.frame_2.place(x=540,y=0,relwidth=1, relheight=1)
        
        # Labels 
        self.getInfo = Label(self.frame_2, text="STUDENTS", font=(self.font_2, 12, "bold"), bg=self.color_2).place(x=40,y=20)
        self.getInfo = Label(self.frame_2, text="MARKS", font=(self.font_2, 12, "bold"), bg=self.color_2).place(x=198,y=20)
        self.getInfo = Label(self.frame_2, text="RANKS", font=(self.font_2, 12, "bold"), bg=self.color_2).place(x=332,y=20)

        # Buttons       
        self.add_bt = Button(self.frame_2, text='ADD STUDENT', font=(self.font_1, 7), bd=2, command=self.AddStudent, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=40,y=60,width=100)
        
        self.view_bt = Button(self.frame_2, text='VIEW STUDENT', font=(self.font_1, 7), bd=2, command=self.ViewStudent, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=40,y=120,width=100)
        
        self.update_bt = Button(self.frame_2, text='UPDATE STUDENT', font=(self.font_1, 7), bd=2, command=self.UpdateStudent, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=40,y=180,width=100)
        
        self.delete_bt = Button(self.frame_2, text='DELETE STUDENT', font=(self.font_1, 7), bd=2, command=self.DeleteStudent,cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=40,y=240,width=100)
        
        self.addmarks_bt = Button(self.frame_2, text='ADD MARKS', font=(self.font_1, 7), bd=2, command=self.AddStudentMark, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=180,y=60,width=100)
        
        self.viewmarks_bt = Button(self.frame_2, text='VIEW MARKS', font=(self.font_1, 7), bd=2, command=self.ViewStudentMark, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=180,y=120,width=100)
        
        self.updatemarks_bt = Button(self.frame_2, text='UPDATE MARKS', font=(self.font_1, 7), bd=2, command=self.UpdateStudentMark, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=180,y=180,width=100)
        
        self.classmarks_bt = Button(self.frame_2, text='VIEW CLASS MARKS', font=(self.font_1, 7), bd=2, command=self.ViewAllMarks, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=180,y=240,width=100)
        
        self.generateranks_bt = Button(self.frame_2, text='GENERATE RANKS', font=(self.font_1, 7), bd=2, command=self.GenerateRanks, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=320,y=60,width=100)
        
        self.viewallranks_bt = Button(self.frame_2, text='VIEW ALL RANKS', font=(self.font_1, 7), bd=2, command=self.ViewAllRanks, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=320,y=120,width=100)
        
        self.view3ranks_bt = Button(self.frame_2, text='VIEW TOP3 RANKS', font=(self.font_1, 7), bd=2, command=self.ViewTopRanks, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=320,y=180,width=100)
        
        self.clear_bt = Button(self.frame_2, text='CLEAR FORM', font=(self.font_1, 7), bd=2, command=self.ClearScreen, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=110,y=300,width=100)
        
        self.exit_bt = Button(self.frame_2, text='EXIT', font=(self.font_1, 7), bd=2, command=self.Exit, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=250,y=300,width=100)


    '''Widgets for adding student data'''
    def AddStudent(self):    
        self.ClearScreen()

        self.roll_no = Label(self.frame_1, text="ROLL NUMBER", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        self.roll_no_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.roll_no_entry.place(x=40,y=60, width=200)
        
        self.student_name = Label(self.frame_1, text="STUDENT NAME", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        self.student_name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.student_name_entry.place(x=300,y=60, width=200)
        
        self.group_name = Label(self.frame_1, text="GROUP NAME", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        self.group_name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.group_name_entry.place(x=40,y=130, width=200)

        self.date_of_birth = Label(self.frame_1, text="DATE OF BIRTH", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        self.date_of_birth_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.date_of_birth_entry.place(x=300,y=130, width=200)

        self.gender = Label(self.frame_1, text="GENDER", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.place(x=40,y=200, width=200)

        self.address = Label(self.frame_1, text="ADDRESS", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        self.address_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.address_entry.place(x=300,y=200, width=200)

        self.mobile_no = Label(self.frame_1, text="MOBILE NUMBER", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        self.mobile_no_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.mobile_no_entry.place(x=40,y=270, width=200)

        self.email = Label(self.frame_1, text="EMAIL", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.place(x=300,y=270, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='SUBMIT', font=(self.font_1, 12), bd=2, command=self.Submit, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=200,y=389,width=100)

    '''Widgets for adding student marks '''
    def AddStudentMark(self):
        self.ClearScreen()

        self.roll_no = Label(self.frame_1, text="ROLL NUMBER", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        self.roll_no_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.roll_no_entry.place(x=40,y=60, width=200)
        
        self.group_name = Label(self.frame_1, text="GROUP NAME", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        self.group_name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.group_name_entry.place(x=300,y=60, width=200)
        
        self.term = Label(self.frame_1, text="TERM", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        self.term_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.term_entry.place(x=40,y=130, width=200)

        self.english = Label(self.frame_1, text="ENGLISH", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        self.english_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.english_entry.place(x=300,y=130, width=200)

        self.mathematics = Label(self.frame_1, text="MATHEMATICS", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        self.mathematics_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.mathematics_entry.place(x=40,y=200, width=200)

        self.physics = Label(self.frame_1, text="PHYSICS", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        self.physics_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.physics_entry.place(x=300,y=200, width=200)

        self.chemistry = Label(self.frame_1, text="CHEMISTRY", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        self.chemistry_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.chemistry_entry.place(x=40,y=270, width=200)

        self.computer_science = Label(self.frame_1, text="COMPUTER SCIENCE", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        self.computer_science_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.computer_science_entry.place(x=300,y=270, width=200)
            
        self.submit_bt_1 = Button(self.frame_1, text='SUBMIT', font=(self.font_1, 12), bd=2, command=self.SubmitMarks, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=200,y=389,width=100)
        
    '''Submit the student form data to the database'''
    def SubmitMarks(self):
        if self.roll_no_entry.get() == "" or self.group_name_entry.get() == "" or self.term_entry.get() == "" or self.english_entry.get() == "" or self.mathematics_entry.get() == "" or self.physics_entry.get() == "" or self.chemistry_entry.get() == "" or self.computer_science_entry.get() == "" :
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from marks where roll_no=%s", self.roll_no_entry.get())
                row=curs.fetchone()
                total = int(self.english_entry.get()) + int(self.mathematics_entry.get()) + int(self.physics_entry.get()) + int(self.chemistry_entry.get()) + int(self.computer_science_entry.get())

                if row!=None:
                    messagebox.showerror("Error!","The Marks for the roll number is already exists, please try again with another roll number",parent=self.window)
                else:
                    curs.execute("insert into marks (roll_no,group_name,term,english,mathematics,physics,chemistry,computer_science, total) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (
                                            self.roll_no_entry.get(),
                                            self.group_name_entry.get(),
                                            self.term_entry.get(),
                                            self.english_entry.get(),
                                            self.mathematics_entry.get(),
                                            self.physics_entry.get(),
                                            self.chemistry_entry.get(),
                                            self.computer_science_entry.get(),
                                            total
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The mark details for the roll number has been submitted")
                    self.reset_marks_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    '''Reset all the marks entry fields'''
    def reset_marks_fields(self):
        self.roll_no_entry.delete(0, END)
        self.group_name_entry.delete(0, END)
        self.term_entry.delete(0, END)
        self.english_entry.delete(0, END)
        self.mathematics_entry.delete(0, END)
        self.physics_entry.delete(0, END)
        self.chemistry_entry.delete(0, END)
        self.computer_science_entry.delete(0, END)

    '''Widget to get the roll number to view the marks '''
    def ViewStudentMark(self):    
        self.ClearScreen()
        self.getInfo = Label(self.frame_1, text="Enter Roll Number", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=140,y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='SUBMIT', font=(self.font_1, 10), bd=2, command=self.ViewMarks, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220,y=150,width=80)
        
    '''Widgets for Viewing student marks '''
    def ViewMarks(self):    
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter correct roll number",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from marks where roll_no=%s", self.getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Mark details for the roll number doesn't exists",parent=self.window)
                else:
                    self.ShowMarkDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
                
    ''' This function will help to generate the ranks for all the students '''
    def GenerateRanks(self):   
        self.ClearScreen()
        
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = connection.cursor()
  
            curs.execute("DROP TABLE IF EXISTS RANKS")
            curs.execute("CREATE TABLE RANKS (ROLL_NO INT NOT NULL, STUDENT_NAME VARCHAR(30) NOT NULL, TOTAL INT NOT NULL, STUDENT_RANK VARCHAR(10) NOT NULL, PRIMARY KEY ( ROLL_NO ));")
            curs.execute("INSERT INTO RANKS(ROLL_NO, STUDENT_NAME, TOTAL, STUDENT_RANK) SELECT M.ROLL_NO, S.STUDENT_NAME, M.TOTAL, RANK() OVER (ORDER BY TOTAL DESC) FROM MARKS M, STUDENTS S WHERE S.ROLL_NO = M.ROLL_NO")
            connection.commit()
            connection.close()
            messagebox.showinfo('Done!', "The ranks for all the students generated successfully")
        except Exception as e:
            messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
   
    '''Widgets for viewing the student ranks '''
    def ViewAllRanks(self):   
        self.ClearScreen()
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = connection.cursor()
  
            curs.execute("SELECT * FROM RANKS WHERE STUDENT_RANK <= 15 ORDER BY STUDENT_RANK ASC")

            records = curs.fetchall();  
            if records == None:
                messagebox.showerror("Error!","Ranks not yet generated for the students. Please click Generate Ranks button",parent=self.window)
            else:
                e = Label(self.frame_1, width=15, text='ROLL NUMBER', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=0)
                e = Label(self.frame_1, width=15, text='STUDENT NAME', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=1)
                e = Label(self.frame_1, width=15, text='TOTAL MARKS', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=2)
                e = Label(self.frame_1, width=15, text='RANK', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=3)
                i=1
                for rank in records: 
                    for j in range(len(rank)):
                        e = Label(self.frame_1, width=15, text=rank[j], borderwidth=2, relief='ridge', anchor="w") 
                        e.place(x=163, y=110, width=200, height=30)
                        e.grid(row=i, column=j) 
                    i=i+1
                    print()# line break at the end of one row
                #self.window.mainloop()
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)   

    '''Widgets for viewing the student ranks '''
    def ViewTopRanks(self):   
        self.ClearScreen()
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = connection.cursor()
  
            curs.execute("SELECT * FROM RANKS WHERE STUDENT_RANK <= 3 ORDER BY STUDENT_RANK ASC")

            records = curs.fetchall();  
            if records == None:
                messagebox.showerror("Error!","Ranks not yet generated for the students. Please click Generate Ranks button",parent=self.window)
            else:
                e = Label(self.frame_1, width=15, text='ROLL NUMBER', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=0)
                e = Label(self.frame_1, width=15, text='STUDENT NAME', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=1)
                e = Label(self.frame_1, width=15, text='TOTAL MARKS', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=2)
                e = Label(self.frame_1, width=15, text='RANK', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=3)
                i=1
                for rank in records: 
                    for j in range(len(rank)):
                        e = Label(self.frame_1, width=15, text=rank[j], borderwidth=2, relief='ridge', anchor="w") 
                        e.place(x=163, y=110, width=200, height=30)
                        e.grid(row=i, column=j) 
                    i=i+1
                    print()# line break at the end of one row
                #self.window.mainloop()
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    '''Widgets for viewing the student ranks '''
    def ViewAllMarks(self):   
        self.ClearScreen()
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = connection.cursor()
  
            curs.execute("SELECT M.ROLL_NO, S.STUDENT_NAME, M.ENGLISH, M.MATHEMATICS, M.PHYSICS, M.CHEMISTRY, M.COMPUTER_SCIENCE, M.TOTAL FROM MARKS M, STUDENTS S WHERE M.ROLL_NO = S.ROLL_NO ORDER BY ROLL_NO")

            records = curs.fetchall();  
            if records == None:
                messagebox.showerror("Error!","Marks details not updated to the database",parent=self.window)
            else:
                e = Label(self.frame_1, width=8, text='ROLL NO', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=0)
                e = Label(self.frame_1, width=8, text='STUD NAME', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=1)
                e = Label(self.frame_1, width=8, text='ENG', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=2)
                e = Label(self.frame_1, width=8, text='MAT', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=3)
                e = Label(self.frame_1, width=8, text='PHY', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=4)
                e = Label(self.frame_1, width=8, text='CHE', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=5)
                e = Label(self.frame_1, width=8, text='CS', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=6)
                e = Label(self.frame_1, width=8, text='TOTAL', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0,column=7)
                i=1
                for mark in records: 
                    for j in range(len(mark)):
                        e = Label(self.frame_1, width=8, text=mark[j], borderwidth=2, relief='ridge', anchor="w") 
                        e.grid(row=i, column=j) 
                    i=i+1
                    print()# line break at the end of one row
                #self.window.mainloop()
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
       
    '''Within frame 1, it displays information about a student mark details'''
    def ShowMarkDetails(self, row):
        self.ClearScreen()
       
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = connection.cursor()
            curs.execute("select * from students where roll_no=%s", row[1])
            stud=curs.fetchone()
            
            if stud == None:
                messagebox.showerror("Error!","Student details for the roll number doesn't exists",parent=self.window)
            else:
                student_name = Label(self.frame_1, text="STUDENT NAME", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=30)
                student_name_data = Label(self.frame_1, text=stud[1], font=(self.font_1, 10)).place(x=40, y=60)
        except Exception as e:
            messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
            
        roll_no = Label(self.frame_1, text="ROLL NUMBER", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        roll_no_data = Label(self.frame_1, text=row[1], font=(self.font_1, 10)).place(x=300, y=60)
        
        group_name = Label(self.frame_1, text="GROUP NAME", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        group_name_data = Label(self.frame_1, text=row[2], font=(self.font_1, 10)).place(x=40, y=130)

        term = Label(self.frame_1, text="TERM", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        term_data = Label(self.frame_1, text=row[3], font=(self.font_1, 10)).place(x=300, y=130)

        english = Label(self.frame_1, text="ENGLISH", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        english_data = Label(self.frame_1, text=row[4], font=(self.font_1, 10)).place(x=40, y=200)

        mathematics = Label(self.frame_1, text="MATHEMATICS", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        mathematics_data = Label(self.frame_1, text=row[5], font=(self.font_1, 10)).place(x=300, y=200)

        physics = Label(self.frame_1, text="PHYSICS", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        physics_data = Label(self.frame_1, text=row[6], font=(self.font_1, 10)).place(x=40, y=270)

        chemistry = Label(self.frame_1, text="CHEMISTRY", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        chemistry_data = Label(self.frame_1, text=row[7], font=(self.font_1, 10)).place(x=300, y=270)

        computer_science = Label(self.frame_1, text="COMPUTER SCIENCE", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=310)
        computer_science_data = Label(self.frame_1, text=row[8], font=(self.font_1, 10)).place(x=40, y=340)
        
        total = Label(self.frame_1, text="TOTAL", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=310)
        total_data = Label(self.frame_1, text=row[9], font=(self.font_1, 10)).place(x=300, y=340)

    '''To update a student mark details, get the student id'''
    def UpdateStudentMark(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Roll Number", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=140,y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='SUBMIT', font=(self.font_1, 10), bd=2, command=self.UpdateMarks, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220,y=150,width=80)
     
    ''' Update the student marks information to the database '''
    def UpdateMarks(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter correct roll number",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from marks where roll_no=%s", self.getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Mark details doesn't exists for this roll number",parent=self.window)
                else:
                    self.UpdateMarkDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    ''' Update the student marks information to the database '''
    def UpdateMarkDetails(self, row):
        self.ClearScreen()
        
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = connection.cursor()
            curs.execute("select * from students where roll_no=%s", row[1])
            stud=curs.fetchone()
            
            if stud == None:
                messagebox.showerror("Error!","Student details for the roll number doesn't exists",parent=self.window)
            else:
                student_name = Label(self.frame_1, text="STUDENT NAME", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=30)
                student_name_data = Label(self.frame_1, text=stud[1], font=(self.font_1, 10)).place(x=40, y=60)
        except Exception as e:
            messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
      
        self.roll_no = Label(self.frame_1, text="ROLL NUMBER", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        roll_no_data = Label(self.frame_1, text=row[1], font=(self.font_1, 10)).place(x=300, y=60)
           
        self.group_name = Label(self.frame_1, text="GROUP NAME", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        group_name_data = Label(self.frame_1, text=row[2], font=(self.font_1, 10)).place(x=40, y=130)

        self.term = Label(self.frame_1, text="TERM", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        self.term_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.term_entry.insert(0, row[3])
        self.term_entry.place(x=300,y=130, width=200)

        self.english = Label(self.frame_1, text="ENGLISH", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        self.english_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.english_entry.insert(0, row[4])
        self.english_entry.place(x=40,y=200, width=200)
        
        self.mathematics = Label(self.frame_1, text="MATHEMATICS", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        self.mathematics_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.mathematics_entry.insert(0, row[5])
        self.mathematics_entry.place(x=300,y=200, width=200)

        self.physics = Label(self.frame_1, text="PHYSICS", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        self.physics_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.physics_entry.insert(0, row[6])
        self.physics_entry.place(x=40,y=270, width=200)

        self.chemistry = Label(self.frame_1, text="CHEMISTRY", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        self.chemistry_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.chemistry_entry.insert(0, row[7])
        self.chemistry_entry.place(x=300,y=270, width=200)

        self.computer_science = Label(self.frame_1, text="COMPUTER SCIENCE", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=310)
        self.computer_science_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.computer_science_entry.insert(0, row[8])
        self.computer_science_entry.place(x=40,y=340, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='SUBMIT', font=(self.font_1, 12), bd=2, command=partial(self.UpdateMarkDetailsToDB, row), cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=160,y=389,width=100)
        
        self.cancel_bt = Button(self.frame_1, text='CANCEL', font=(self.font_1, 12), bd=2, command=self.ClearScreen, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=280,y=389,width=100)
        
        
    '''Updates student mark data to the database'''
    def UpdateMarkDetailsToDB(self, row):
        if self.term_entry.get() == "" or self.english_entry.get() == "" or self.mathematics_entry.get() == "" or self.physics_entry.get() == "" or self.chemistry_entry.get() == "" or self.computer_science_entry.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from marks where roll_no=%s", row[1])
                row=curs.fetchone()
                
                total = int(self.english_entry.get()) + int(self.mathematics_entry.get()) + int(self.physics_entry.get()) + int(self.chemistry_entry.get()) + int(self.computer_science_entry.get())

                if row==None:
                    messagebox.showerror("Error!","The mark details for the roll number doesn't exists",parent=self.window)
                else:
                    curs.execute("update marks set term=%s, english=%s, mathematics=%s, physics=%s, chemistry=%s, computer_science=%s, total=%s where roll_no=%s",
                                        (
                                            self.term_entry.get(),
                                            self.english_entry.get(),
                                            self.mathematics_entry.get(),
                                            self.physics_entry.get(),
                                            self.chemistry_entry.get(),
                                            self.computer_science_entry.get(),
                                            total,
                                            row[1]
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The mark details for the roll number has been updated")
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
        

    '''Get the roll number to view student details'''
    def ViewStudent(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Roll Number", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=140,y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='SUBMIT', font=(self.font_1, 10), bd=2, command=self.Student_View, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220,y=150,width=80)
            
    '''To update a student details, get the roll number '''
    def UpdateStudent(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Roll Number", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=140,y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='SUBMIT', font=(self.font_1, 10), bd=2, command=self.Student_Update, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220,y=150,width=80)

    '''Get the roll number to delete a student record'''
    def DeleteStudent(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Roll Number", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=140,y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='SUBMIT', font=(self.font_1, 10), bd=2, command=self.DeleteData, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220,y=150,width=80)

    '''Remove all widgets from the frame 1'''
    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    '''Exit window'''
    def Exit(self):
        self.window.destroy()

    ''' View the student details based on the roll number entered '''
    def Student_View(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter correct roll number",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from students where roll_no=%s", self.getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Roll Number doesn't exists",parent=self.window)
                else:
                    self.ShowDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)


    ''' Update student details based on the roll number '''
    def Student_Update(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter correct roll number",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from students where roll_no=%s", self.getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Roll number doesn't exists",parent=self.window)
                else:
                    self.GetUpdateDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
   
    '''Delete student data based on the roll number'''
    def DeleteData(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter Roll number",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from students where roll_no=%s", self.getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Roll number doesn't exists",parent=self.window)
                else:
                    curs.execute("delete from students where roll_no=%s", self.getInfo_entry.get())
                    connection.commit()
                    messagebox.showinfo('Done!', "The student details has been deleted")
                    connection.close()
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)


    '''Gets the data that the user wants to update to perform the update operation'''
    def GetUpdateDetails(self, row):
        self.ClearScreen()

        self.roll_no = Label(self.frame_1, text="ROLL NUMBER", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        self.roll_no_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.roll_no_entry.insert(0, row[0])
        self.roll_no_entry.place(x=40,y=60, width=200)
        
        self.student_name = Label(self.frame_1, text="STUDENT NAME", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        self.student_name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.student_name_entry.insert(0, row[1])
        self.student_name_entry.place(x=300,y=60, width=200)
        
        self.group_name = Label(self.frame_1, text="GROUP NAME", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        self.group_name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.group_name_entry.insert(0, row[2])
        self.group_name_entry.place(x=40,y=130, width=200)

        self.date_of_birth = Label(self.frame_1, text="DATE OF BIRTH", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        self.date_of_birth_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.date_of_birth_entry.insert(0, row[3])
        self.date_of_birth_entry.place(x=300,y=130, width=200)

        self.gender = Label(self.frame_1, text="GENDER", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.insert(0, row[4])
        self.gender_entry.place(x=40,y=200, width=200)

        self.address = Label(self.frame_1, text="ADDRESS", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        self.address_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.address_entry.insert(0, row[5])
        self.address_entry.place(x=300,y=200, width=200)

        self.mobile_no = Label(self.frame_1, text="MOBILE_NO", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        self.mobile_no_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.mobile_no_entry.insert(0, row[6])
        self.mobile_no_entry.place(x=40,y=270, width=200)

        self.email = Label(self.frame_1, text="EMAIL", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.insert(0, row[7])
        self.email_entry.place(x=300,y=270, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='SUBMIT', font=(self.font_1, 12), bd=2, command=partial(self.UpdateDetails, row), cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=160,y=389,width=100)
        
        self.cancel_bt = Button(self.frame_1, text='CANCEL', font=(self.font_1, 12), bd=2, command=self.ClearScreen, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=280,y=389,width=100)

    
    '''Within frame 1, it displays information about a student'''
    def ShowDetails(self, row):
        self.ClearScreen()
        roll_no = Label(self.frame_1, text="ROLL NUMBER", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        roll_no_data = Label(self.frame_1, text=row[0], font=(self.font_1, 10)).place(x=40, y=60)
        
        student_name = Label(self.frame_1, text="STUDENT NAME", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        student_name_data = Label(self.frame_1, text=row[1], font=(self.font_1, 10)).place(x=300, y=60)
        
        group_name = Label(self.frame_1, text="GROUP NAME", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        group_name_data = Label(self.frame_1, text=row[2], font=(self.font_1, 10)).place(x=40, y=130)

        date_of_birth = Label(self.frame_1, text="DATE OF BIRTH", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        date_of_birth_data = Label(self.frame_1, text=row[3], font=(self.font_1, 10)).place(x=300, y=130)

        gender = Label(self.frame_1, text="GENDER", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        gender_data = Label(self.frame_1, text=row[4], font=(self.font_1, 10)).place(x=40, y=200)

        address = Label(self.frame_1, text="ADDRESS", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        address_data = Label(self.frame_1, text=row[5], font=(self.font_1, 10)).place(x=300, y=200)

        mobile_no = Label(self.frame_1, text="MOBILE NO", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        mobile_no_data = Label(self.frame_1, text=row[6], font=(self.font_1, 10)).place(x=40, y=270)

        email = Label(self.frame_1, text="EMAIL", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        email_data = Label(self.frame_1, text=row[7], font=(self.font_1, 10)).place(x=300, y=270)
   

    '''Updates student data'''
    def UpdateDetails(self, row):
        if self.roll_no_entry.get() == "" or self.student_name_entry.get() == ""  or self.group_name_entry.get() == "" or self.date_of_birth_entry.get() == "" or self.gender_entry.get() == "" or self.address_entry.get() == "" or self.mobile_no_entry.get() == "" or self.email_entry.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from students where roll_no=%s", self.roll_no_entry.get())
                row=curs.fetchone()

                if row==None:
                    messagebox.showerror("Error!","The roll number doesn't exists",parent=self.window)
                else:
                    curs.execute("update students set student_name=%s,group_name= %s,date_of_birth=%s, gender=%s, address=%s, mobile_no=%s, email=%s where roll_no=%s",
                                        (
                                            self.student_name_entry.get(),
                                            self.group_name_entry.get(),
                                            self.date_of_birth_entry.get(),
                                            self.gender_entry.get(),
                                            self.address_entry.get(),
                                            self.mobile_no_entry.get(),
                                            self.email_entry.get(),
                                            self.roll_no_entry.get()
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The student details has been updated")
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
       
    '''It adds the information of new students'''
    def Submit(self):
        if self.roll_no_entry.get() == "" or self.student_name_entry.get() == "" or self.group_name_entry.get() == "" or self.date_of_birth_entry.get() == "" or self.gender_entry.get() == "" or self.address_entry.get() == "" or self.mobile_no_entry.get() == "" or self.email_entry.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from students where roll_no=%s", self.roll_no_entry.get())
                row=curs.fetchone()

                if row!=None:
                    messagebox.showerror("Error!","The Student Roll No is already exists, please try again with another number",parent=self.window)
                else:
                    curs.execute("insert into students (roll_no,student_name,group_name,date_of_birth,gender,address,mobile_no,email) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (
                                            self.roll_no_entry.get(),
                                            self.student_name_entry.get(),
                                            self.group_name_entry.get(),
                                            self.date_of_birth_entry.get(),
                                            self.gender_entry.get(),
                                            self.address_entry.get(),
                                            self.mobile_no_entry.get(),
                                            self.email_entry.get() 
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The Student details has been submitted")
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    '''Reset all the entry fields'''
    def reset_fields(self):
        self.roll_no_entry.delete(0, END)
        self.student_name_entry.delete(0, END)
        self.group_name_entry.delete(0, END)
        self.date_of_birth_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.mobile_no_entry.delete(0, END)
        self.email_entry.delete(0, END)

# The main function
if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()
