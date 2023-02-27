import qrcode
from tkinter import*
from PIL import Image,ImageTk
from resizeimage import resizeimage

class QR_generator:
    def __init__(self,root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("zeno")
        self.message=Message

        title = Label(self.root,text="Qr Generator",font=("title new roman",40),bg="#053246",fg="white",anchor="w").place(x=0,y=0,relwidth=1)

        self.var_emp_code =StringVar()
        self.var_name =StringVar()
        self.var_depertment =StringVar()
        self.var_designation =StringVar()

        emp_Frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)

        emp_title = Label(emp_Frame,text="Employee Detail",font=("goudy old style  ",20),bg="#043256",fg="white").place(x=0,y=0,relwidth=1)

        lbl_emp_code = Label(emp_Frame,text="Employee ID",font=("times new roman",15,'bold'),bg="white").place(x=20,y=60)
        
        lbl_emp_code= Label(emp_Frame,text="Name",       font=("times new roman",15,'bold'),bg="white").place(x=20,y=100)
        lbl_emp_code= Label(emp_Frame,text="Department", font=("times new roman",15,'bold'),bg="white").place(x=20,y=140)
        lbl_emp_code= Label(emp_Frame,text="Designation",font=("times new roman",15,'bold'),bg="white").place(x=20,y=180)

        txt_emp_code = Entry(emp_Frame,font=("times new roman",15,),textvariable=self.var_emp_code,bg="lightyellow").place(x=200,y=60)
        txt_emp_code= Entry(emp_Frame ,font=("times new roman",15,),textvariable=self.var_name,bg="lightyellow").place(x=200,y=100)
        txt_emp_code= Entry(emp_Frame ,font=("times new roman",15,),textvariable=self.var_depertment,bg="lightyellow").place(x=200,y=140)
        txt_emp_code= Entry(emp_Frame,font=("times new roman",15,),textvariable=self.var_designation,bg="lightyellow").place(x=200,y=180)

        btn_generator=Button(lbl_emp_code,text='QR Generate',command=self.generate,font=("times in roman",18,'bold'),bg ='#2196f3',fg='white').place(x=90,y=350,width=180,height=30)
        btn_clear=Button(lbl_emp_code,text='Clear',command=self.clear,font=("times in roman",18,'bold'),bg ='#607d8b',fg='white').place(x=300,y=350,width=120,height=30)


        self.message=''
        self.lbl_message=Label(emp_Frame,text=self.message,font=('times new roman',20),bg='white',fg='green')
        self.lbl_message.place(x=0,y=310,relwidth=1)

        qr_Frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        title = Label(qr_Frame,text="Employee QR Code",font=("goudy old style  ",20),bg="#043256",fg="white").place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_Frame,text='QR code\n Not Available',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)


    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_depertment.set('')
        self.var_designation.set('')
        self.lbl_message.config(text=self.message)
        self.qr_code.config(image='')



    def generate(self):

        if self.var_designation.get() =='' or self.var_depertment.get() =='' or self.var_emp_code.get() == '' or self.var_name.get()=='':
            self.message= 'All Fields are Required!!!'
            self.lbl_message.config(text=self.message,fg='red')
        else:

            qr_data = (f"Employee ID{self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nDepartment:{self.var_depertment.get()}\nDesignation:{self.var_designation.get()} ")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Employee_qr/Emp_" +str(self.var_emp_code.get())+'.png')
            self.img= ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.img)

            self.message = 'QR Geenerated Successgully!!!'
            self.lbl_message.config(text=self.message,fg='green')




root = Tk()
root.iconbitmap("C:\\Users\\tanze\\OneDrive\\Desktop\\AI chatbot\\logo.ico")
obj = QR_generator(root)
root.mainloop()