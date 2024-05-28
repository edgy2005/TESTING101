#   ====================================================================================================================
#                                            OOP- Final Project
#
#                                               Passed By:
#
#                                            Sir Andrean Reyes
#                                            Jericho Mariñas
#                                            Renzo John Rondina
#                                            Edrich Tolentino
#
#   =====================================================================================================================

#SIR ANDREAN REYES 2
# JERICHO 2

import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

#         ------------ CHECK LOGIN -----------------

def check_login():
    username = Uname.get()
    password = Pword.get()

    # Connect to the SQLite database
    conn = sqlite3.connect('Login')
    cursor = conn.cursor()

    # Query the database for the username, password, and department
    cursor.execute('SELECT * FROM login_tbl WHERE username = ? AND password = ?', (username, password))
    result = cursor.fetchone()

    if result:
        Dept = result[2]
        if Dept == "admin":
            login_window.destroy()
            homepage()

        elif Dept == "accounting":
            login_window.destroy()
            homepage2()
        elif Dept == "HR":
            login_window.destroy()
            homepage3()
        else:
            messagebox.showerror("Invalid Department", "User belongs to an invalid department")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
    conn.close()

def save_data_entry():
    # Placeholder function to save form data
    # Add logic to save the form data to the database or a file
    messagebox.showinfo("Save", "Data saved successfully!")

#       ------------------ PAYROLL -----------------------

def payroll():

    Proll = tk.Toplevel()
    Proll.title("Se-ri's Choice Payroll")

    Pframe = Frame(Proll, width=850, height=800, bg='#d3d3d3')
    Pframe.place(x=1, y=1)
    heading = Label(Pframe, text="SE-RI'S CHOICE PAYROLL", fg='black', bg='#d3d3d3',
                    font=('Algerian', 30, 'bold'))
    heading.place(x=170, y=1)
    employeebf = Label(Pframe, text="EMPLOYEE BASIC INFO:", fg='black', bg='#d3d3d3',
                       font=('Calibri', 10, 'bold')).place(x=45, y=60)
    border = Label(Pframe, width=16, height=7, bg="gray", border=2).place(x=50, y=80)

    # Employee Number
    employeeno = Label(Pframe, text="Employee Number:", width=15, bg='#d3d3d3', font=("bold", 10)).place(x=50, y=200)
    empno = Entry(Pframe)
    empno.place(x=200, y=200)

    # Department
    department = Label(Pframe, text="Department:", width=10, bg='#d3d3d3', font=("bold", 10))
    department.place(x=49, y=260)
    dept = Entry(Pframe)
    dept.place(x=200, y=260)

    #                                   B A S I C    I N C O M E

    basicincome = Label(Pframe, text="BASIC INCOME:", fg='black', bg='#d3d3d3', font=('Calibri', 15, 'bold')).place(x=45,
                                                                                                                   y=290)

    ratehour1 = Label(Pframe, text="Rate/Hour:", width=10, bg='#d3d3d3', font=("bold", 10))
    ratehour1.place(x=46, y=320)
    rhour1 = Entry(Pframe)
    rhour1.place(x=200, y=320)

    cutoff1 = Label(Pframe, text="No. of Hours/Cut Off:", width=15, bg='#d3d3d3', font=("bold", 10))
    cutoff1.place(x=55, y=350)
    co1 = Entry(Pframe)
    co1.place(x=200, y=350)

    incomeco1 = Label(Pframe, text="Income/Cut Off:", width=15, bg='#d3d3d3', font=("bold", 10))
    incomeco1.place(x=41, y=380)

    def calculate_BasicIncome(*args):
        ratehour1_val_str = rhour1_var.get()
        cutoff1_val_str = co1_var.get()

        if ratehour1_val_str and cutoff1_val_str:  # Check if both values are not empty
            try:
                ratehour1_val = float(ratehour1_val_str)
                cutoff1_val = float(cutoff1_val_str)
                income1_val = ratehour1_val * cutoff1_val
                ico1_var.set(income1_val)
            except ValueError:
                tk.messagebox.showerror("Invalid Input",
                                        "Please enter valid numeric values for Rate/Hour and No. of Hours/Cut Off.")
        else:
            ico1_var.set("")

    rhour1_var = StringVar()
    co1_var = StringVar()
    rhour1_var.trace("w", calculate_BasicIncome)
    co1_var.trace("w", calculate_BasicIncome)
    rhour1 = Entry(Pframe, textvariable=rhour1_var)
    rhour1.place(x=200, y=320)
    co1 = Entry(Pframe, textvariable=co1_var)
    co1.place(x=200, y=350)
    ico1_var = StringVar()
    ico1 = Entry(Pframe, textvariable=ico1_var, state="readonly")
    ico1.place(x=200, y=380)

    # -----------------------------------------------------------------------------------------------------------------------

    #                          --- H O N O R A R I U M    I N C O M E ---

    honorariumincome = (Label(Pframe, text="HONORARIUM INCOME:", fg='black', bg='#d3d3d3', font=('Calibri', 15, 'bold'))
                        .place(x=45, y=410))

    ratehour2 = Label(Pframe, text="Rate/Hour:", width=10, bg='#d3d3d3', font=("bold", 10))
    ratehour2.place(x=46, y=440)

    cutoff2 = Label(Pframe, text="No. of Hours/Cut Off: ", width=15, bg='#d3d3d3', font=("bold", 10))
    cutoff2.place(x=55, y=470)

    incomeco2 = Label(Pframe, text="Income/Cut Off: ", width=15, bg='#d3d3d3', font=("bold", 10))
    incomeco2.place(x=41, y=500)

    rhour2_var = StringVar()
    co2_var = StringVar()

#   ------------------CALCULATE HONORARIUM----------------

    def calculate_Honorarium(*args):
        ratehour2_val_str = rhour2_var.get()
        cutoff2_val_str = co2_var.get()

        if ratehour2_val_str and cutoff2_val_str:  # Check if both values are not empty
            try:
                ratehour2_val = float(ratehour2_val_str)
                cutoff2_val = float(cutoff2_val_str)
                income2_val = ratehour2_val * cutoff2_val
                ico2_var.set(income2_val)
            except ValueError:
                tk.messagebox.showerror("Invalid Input",
                                        "Please enter valid numeric values for Rate/Hour and No. of Hours/Cut Off.")
        else:
            ico2_var.set("")

    rhour2_var.trace("w", calculate_Honorarium)
    co2_var.trace("w", calculate_Honorarium)
    rhour2 = Entry(Pframe, textvariable=rhour2_var)
    rhour2.place(x=200, y=440)
    co2 = Entry(Pframe, textvariable=co2_var)
    co2.place(x=200, y=470)
    ico2_var = StringVar()
    ico2 = Entry(Pframe, textvariable=ico2_var, state="readonly")
    ico2.place(x=200, y=500)

    # ---------------------------------------------------------------------------------------------------------------------

    #                               --- O T H E R   I N C O M E ---

    otherincome = Label(Pframe, text="OTHER INCOME: ", fg='black', bg='#d3d3d3', font=('Calibri', 15, 'bold')).place(
        x=45,
        y=530)
    ratehour3 = Label(Pframe, text="Rate/Hour:", width=10, bg='#d3d3d3', font=("bold", 10))
    ratehour3.place(x=46, y=560)

    cutoff3 = Label(Pframe, text="No. of Hours/Cut Off: ", width=15, bg='#d3d3d3', font=("bold", 10))
    cutoff3.place(x=55, y=590)

    incomeco3 = Label(Pframe, text="Income/Cut Off: ", width=15, bg='#d3d3d3', font=("bold", 10))
    incomeco3.place(x=41, y=620)

    rhour3_var = StringVar()
    co3_var = StringVar()

#-------------CALCULATE OTHER INCOME----------------
    def calculate_OtherIncome(*args):
        ratehour3_val_str = rhour3_var.get()
        cutoff3_val_str = co3_var.get()

        if ratehour3_val_str and cutoff3_val_str:
            try:
                ratehour3_val = float(ratehour3_val_str)
                cutoff3_val = float(cutoff3_val_str)
                income3_val = ratehour3_val * cutoff3_val
                ico3_var.set(income3_val)
            except ValueError:
                tk.messagebox.showerror("Invalid Input",
                                        "Please enter valid numeric values for Rate/Hour and No. of Hours/Cut Off.")
        else:
            ico3_var.set("")

    rhour3_var.trace("w", calculate_OtherIncome)
    co3_var.trace("w", calculate_OtherIncome)
    rhour3 = Entry(Pframe, textvariable=rhour3_var)
    rhour3.place(x=200, y=560)
    co3 = Entry(Pframe, textvariable=co3_var)
    co3.place(x=200, y=590)
    ico3_var = StringVar()
    ico3 = Entry(Pframe, textvariable=ico3_var, state="readonly")
    ico3.place(x=200, y=620)

    #                                        S U M M A R Y    I N C O M E

    summaryincome = (Label(Pframe, text="SUMMARY INCOME: ", fg='black', bg='#d3d3d3', font=('Calibri', 15, 'bold'))
                     .place(x=45, y=650))

    grossincome = Label(Pframe, text="Gross Income:", width=10, bg='#d3d3d3', font=("bold", 10))
    grossincome.place(x=55, y=680)

    gic = Entry(Pframe)
    gic.place(x=200, y=680)

    netincome = Label(Pframe, text="Net Income: ", width=15, bg='#d3d3d3', font=("bold", 10))
    netincome.place(x=55, y=710)

    nic = Entry(Pframe)
    nic.place(x=200, y=710)

    # First Name
    firstname = Label(Pframe, text="First Name: ", width=15, bg='#d3d3d3', font=("bold", 10))
    firstname.place(x=415, y=60)
    fn = Entry(Pframe)
    fn.place(x=550, y=60)

    # Middle Name
    middlename = Label(Pframe, text="Middle Name: ", width=15, bg='#d3d3d3', font=("bold", 10))
    middlename.place(x=420, y=90)
    mn = Entry(Pframe)
    mn.place(x=550, y=90)

    # Surname
    surname = Label(Pframe, text="Surname: ", width=15, bg='#d3d3d3', font=("bold", 10))
    surname.place(x=408, y=120)
    sn = Entry(Pframe)
    sn.place(x=550, y=120)

    # Civil Status
    civilstatus = Label(Pframe, text="Civil Status: ", width=15, bg='#d3d3d3', font=("bold", 10))
    civilstatus.place(x=415, y=150)
    cv = Entry(Pframe)
    cv.place(x=550, y=150)

    qualds = Label(Pframe, text="Qualified Dependents\nStatus: ", width=20, bg='#d3d3d3', font=("bold", 8))
    qualds.place(x=408, y=180)
    qds = Entry(Pframe)
    qds.place(x=550, y=180)

    paydate = Label(Pframe, text="Paydate: ", width=15, bg='#d3d3d3', font=("bold", 10))
    paydate.place(x=408, y=210)
    pd = Entry(Pframe)
    pd.place(x=550, y=210)

    empstatus = Label(Pframe, text="Employee Status: ", width=15, bg='#d3d3d3', font=("bold", 10))
    empstatus.place(x=413, y=240)
    emps = Entry(Pframe)
    emps.place(x=550, y=240)

    design = Label(Pframe, text="Designation: ", width=15, bg='#d3d3d3', font=("bold", 10))
    design.place(x=415, y=270)
    des = Entry(Pframe)
    des.place(x=550, y=270)

    regded = Label(Pframe,
                   text="REGULAR DEDUCTIONS: ", fg='black', bg='#d3d3d3', font=('Calibri', 15, 'bold')).place(x=415,
                                                                                                              y=290)

    # ----- SSS Contribution ------------------
    def calculateSSS():
        gross_income = float(gic.get())
        if gross_income < 4250:
            sss_contribution = 180
        elif 4250 <= gross_income <= 4749.99:
            sss_contribution = 202.50
        elif 4750 <= gross_income <= 5249.99:
            sss_contribution = 225.00
        elif 5250 <= gross_income <= 5749.99:
            sss_contribution = 247.50
        elif 5750 <= gross_income <= 6249.99:
            sss_contribution = 270.00
        elif 6250 <= gross_income <= 6749.99:
            sss_contribution = 292.50
        elif 6750 <= gross_income <= 7249.99:
            sss_contribution = 315.00
        elif 7250 <= gross_income <= 7749.99:
            sss_contribution = 337.50
        elif 7750 <= gross_income <= 8249.99:
            sss_contribution = 360.00
        elif 8250 <= gross_income <= 8749.99:
            sss_contribution = 382.50
        elif 8750 <= gross_income <= 9249.99:
            sss_contribution = 405.00
        elif 9250 <= gross_income <= 9749.99:
            sss_contribution = 427.50
        elif 7750 <= gross_income <= 10249.99:
            sss_contribution = 450.00
        elif 10250 <= gross_income <= 10749.99:
            sss_contribution = 472.50
        elif 10750 <= gross_income <= 11249.99:
            sss_contribution = 495.00
        elif 11250 <= gross_income <= 11749.99:
            sss_contribution = 517.50
        elif 11750 <= gross_income <= 12249.99:
            sss_contribution = 540.00
        elif 12250 <= gross_income <= 12749.99:
            sss_contribution = 562.00
        elif 12750 <= gross_income <= 13249.99:
            sss_contribution = 585.00
        elif 13250 <= gross_income <= 13749.99:
            sss_contribution = 607.00
        elif 13750 <= gross_income <= 14249.99:
            sss_contribution = 630.00
        elif 14250 <= gross_income <= 14749.99:
            sss_contribution = 652.00
        elif 14750 <= gross_income <= 15249.99:
            sss_contribution = 675.00
        elif 15250 <= gross_income <= 15749.99:
            sss_contribution = 697.00
        elif 15750 <= gross_income <= 16249.99:
            sss_contribution = 720.00
        elif 16250 <= gross_income <= 16749.99:
            sss_contribution = 742.00
        elif 16750 <= gross_income <= 17249.99:
            sss_contribution = 765.00
        elif 17250 <= gross_income <= 17749.99:
            sss_contribution = 787.00
        elif 17750 <= gross_income <= 18249.99:
            sss_contribution = 810.00
        elif 18250 <= gross_income <= 18749.99:
            sss_contribution = 832.00
        elif 18750 <= gross_income <= 19249.99:
            sss_contribution = 855.00
        elif 19250 <= gross_income <= 19749.99:
            sss_contribution = 877.50
        else:
            sss_contribution = 900
        sssc.delete(0, END)  # Clear the PhilHealth entry widget
        sssc.insert(0, f"{sss_contribution:.2f}")

    ssscon = Label(Pframe, text="SSS Contribution: ", width=15, bg='#d3d3d3', font=("bold", 10))
    ssscon.place(x=415, y=320)
    sssc = Entry(Pframe)
    sssc.place(x=550, y=320)

    def calculatePhilhealth():
        gross_income = float(gic.get())

        if gross_income < 10000:
            philhealth_contribution = 0.00
        elif 10000 <= gross_income <= 79999.99:
            philhealth_contribution = gross_income * 0.045
        else:
            philhealth_contribution = 3200.00

        phc.delete(0, END)
        phc.insert(0, f"{philhealth_contribution:.2f}")

    phcon = Label(Pframe, text="PhilHealth Contribution: ", width=18, bg='#d3d3d3', font=("bold", 10))
    phcon.place(x=410, y=350)
    phc = Entry(Pframe)
    phc.place(x=550, y=350)

    def calculatePagibig():
        pagibig_contribution = 100
        pgc.delete(0, END)
        pgc.insert(0, f"{pagibig_contribution:.2f}")

    pagcon = Label(Pframe, text="Pagibig Contribution: ", width=15, bg='#d3d3d3', font=("bold", 10))
    pagcon.place(x=420, y=380)
    pgc = Entry(Pframe)
    pgc.place(x=550, y=380)

# --------CALCULATE WITH HOLDING TAX-----------
    def calculateWithholdingTax():
        gross_income = float(gic.get())
        if gross_income <= 10417:
            incomeTax_contribution = 0.00
        elif 10418 <= gross_income <= 16666:
            incomeTax_contribution = (gross_income - 10418) * 0.15 + 0.00
        elif 16667 <= gross_income <= 33332:
            incomeTax_contribution = (gross_income - 16667) * 0.20 + 937.50
        elif 33333 <= gross_income <= 83332:
            incomeTax_contribution = (gross_income - 33333) * 0.25 + 4270.70
        elif 83333 <= gross_income <= 333332:
            incomeTax_contribution = (gross_income - 83333) * 0.30 + 16770.70
        else:
            incomeTax_contribution = (gross_income - 91770.70) * 0.35 + 333333

        itc.delete(0, END)
        itc.insert(0, f"{incomeTax_contribution:.2f}")

    inctaxc = Label(Pframe, text="Income Tax Contribution: ", width=18, bg='#d3d3d3', font=("bold", 10))
    inctaxc.place(x=408, y=410)
    itc = Entry(Pframe)
    itc.place(x=550, y=410)

    otherded = Label(Pframe, text="OTHER DEDUCTIONS: ", fg='black', bg='#d3d3d3', font=('Calibri', 15, 'bold')).place(
        x=415, y=440)

    sssloan = Label(Pframe, text="SSS Loan: ", width=15, bg='#d3d3d3', font=("bold", 10))
    sssloan.place(x=407, y=470)
    sssl = Entry(Pframe)
    sssl.place(x=550, y=470)

    pagloan = Label(Pframe, text="Pagibig Loan: ", width=15, bg='#d3d3d3', font=("bold", 10))
    pagloan.place(x=415, y=500)
    pgloan = Entry(Pframe)
    pgloan.place(x=550, y=500)

    fcsdep = Label(Pframe, text="Faculty Savings\nDeposit: ", width=15, bg='#d3d3d3', font=("bold", 8))
    fcsdep.place(x=415, y=530)
    fcsd = Entry(Pframe)
    fcsd.place(x=550, y=530)

    fcsloan = Label(Pframe, text="Faculty Savings Loan: ", width=20, bg='#d3d3d3', font=("bold", 8))
    fcsloan.place(x=415, y=560)
    fcsl = Entry(Pframe)
    fcsl.place(x=550, y=560)

    dedsum = Label(Pframe, text="DEDUCTION SUMMARY: ", fg='black', bg='#d3d3d3', font=('Calibri', 15, 'bold')).place(
        x=415, y=590)

#-------CALCULATE TOTAL DEDUCTION--------

    def calculate_total_deduction():

        pagibig_deduc = float(pgloan.get())
        sss_deduc = float(sssl.get())
        philhealth_deduc = float(phc.get())
        witholding_deduc = float(itc.get())

        pagibigloan_deduc = float(pgloan.get())
        sssloan_deduc = float(sssl.get())
        fcsd_deduc = float(fcsd.get())
        fcsl_deduc = float(fcsl.get())

        totaldeduc = pagibig_deduc + sss_deduc + philhealth_deduc + witholding_deduc + pagibigloan_deduc + sssloan_deduc + fcsd_deduc + fcsl_deduc
        totald.delete(0, END)
        totald.insert(0, f"{totaldeduc:.2f}")

    totalded = Label(Pframe, text="Total Deductions: ", width=15, bg='#d3d3d3', font=("bold", 10))
    totalded.place(x=407, y=620)
    totald = Entry(Pframe)
    totald.place(x=550, y=620)

    #                                             ---- B U T T O N S ----

    # --------------- SEARCH BUTTON ---------

    def search_employee():
        empployeeno = empno.get()
        con = sqlite3.connect("Login")
        show = con.cursor()
        show.execute("SELECT * FROM login_tbl WHERE Emp_No=?", (empployeeno,))
        row = show.fetchone()
        con.close()

        if row:
            dept.delete(0, END)
            dept.insert(0, row[3])

            rhour1.delete(0, END)
            rhour1.insert(0, row[4])

            co1.delete(0, END)
            co1.insert(0, row[5])

            ico1.delete(0, END)
            ico1.insert(0, row[6])

            rhour2.delete(0, END)
            rhour2.insert(0, row[7])

            co2.delete(0, END)
            co2.insert(0, row[8])

            ico2.delete(0, END)
            ico2.insert(0, row[9])

            rhour3.delete(0, END)
            rhour3.insert(0, row[10])

            co3.delete(0, END)
            co3.insert(0, row[11])

            ico3.delete(0, END)
            ico3.insert(0, row[12])

            gic.delete(0, END)
            gic.insert(0, row[13])

            nic.delete(0, END)
            nic.insert(0, row[14])

            fn.delete(0, END)
            fn.insert(0, row[15])

            mn.delete(0, END)
            mn.insert(0, row[16])

            sn.delete(0, END)
            sn.insert(0, row[17])

            cv.delete(0, END)
            cv.insert(0, row[18])

            qds.delete(0, END)
            qds.insert(0, row[19])

            pd.delete(0, END)
            pd.insert(0, row[20])

            emps.delete(0, END)
            emps.insert(0, row[21])

            des.delete(0, END)
            des.insert(0, row[22])

            sssc.delete(0, END)
            sssc.insert(0, row[23])

            phc.delete(0, END)
            phc.insert(0, row[24])

            pgc.delete(0, END)
            pgc.insert(0, row[25])

            itc.delete(0, END)
            itc.insert(0, row[26])

            sssl.delete(0, END)
            sssl.insert(0, row[27])

            pgloan.delete(0, END)
            pgloan.insert(0, row[28])

            fcsd.delete(0, END)
            fcsd.insert(0, row[29])

            fcsl.delete(0, END)
            fcsl.insert(0, row[30])

            totald.delete(0, END)
            totald.insert(0, row[31])
        else:
            tk.messagebox.showinfo("No Record Found", "No record found for this employee number")

    searchemp = Label(Pframe, text="Search Employee:", width=15, bg='#d3d3d3', font=("bold", 10)).place(x=46, y=230)
    search_button = Button(Proll, width=10, text="SEARCH", bg='red', fg='white', font=("Calibri", 10),
                           command=search_employee).place(x=200, y=230)

    # ------ GROSS INCOME BUTTON ------------

    def calculate_gross_income():
        rate_hour1_value = rhour1.get()
        rate_hour2_value = rhour2.get()
        rate_hour3_value = rhour3.get()
        co1_value = co1.get()
        co2_value = co2.get()
        co3_value = co3.get()

        if rate_hour1_value.strip() == '' or rate_hour2_value.strip() == '' or rate_hour3_value.strip() == '':
            messagebox.showerror("Error", "Please enter all rate per hour values")
            return

        rate_hour1 = float(rate_hour1_value)
        rate_hour2 = float(rate_hour2_value)
        rate_hour3 = float(rate_hour3_value)

        cut_off1 = float(co1_value)
        cut_off2 = float(co2_value)
        cut_off3 = float(co3_value)

        income_cutoff1 = rate_hour1 * cut_off1
        ico1.delete(0, END)
        ico1.insert(0, f"{income_cutoff1:.2f}")

        income_cutoff2 = rate_hour2 * cut_off2
        ico2.delete(0, END)
        ico2.insert(0, f"{income_cutoff2:.2f}")

        income_cutoff3 = rate_hour3 * cut_off3
        ico3.delete(0, END)
        ico3.insert(0, f"{income_cutoff3:.2f}")

        grossincome = income_cutoff1 + income_cutoff2 + income_cutoff3
        gic.delete(0, END)
        gic.insert(0, f"{grossincome:.2f}")
        calculatePagibig()
        calculateSSS()
        calculatePhilhealth()
        calculateWithholdingTax()
        calculate_total_deduction()

    GrossIncome_Button = Button(Proll, width=11, text="GROSS INCOME", bg='blue', fg='white', font=("Calibri", 10),
                                command=calculate_gross_income).place(x=415, y=650)

    # ------ SAVE BUTTON --------------------

    def save_data_entry():
        empployeeno = empno.get()
        department = dept.get()
        ratehour1 = rhour1.get()
        cutoff1 = co1.get()
        incomeco1 = ico1.get()
        ratehour2 = rhour2.get()
        cutoff2 = co2.get()
        incomeco2 = ico2.get()
        ratehour3 = rhour3.get()
        cutoff3 = co3.get()
        incomeco3 = ico3.get()
        grossincome = gic.get()
        netincome = nic.get()
        firstname = fn.get()
        middlename = mn.get()
        surname = sn.get()
        civilstatus = cv.get()
        qualds = qds.get()
        paydate = pd.get()
        empstatus = emps.get()
        design = des.get()
        ssscon = sssc.get()
        phcon = phc.get()
        pagcon = pgc.get()
        inctaxc = itc.get()
        sssloan = sssl.get()
        pagloan = pgloan.get()
        fcsdep = fcsd.get()
        fcsloan = fcsl.get()
        totalded = totald.get()

        con = sqlite3.connect("Login")
        save_data_query = """
        INSERT INTO login_tbl (Emp_No, Dept, ratehour1, CutOff1, Income1, ratehour2, CutOff2, Income2, ratehour3, CutOff3, Income3, GrossIncome, NetIncome, FirstName, MiddleName, Surname, CivilStatus, Qualified, Paydate, EmpStats ,Designation, SSSContrib, PhilHealthContrib , PagIbigContrib , IncomeTax, SSSLoan,PagIbigLoan,FacultySavingsDeposit, FacultySavingsLoan, TotalDeductions) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)"""
        con.execute(save_data_query, (
            empployeeno, department, ratehour1, cutoff1, incomeco1, ratehour2, cutoff2, incomeco2, ratehour3, cutoff3,
            incomeco3, grossincome, netincome, firstname, middlename, surname, civilstatus, qualds, paydate, empstatus,
            design,
            ssscon, phcon, pagcon, inctaxc, sssloan, pagloan, fcsdep, fcsloan, totalded))
        con.commit()
        con.close()
        tk.messagebox.showinfo("Data Saved", "Data has been saved to the database")

    Save = (
        Button(Proll, width=10, text="SAVE", bg='#009966', fg='white', font=("Calibri", 10), command=save_data_entry)
        .place(x=587, y=650))

    # -------------- UPDATE BUTTON ----------------------

    def Update_emp_info():
        empployeeno = empno.get()
        department = dept.get()
        ratehour1 = rhour1.get()
        cutoff1 = co1.get()
        incomeco1 = ico1.get()
        ratehour2 = rhour2.get()
        cutoff2 = co2.get()
        incomeco2 = ico2.get()
        ratehour3 = rhour3.get()
        cutoff3 = co3.get()
        incomeco3 = ico3.get()
        grossincome = gic.get()
        netincome = nic.get()
        firstname = fn.get()
        middlename = mn.get()
        surname = sn.get()
        civilstatus = cv.get()
        qualds = qds.get()
        paydate = pd.get()
        empstatus = emps.get()
        design = des.get()
        ssscon = sssc.get()
        phcon = phc.get()
        pagcon = pgc.get()
        inctaxc = itc.get()
        sssloan = sssl.get()
        pagloan = pgloan.get()
        fcsdep = fcsd.get()
        fcsloan = fcsl.get()
        totalded = totald.get()

        con = sqlite3.connect("Login")
        update_data_query = """
        UPDATE login_tbl 
        SET Dept=?, ratehour1=?, CutOff1=?, Income1=?, ratehour2=?, CutOff2=?, Income2=?, ratehour3=?, CutOff3=?, Income3=?, GrossIncome=?, NetIncome=?, FirstName=?, MiddleName=?, Surname=?, CivilStatus=?, Qualified=?, Paydate=?, EmpStats=?, Designation=?, SSSContrib=?, PhilHealthContrib=?, PagIbigContrib=?, IncomeTax=?, SSSLoan=?, PagIbigLoan=?, FacultySavingsDeposit=?, FacultySavingsLoan=?, TotalDeductions=?
        WHERE Emp_No=?"""
        con.execute(update_data_query, (
            department, ratehour1, cutoff1, incomeco1, ratehour2, cutoff2, incomeco2, ratehour3, cutoff3, incomeco3,
            grossincome, netincome, firstname, middlename, surname, civilstatus, qualds, paydate, empstatus, design,
            ssscon, phcon, pagcon, inctaxc, sssloan, pagloan, fcsdep, fcsloan, totalded, empployeeno))
        con.commit()
        con.close()
        tk.messagebox.showinfo("Data Updated", "Employee information has been updated")

    Update = (Button(Proll, width=10, text="UPDATE", bg='#009966', fg='white', font=("Calibri", 10),
                     command=Update_emp_info).place(x=670, y=650))

    # --------------------- NEW BUTTON --------------------

    def New_Entry():
        empno.delete(0, END)
        dept.delete(0, END)
        rhour1.delete(0, END)
        co1.delete(0, END)
        ico1.delete(0, END)
        rhour2.delete(0, END)
        co2.delete(0, END)
        ico2.delete(0, END)
        rhour3.delete(0, END)
        co3.delete(0, END)
        ico3.delete(0, END)
        gic.delete(0, END)
        nic.delete(0, END)
        fn.delete(0, END)
        mn.delete(0, END)
        sn.delete(0, END)
        cv.delete(0, END)
        qds.delete(0, END)
        pd.delete(0, END)
        emps.delete(0, END)
        des.delete(0, END)
        sssc.delete(0, END)
        phc.delete(0, END)
        pgc.delete(0, END)
        itc.delete(0, END)
        sssl.delete(0, END)
        pgloan.delete(0, END)
        fcsd.delete(0, END)
        fcsl.delete(0, END)
        totald.delete(0, END)

    New = (Button(Proll, width=10, text="NEW", bg='#FFAE42', fg='white', font=("Calibri", 10), command=New_Entry)
           .place(x=755, y=650))

    # --------------------- NET INCOME BUTTON -----------------------------

    def calculate_net_income():
        gross_income = float(gic.get())
        total_deductions = float(totald.get())
        net_income = gross_income - total_deductions
        nic.delete(0, END)
        nic.insert(0, f"{net_income:.2f}")

    NetIncome_Button = Button(Proll, width=10, text="NET INCOME", bg='blue', fg='white', font=("Calibri", 10),
                              command=calculate_net_income)
    NetIncome_Button.place(x=505, y=650)

    Proll.geometry("850x800")
    Proll.mainloop()

    # ---------------------- REGISTRATION FORM-------------------------------------

def regis_form():
    def save_data_entry():
        FirstName = get_FirstName.get()
        MiddleName = get_MiddleName.get()
        LastName = get_LastName.get()
        Suffix = get_Suffix.get()
        DateOfBirth = DateOfBirth_entry.get()
        Gender = gender_box.get()
        Nationality = NationalityBox.get()
        CivilStats = CivilStatsBox.get()
        Department = get_Department.get()
        Designation = get_Designation.get()
        QualidDeptStats = QualidDeptStats_combobox.get()
        EmployeeStats = get_EmployeeStats.get()
        Paydate = get_Paydate.get()
        EmployeeNum = get_EmployeeNum.get()
        ContactNo = get_ContactNo.get()
        Email = get_Email.get()
        SocMed = getSocMed.get()
        AccIdNo = get_AccIdNo.get()
        AddLine1 = get_AddLine1.get()
        AddLine2 = get_AddLine2.get()
        MuniCity = get_MuniCity.get()
        StateProv = get_StateProv.get()
        Country = getCountry.get()
        Zip = get_Zip.get()
        PicPath = get_PicPath.get()

        con = sqlite3.connect("Login")
        save_data_query = """
        INSERT INTO login_tbl (FirstName, MiddleName, Surname, Suffix, DateOfBirth, gender, Nationality, CivilStatus, Dept, Designation, Qualified, EmpStats, Paydate, Emp_No, ContactNo, Email, SocMed, AccIdNo, AddLine1, AddLine2, MuniCity, StateProv, Country, Zip, PicPath) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        con.execute(save_data_query, (FirstName, MiddleName, LastName, Suffix, DateOfBirth, Gender, Nationality,
                                      CivilStats, Department, Designation, QualidDeptStats, EmployeeStats, Paydate,
                                      EmployeeNum, ContactNo, Email, SocMed, AccIdNo, AddLine1, AddLine2, MuniCity,
                                      StateProv, Country, Zip, PicPath))
        con.commit()
        con.close()
        tk.messagebox.showinfo("Data Saved", "Data has been saved to the database")
    form_window = tk.Toplevel()
    form_window.title("Registration Form")

    mainframe = Frame(form_window, width=1200, height=1500, bg='white')
    mainframe.grid(row=0, column=0, rowspan=20, columnspan=4)

    frame = Frame(mainframe, width=1000, height=300, bg='light grey')
    frame.grid(row=0, column=0, rowspan=4, columnspan=4, padx=30, pady=(5, 0), sticky='w')

    frame2 = Frame(mainframe, width=1000, height=100, bg='light grey')
    frame2.grid(row=4, column=0, rowspan=4, columnspan=4, padx=30, pady=(20, 0), sticky='w')

    frame3 = Frame(mainframe, width=1000, height=100, bg='light grey')
    frame3.grid(row=9, column=0, rowspan=4, columnspan=4, padx=30, pady=(0, 0), sticky='w')

    frame4 = Frame(mainframe, width=1000, height=100, bg='light grey')
    frame4.grid(row=15, column=0, rowspan=4, columnspan=4, padx=30, pady=(0, 0), sticky='w')

    # ----------------- FRAME 1 ------------------------------------------------
    #-------------------IMAGE---------------------------------------------------

    image = Image.open("C:\\Users\\Sirandrean\\Downloads\\charitymae.jpg")
    image = image.resize((100, 100))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(frame, image=photo)
    image_label.image = photo  # Keep reference to avoid garbage collection
    image_label.grid(row=0, column=0, rowspan=3, padx=(5, 5), pady=5)

    choose_file_button = tk.Button(frame, text="Choose File")
    choose_file_button.grid(row=3, column=0, padx=(0, 5), pady=5)

    #-------------------LABEL AND TEXTBOX---------------------------------------------------

    #           -- First Name --
    FirstName = tk.Label(frame, text="First Name", bg='light grey')
    FirstName.grid(row=0, column=1, sticky="w", padx=10, pady=(10, 0))
    get_FirstName = tk.Entry(frame)
    get_FirstName.grid(row=1, column=1, padx=10, pady=(0, 10))

    #         --- Middle Name ---
    MiddleName = tk.Label(frame, text="Middle Name", bg='light grey')
    MiddleName.grid(row=0, column=2, sticky="w", padx=10, pady=(10, 0))
    get_MiddleName = tk.Entry(frame)
    get_MiddleName.grid(row=1, column=2, padx=10, pady=(0, 10))

    #         --- Last Name ---
    LastName = tk.Label(frame, text="Last Name", bg='light grey')
    LastName.grid(row=0, column=3, sticky="w", padx=10, pady=(10, 0))
    get_LastName = tk.Entry(frame)
    get_LastName.grid(row=1, column=3, padx=10, pady=(0, 10))

    #            --- Suffix ---
    Suffix = tk.Label(frame, text="Suffix", bg='light grey')
    Suffix.grid(row=0, column=4, sticky="w", padx=10, pady=(10, 0))
    get_Suffix = tk.Entry(frame, width=20)
    get_Suffix.grid(row=1, column=4, padx=10, pady=(0, 10))

    #               --- Date Of Birth ---
    DateOfBirth = tk.Label(frame, text="Date of Birth", bg='light grey')
    DateOfBirth.grid(row=2, column=1, sticky="w")
    DateOfBirth_entry = tk.Entry(frame)
    DateOfBirth_entry.grid(row=3, column=1, padx=10, pady=1)

    #                --- Gender ---
    gender = tk.Label(frame, text="Gender", bg='light grey')
    gender.grid(row=2, column=2, sticky="w")
    gender_box = ttk.Combobox(frame, values=["Male", "Female", "Other"])
    gender_box.set(' -- select one --')
    gender_box.grid(row=3, column=2, padx=8, pady=1)

    Nationality = tk.Label(frame, text="Nationality", bg='light grey')
    Nationality.grid(row=2, column=3, sticky="w")
    NationalityBox = ttk.Combobox(frame, values=["Filipino", "American", "Other"])
    NationalityBox.set('Filipino')
    NationalityBox.grid(row=3, column=3, sticky="w", pady=1)

    CivilStats = tk.Label(frame, text="Civil Status", bg='light grey')
    CivilStats.grid(row=2, column=4, sticky="w", padx=10, pady=(5, 0))
    CivilStatsBox = ttk.Combobox(frame, values=["Married", "Single", "Other"], width=19)
    CivilStatsBox.set('--select one--')
    CivilStatsBox.grid(row=3, column=4, sticky="w", padx=10, pady=0)

    # ----------------------- FRAME 2 -------------------------------------------------------------------------------

    Department = tk.Label(frame2, text="Department", bg='light grey')
    Department.grid(row=1, column=0, sticky="w", padx=15, pady=(10, 0))
    get_Department = tk.Entry(frame2, width=50)
    get_Department.grid(row=2, column=0, padx=(15, 1), pady=0)

    Designation = tk.Label(frame2, text="Designation", bg='light grey')
    Designation.grid(row=1, column=1, sticky='w', padx=6, pady=(10, 0))
    get_Designation = tk.Entry(frame2, width=25)
    get_Designation.grid(row=2, column=1, padx=(6, 0), pady=0)

    QualidDeptStats = tk.Label(frame2, text="Qualified Dep. Status", bg='light grey')
    QualidDeptStats.grid(row=1, column=3, sticky='w', padx=15, pady=(10, 0))
    QualidDeptStats_combobox = ttk.Combobox(frame2, values=["Pending", "Other"], width=32)
    QualidDeptStats_combobox.set(' -- select one --')
    QualidDeptStats_combobox.grid(row=2, column=3, padx=(10, 0), pady=0, sticky="w")

    EmployeeStats = tk.Label(frame2, text="Employee Status", bg='light grey')
    EmployeeStats.grid(row=3, column=0, sticky='w', padx=(15, 0), pady=(10, 0))
    get_EmployeeStats = tk.Entry(frame2, width=50)
    get_EmployeeStats.grid(row=4, column=0, padx=(15, 0), pady=5)

    Paydate = tk.Label(frame2, text="Pay Date", bg='light grey')
    Paydate.grid(row=3, column=1, sticky='w', padx=15, pady=(10, 0))
    get_Paydate = tk.Entry(frame2, width=20)
    get_Paydate.grid(row=4, column=1, padx=15, pady=5)

    EmployeeNum = tk.Label(frame2, text="Employee Number", bg='light grey')
    EmployeeNum.grid(row=3, column=3, sticky='w', padx=15, pady=(10, 0))
    get_EmployeeNum = tk.Entry(frame2, width=34)
    get_EmployeeNum.grid(row=4, column=3, padx=15, pady=5)

    # ======================================================================================================================

    Contact = Label(mainframe, text="Contact Info", bg='white', font=('Times New Roman', 12, 'bold'))
    Contact.grid(row=8, column=0, sticky='w', padx=30, pady=(10, 0))

    # -------------------- FRAME 3 ----------------------------------------------------------------------------------

    ContactNo = Label(frame3, text="Contact No.", bg='light grey')
    ContactNo.grid(row=1, column=0, padx=15, pady=(10, 0), sticky='w')
    get_ContactNo = tk.Entry(frame3, width=50)
    get_ContactNo.grid(row=2, column=0, sticky='w', padx=15, pady=(0, 0))

    Email = Label(frame3, text="Email Address", bg='light grey')
    Email.grid(row=1, column=1, padx=0, pady=(10, 0), sticky='w')
    get_Email = tk.Entry(frame3, width=55)
    get_Email.grid(row=2, column=1, padx=(0, 30), pady=(0, 0))

    SocMed = Label(frame3, text="Social Media", bg='light grey')
    SocMed.grid(row=3, column=0, padx=15, pady=(10, 0), sticky='w')
    getSocMed = ttk.Combobox(frame3, values=["Facebook", "Instagram", "X"], width=50)
    getSocMed.set(' -- select one --')
    getSocMed.grid(row=4, column=0, sticky='w', padx=15, pady=(0, 10))

    AccIdNo = Label(frame3, text="Social Media Account Id/No", bg='light grey')
    AccIdNo.grid(row=3, column=1, padx=0, pady=(10, 0), sticky='w')
    get_AccIdNo = tk.Entry(frame3, width=54)
    get_AccIdNo.grid(row=4, column=1, sticky='w', padx=(0, 30), pady=(0, 10))

    Contact = Label(mainframe, text="Address", bg='white', font=('Times New Roman', 12, 'bold'))
    Contact.grid(row=14, column=0, sticky='w', padx=30, pady=(10, 0))

    AddLine1 = Label(frame4, text="Address Line 1", bg='light grey')
    AddLine1.grid(row=1, column=0, padx=15, pady=(10, 0), sticky='w')
    get_AddLine1 = tk.Entry(frame4, width=114)
    get_AddLine1.grid(row=2, column=0, columnspan=4, padx=(15, 15), sticky='w')

    AddLine2 = Label(frame4, text="Address Line 2", bg='light grey')
    AddLine2.grid(row=3, column=0, padx=15, pady=(10, 0), sticky='w')
    get_AddLine2 = tk.Entry(frame4, width=114)
    get_AddLine2.grid(row=4, column=0, columnspan=4, padx=(15, 15), sticky='w')

    MuniCity = Label(frame4, text="Municipality/City", bg='light grey')
    MuniCity.grid(row=5, column=0, padx=(15, 0), pady=(10, 0), sticky='w')
    get_MuniCity = tk.Entry(frame4, width=50)
    get_MuniCity.grid(row=6, column=0, sticky='w', padx=(15, 0), pady=(0, 0))

    StateProv = Label(frame4, text="State/Province", bg='light grey')
    StateProv.grid(row=5, column=1, padx=(15, 0), pady=(10, 0), sticky='w')
    get_StateProv = tk.Entry(frame4, width=57)
    get_StateProv.grid(row=6, column=1, sticky='w', padx=(15, 0), pady=(0, 0))

    Country = Label(frame4, text="Country", bg='light grey')
    Country.grid(row=7, column=0, padx=(15, 0), pady=(10, 0), sticky='w')
    getCountry = ttk.Combobox(frame4, values=["America", "Philippines", "Others"], width=47)
    getCountry.set(' -- select one --')
    getCountry.grid(row=8, column=0, sticky='w', padx=15, pady=(0, 10))

    Zip = Label(frame4, text="Zip Code", bg='light grey')
    Zip.grid(row=7, column=1, padx=(15, 0), pady=(10, 0), sticky='w')
    get_Zip = tk.Entry(frame4, width=20)
    get_Zip.grid(row=8, column=1, sticky='w', padx=(15, 0), pady=(0, 0))

    PicPath = Label(frame4, text="Picture Path", bg='light grey')
    PicPath.grid(row=9, column=0, padx=15, pady=(5, 0), sticky='w')
    get_PicPath = tk.Entry(frame4, width=114)
    get_PicPath.grid(row=10, column=0, columnspan=4, padx=(15, 15), pady=(0, 10), sticky='w')

    # Save Button
    Save = tk.Button(mainframe, text="Save", bg="blue", fg='white', width=10, command=save_data_entry)
    Save.grid(row=26, column=0, padx=(29, 0), pady=5, sticky='w')

    Cancel = tk.Button(mainframe, text="Cancel", width=10, command=form_window.destroy)
    Cancel.grid(row=26, column=0, padx=(115, 0), pady=5, sticky='w')

     # --------------------- ACCOUNT USER ---------------------------

def Account_User():
    def clear_inputs():
        get_first_name.delete(0, END)
        get_middle_name.delete(0, END)
        get_last_name.delete(0, END)
        get_Suffix.delete(0, END)
        get_department.delete(0, END)
        get_designation.delete(0, END)
        get_username.delete(0, END)
        get_password.delete(0, END)
        get_confirm_password.delete(0, END)
        get_user_type.delete(0, END)
        get_user_status.delete(0, END)
        get_emp_num.delete(0, END)

    # ------------------------- DATA ENTRIES ----------------------------------

    def save_data_entry():
        first_name = get_first_name.get()
        middle_name = get_middle_name.get()
        last_name = get_last_name.get()
        Suffix = get_Suffix.get()
        department = get_department.get()
        designation = get_designation.get()
        username = get_username.get()
        password = get_password.get()
        confirm_password = get_confirm_password.get()
        user_type = get_user_type.get()
        user_status = get_user_status.get()
        emp_num = get_emp_num.get()

        con = sqlite3.connect("Login")
        save_data_query = """
        INSERT INTO login_tbl (FirstName, MiddleName, Surname, Suffix, Dept, Designation, username, password, confirm_password, user_type, user_status, Emp_no) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        con.execute(save_data_query, (
        first_name, middle_name, last_name, Suffix, department, designation, username, password, confirm_password,
        user_type, user_status, emp_num))
        con.commit()
        con.close()
        tk.messagebox.showinfo("Data Updated", "Data has been updated to the database")

    Acc_User = tk.Toplevel()
    Acc_User.title("Personal Info")

    detail_frame = (tk.Frame(Acc_User, width=870, height=300, bg='light gray').place(relx=.13, rely=.230))

    # ----------------- FRAME 1 ------------------------------------------------

    image = Image.open("C:\\Users\\Sirandrean\\Downloads\\charitymae.jpg")
    image = image.resize((130, 130))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(Acc_User, image=photo)
    image_label.place(relx=.135, rely=.100)

    #           -- First Name --
    first_name = tk.Label(Acc_User, text="First Name", bg='light gray')
    first_name.place(relx=.260, rely=.280)
    get_first_name = tk.Entry(Acc_User)
    get_first_name.place(height=27, relx=.260, rely=.330)

    #         --- Middle Name ---
    middle_name = tk.Label(Acc_User, text="Middle Name", bg='light gray')
    middle_name.place(relx=.370, rely=.280)
    get_middle_name = tk.Entry(Acc_User)
    get_middle_name.place(height=27, relx=.370, rely=.330)

    #         --- Last Name ---
    last_name = tk.Label(Acc_User, text="Last Name", bg='light gray')
    last_name.place(relx=.480, rely=.280)
    get_last_name = tk.Entry(Acc_User)
    get_last_name.place(height=27, relx=.480, rely=.330)

    #            --- Suffix ---
    Suffix = tk.Label(Acc_User, text="Suffix", bg='light grey')
    Suffix.place(relx=.590, rely=.280)
    get_Suffix = tk.Entry(Acc_User)
    get_Suffix.place(height=27, relx=.590, rely=.330)

    #               --- department ---
    department = tk.Label(Acc_User, text="Department", bg='light grey')
    department.place(relx=.700, rely=.280)
    get_department = tk.Entry(Acc_User)
    get_department.place(height=27, relx=.700, rely=.330)

    #                --- designation ---
    designation = tk.Label(Acc_User, text="Designation", bg='light grey')
    designation.place(relx=.14, rely=.430)
    get_designation = tk.Entry(Acc_User)
    get_designation.place(height=27, width=250, relx=.14, rely=.480)

    #                --- Username ---

    username = tk.Label(Acc_User, text="Username", bg='light grey')
    username.place(relx=.370, rely=.430)
    get_username = tk.Entry(Acc_User)
    get_username.place(height=27, width=180, relx=.360, rely=.480)

    #                --- Password ---

    password = tk.Label(Acc_User, text="Password", bg='light grey')
    password.place(relx=.520, rely=.430)
    get_password = tk.Entry(Acc_User)
    get_password.place(height=27, width=340, relx=.520, rely=.480)

    #                --- Confirm Password ---

    confirm_password = tk.Label(Acc_User, text="Confirm Password", bg='light grey')
    confirm_password.place(relx=.14, rely=.570)
    get_confirm_password = tk.Entry(Acc_User)
    get_confirm_password.place(height=27, width=250, relx=.14, rely=.630)

    #                --- User Type ---

    user_type = tk.Label(Acc_User, text="User Type", bg='light grey')
    user_type.place(relx=.370, rely=.570)
    get_user_type = tk.Entry(Acc_User)
    get_user_type.place(height=27, width=180, relx=.360, rely=.630)

    #                --- User Status ---

    user_status = tk.Label(Acc_User, text="User Status", bg='light grey')
    user_status.place(relx=.520, rely=.570)
    get_user_status = tk.Entry(Acc_User)
    get_user_status.place(height=27, width=180, relx=.520, rely=.630)

    #                --- Employee Number ---

    emp_num = tk.Label(Acc_User, text="Employee Number", bg='light grey')
    emp_num.place(relx=.680, rely=.570)
    get_emp_num = tk.Entry(Acc_User)
    get_emp_num.place(height=27, width=180, relx=.680, rely=.630)

    #                --- Buttons ---

    update = tk.Button(Acc_User, text="Update", bg="blue", fg='white', width=10,command=save_data_entry)
    update.place(width=100, relx=.25, rely=.730)

    delete = tk.Button(Acc_User, text="Delete", bg="#EEC900", fg='black', width=10,command=clear_inputs)
    delete.place(width=100, relx=.34, rely=.730)

    cancel = tk.Button(Acc_User, text="Cancel", bg="light gray", fg='black', width=10,command=Acc_User.destroy)
    cancel.place(width=100, relx=.43, rely=.730)

    Acc_User.geometry('1200x500')
    Acc_User.mainloop()

# ------------------- HOMEPAGE IS FOR 'ADMIN' ----------------------

def homepage():
    global window
    window = Tk()
    window.geometry('1920x1080')
    window.title("Welcome")
    window.configure(bg='#7091E6')

    BlueFrame = Frame(window,width = 1920,height = 40,bg='#3D52A0')
    BlueFrame.place(x=1,y=1)

    seri = Label(BlueFrame,fg='white',bg='#3D52A0',text="Seri's Choice" ,font=('Sans Serif',18,'bold'))
    seri.place(x=1,y=4)

    footer = Frame(window,width = 1920,height = 20,bg='#3D52A0')
    footer.place(x=1,y=770)

    logout_button = Button(BlueFrame, text="Logout",bg='#3D52A0',fg='white',highlightbackground='white',highlightthickness=2,command=logout)
    logout_button.place(x=1450,y=7)

    MidFrame = Frame(window,width=400,height =280,bg='#96B4DD',highlightbackground="#7091E6",highlightthickness=2)
    MidFrame.place(x=550,y=200)

    label = Label(MidFrame, text="Hello, ADMIN!",fg='white',font=('Sans Serif',32,'bold'),bg='#96B4DD',pady=10)
    label.place(x=68,y=1)

    form_button = Button(MidFrame,width=50,pady=10,text="Registration Form",bg='#ede8f5', command=regis_form)
    form_button.place(x =20,y = 80)

    form_button2 = Button(MidFrame,width=50,pady=10,text="Payroll",command=payroll,bg='#ede8f5')
    form_button2.place(x=20, y=130)

    form_button3 = Button(MidFrame,width=50,pady=10,text="User Account Information",bg='#ede8f5',command=Account_User)
    form_button3.place(x=20, y=190)

    window.mainloop()

    # ------------------ HOMEPAGE 2 IS FOR 'ACCOUNTING' -------------------------

def homepage2():
    global window
    window = Tk()
    window.geometry('1920x1080')
    window.title("Welcome")
    window.configure(bg='#7091E6')

    BlueFrame = Frame(window,width = 1920,height = 40,bg='#3D52A0')
    BlueFrame.place(x=1,y=1)

    seri = Label(BlueFrame,fg='white',bg='#3D52A0',text="Seri's Choice" ,font=('Sans Serif',18,'bold'))
    seri.place(x=1,y=4)

    footer = Frame(window,width = 1920,height = 20,bg='#3D52A0')
    footer.place(x=1,y=770)

    logout_button = Button(BlueFrame, text="Logout",bg='#3D52A0',fg='white',highlightbackground='white',highlightthickness=2,command=logout)
    logout_button.place(x=1450,y=7)

    MidFrame = Frame(window,width=600,height =280,bg='#96B4DD',highlightbackground="#7091E6",highlightthickness=2)
    MidFrame.place(x=480,y=200)

    label = Label(MidFrame, text="Hello, Accountant!",fg='white',font=('Sans Serif',32,'bold'),bg='#96B4DD',pady=10)
    label.place(x=130,y=1)

    form_button2 = Button(MidFrame,width=50,text="PAYROLL",command=payroll,bg='#ede8f5',height=5)
    form_button2.place(x=130, y=130)

    window.mainloop()

    # ----------------- HOMEPAGE 3 IS FOR 'HR STAFF' ----------------------

def homepage3():
    global window
    window = Tk()
    window.geometry('1920x1080')
    window.title("Welcome")
    window.configure(bg='#7091E6')

    BlueFrame = Frame(window,width = 1920,height = 40,bg='#3D52A0')
    BlueFrame.place(x=1,y=1)

    seri = Label(BlueFrame,fg='white',bg='#3D52A0',text="Seri's Choice" ,font=('Sans Serif',18,'bold'))
    seri.place(x=1,y=4)

    footer = Frame(window,width = 1920,height = 20,bg='#3D52A0')
    footer.place(x=1,y=770)

    logout_button = Button(BlueFrame, text="Logout",bg='#3D52A0',fg='white',highlightbackground='white',highlightthickness=2,command=logout)
    logout_button.place(x=1450,y=7)

    MidFrame = Frame(window,width=600,height =280,bg='#96B4DD',highlightbackground="#7091E6",highlightthickness=2)
    MidFrame.place(x=480,y=200)

    label = Label(MidFrame, text="Hello, HR!        ",fg='white',font=('Sans Serif',32,'bold'),bg='#96B4DD',pady=10)
    label.place(x=130,y=1)

    form_button = Button(MidFrame, width=50,text="REGISTRATION FORM", bg='#ede8f5', command=regis_form,height=5)
    form_button.place(x=130, y=130)

    # --------------------- LOGOUT -------------------------------

def logout():
    window.destroy()
    show_login_window()

    # ------------------- LOGIN WINDOW -------------------------

def show_login_window():
    global login_window, Uname, Pword
    login_window = Tk()
    login_window.geometry('1920x1080')
    login_window.title("Login Page")
    login_window.configure(bg='#7091E6')

    Uname = StringVar()
    Pword = StringVar()

    frame = Frame(login_window, width=900, height=850, bg='floral white',highlightbackground="#7091E6",highlightthickness=2)
    frame.place(x=640,y=250)
    heading = Label(frame,text="Sign In",fg='navy blue',bg='floral white',font=('Calibre',21,'bold'))
    heading.place(x=1,y=1)

    entry1 = Entry(frame, textvariable=Uname)
    entry1.pack(pady=(50,0),padx=(20,80))
    entry1.insert(0,"Username")


    entry2 = Entry(frame, textvariable=Pword, show='*')
    entry2.pack(pady=10,padx=(20,80))
    entry2.insert(0,"Password")

    login_button = Button(frame, text="Login", command=check_login)
    login_button.pack(pady=20)

    login_window.mainloop()

show_login_window()



