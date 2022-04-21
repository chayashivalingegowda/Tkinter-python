#FrontEnd

from doctest import master
from tkinter import *
import tkinter.messagebox
import projectbackend

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("GEMS Dubai International School")
        self.root.config(bg="snow3")
        self.root.geometry("1350x720+0+0")

        StdID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Dob = StringVar()
        # =============================================================Functions===============================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("GEMS Dubai International School","Do you want to Exit the program?")
            if iExit>0:
                root.destroy()
                return


        def Stdrec(event):
            global sd
            searchstd = studentlist.curselection()[0]
            sd = studentlist.get(searchstd)


        def cleardata():
            self.txtLna.delete(0, END)
            self.txtDob.delete(0, END)

        def addData():
            if(len(StdID.get())!=0):
                projectbackend.addStdRec(StdID.get(), Firstname.get() , Lastname.get() , Dob.get() )
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), Firstname.get() , Lastname.get() , Dob.get()))

        def DisplayData():
            studentlist.delete(0, END)
            for row in projectbackend.Viewdata():
                studentlist.insert(END,row,str(""))

        def deleteData():
            if(len(StdID.get())!=0):
                projectbackend.deletRec(sd[0])
                cleardata()
                DisplayData()

        def Searchdatabase():
            studentlist.delete(0,END)
            for row in projectbackend.searchdata(StdID.get(), Firstname.get() , Lastname.get() , Dob.get()):
                studentlist.insert(END, row, str(""))
        def UpdateDatabase():
            if(len(StdID.get())!=0):
                projectbackend.deletRec(sd[0])

            if (len(StdID.get()) != 0):
                projectbackend.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), Dob.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Lastname.get(), Dob.get()))




        #=============================================================FRAMES===================================================================

        MainFrame = Frame(self.root, bg="snow3")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, padx=0, pady=0, bg="snow3", relief=RIDGE)
        TitFrame.pack(side=TOP, padx=30, pady=30)


        self.lblTit = Label(TitFrame,font= ('arial',25,'bold'),text="GEMS Dubai International School", bg="snow")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, width=1200, height=90, padx=1, pady=1, bg="snow3" ,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=18, bg="snow3", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=500, height=500, padx=20, bg="aquamarine", relief=RIDGE,
                                   font=('arial',20,'bold'),text="Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=500, height=600, padx=20, bg="lightgoldenrod1", relief=RIDGE,
                                   font=('arial', 20, 'bold'), text="Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # ========================================================Labels and Entry Widget===================================================================
        options = [
        "School Bus",
        "Rental Vehichle",
        "Personal Vehichle",
        "By Walk",
        "Others"
        ]
        StdID.set("School Bus")
        
        self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mode Of Transport:", padx=1, pady=1, bg="aquamarine")
        self.lblStdID.grid( row = 0, column = 0, sticky = W)
        self.txtStdID = OptionMenu( DataFrameLEFT, StdID, *options )
        # self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1, padx=0, pady=30)


        self.lblFna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Entry Gate: ", padx=2, pady=2, bg="aquamarine")
        self.lblFna.grid(row=1, column=0, sticky=W)
        Radiobutton(DataFrameLEFT, text = "Front Gate", variable = Firstname,value = "Front Gate", indicator = 0, background = "light blue").grid(row=1, column=1, padx=0, pady=30)
        Radiobutton(DataFrameLEFT, text = "Back Gate", variable = Firstname,value = "Back Gate", indicator = 0, background = "light blue").grid(row=2, column=1, padx=0, pady=30)


        self.lblLna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Arrival Time at Entry Gate: ", padx=2, pady=2,
                            bg="aquamarine")
        self.lblLna.grid(row=3, column=0, sticky=W)
        self.txtLna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Lastname, width=19)
        self.txtLna.grid(row=3, column=1, padx=80, pady=30)


        self.lblDob = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Waiting Time: ", padx=2, pady=2,
                            bg="aquamarine")
        self.lblDob.grid(row=5, column=0, sticky=W)
        self.txtDob = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Dob, width=19)
        self.txtDob.grid(row=5, column=1, padx=80, pady=30)


        
        # ========================================================ScrollBar and ListBox===================================================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width = 41 ,height = 22 , font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',Stdrec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config( command = studentlist.yview)

        # ========================================================Button Widget===================================================================
        self.btnAddData = Button(ButtonFrame, text="Add new", font= ('arial',12,'bold') , fg="white", bg="grey", width = 10 ,height = 1, bd=4, command = addData)
        self.btnAddData.grid(row=0, column=0, padx=10, pady=10)

        self.btnDispay = Button(ButtonFrame, text="Display", font=('arial', 12, 'bold'), fg="white", bg="grey",width=10, height=1, bd=4, command = DisplayData)
        self.btnDispay.grid(row=0, column=1, padx=10, pady=10)

        self.btnClear = Button(ButtonFrame, text="Clear", font=('arial', 12, 'bold'),fg="white", bg="grey", width=10, height=1, bd=4, command=cleardata)
        self.btnClear.grid(row=0, column=2, padx=10, pady=10)

        self.btnDelete = Button(ButtonFrame, text="Delete", font=('arial', 12, 'bold'), fg="white", bg="grey",width=10, height=1, bd=4, command =deleteData)
        self.btnDelete.grid(row=0, column=3, padx=10, pady=10)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 12, 'bold'), fg="white", bg="grey", width=10, height=1, bd=4 , command=iExit)
        self.btnExit.grid(row=0, column=6, padx=10, pady=10)

if __name__ =='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()







