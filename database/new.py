# %%

# %%

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import time
import datetime
import sqlite3 as sql
import random

user_name = ""
pass_word = ""


def w1():
    global user_name, pass_word
    window = Tk()
    window.configure(background="DeepSkyBlue4")
    window.title("USER DETAILS")
    window.geometry('1920x1080')

    ##Upper Name

    lbl = Label(window, text="DORA'S KITCHEN", background="DeepSkyBlue4", foreground="gold3", font=("Algerian", 50))
    lbl.place(x=480, y=150)
    lbl1 = Label(window, text="LOGIN", font=("Times New Roman Bold", 25), background="DeepSkyBlue4",
                 foreground="SeaGreen3")
    lbl1.place(x=680, y=250)

    ## username entry point

    ent = Entry(window, font=("Times New Roman Bold", 15))
    ent.place(x=632, y=350)
    ent.insert(0, "ENTER USERNAME/MAIL")
    ent.configure(state=DISABLED)

    ##  password entry point

    ent1 = Entry(window, font=("Times New Roman Bold", 15), show="*")
    ent1.place(x=632, y=400)
    ent1.insert(0, "ENTER PASSWORD")
    ent1.configure(state=DISABLED)

    ## username

    def on_click(event):
        ent.configure(state=NORMAL)
        ent.delete(0, END)
        ent.unbind('<Button-1>', on_click_id)

    on_click_id = ent.bind('<Button-1>', on_click)

    ## password

    def on_click1(event):
        ent1.configure(state=NORMAL)
        ent1.delete(0, END)
        ent1.unbind('<Button-1>', on_click_ps)

    on_click_ps = ent1.bind('<Button-1>', on_click1)

    ###Function

    def LOGIN():
        if ent.get() == user_name and ent1.get() == pass_word:

            messagebox.showinfo('Update Info', "Yupp!!")
            window.destroy()
            w2()
        else:
            messagebox.showerror('Error Message', 'Error in Credential!!')

    ###Log In Button

    btn = Button(window, text="Click", command=LOGIN)
    btn.place(x=640, y=450)
    btn.config(text="LOGIN", width=30)
    window.mainloop()


def w2():
    window = Tk()
    window.title("USER DETAILS")
    window.geometry('1920x1080')
    window.configure(background="red")
    lbl = Label(window, text="Explore Menu", font=("Algerian", 30), background="Red", foreground="blue2")
    lbl.place(x=10, y=15)
    ### <---------------------------------------------->
    # chicken level
    img_chicken = Label(window, width=70, text="CHICKEN", font=("Arial Black", 15), background="red", foreground="cyan")
    img_chicken.place(x=100, y=100)
    # chicken price level
    chicken_lbl1 = Label(window, text="PRICE-120 ", font=("Agency FB", 13), background="snow", foreground="red2")
    chicken_lbl1.place(x=45, y=178)

    # chicken"+" button
    def chicken_click():
        x = 120
        y = int(chicken_ent.get())
        z = x * y
        chicken_val = z
        val = str(z)
        chicken_lbl2.configure(text=val)

    chicken_btn = Button(window, text="=", width=3, command=chicken_click)
    chicken_btn.place(x=178, y=179)
    # entey quantity
    chicken_ent = Entry(window, width=5)
    chicken_ent.place(x=137, y=181)
    # chicken price count level
    chicken_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    chicken_lbl2.place(x=220, y=178)

    # <------------------------------------------------->
    # bergar
    ####<------------------------------------------------>

    # berger level
    img_bergar = Label(window, width=70, text="BURGER", font=("Arial Black", 15), background="red", foreground="cyan")
    img_bergar.place(x=104, y=270)
    # bergur price level
    bergar_lbl1 = Label(window, text="PRICE-150 ", font=("Agency FB", 13), background="snow", foreground="red2")
    bergar_lbl1.place(x=45, y=350)

    # burger"+" button
    def berger_click():
        x = 150
        y = int(bergar_ent.get())
        z = x * y
        bergar_val = z
        val = str(z)
        bergar_lbl2.configure(text=val)

    bergar_btn = Button(window, text="=", width=3, command=berger_click)
    bergar_btn.place(x=178, y=350)
    # bergar entry box
    bergar_ent = Entry(window, width=5)
    bergar_ent.place(x=138, y=352)
    # chicken price count level
    bergar_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    bergar_lbl2.place(x=220, y=350)
    ####<------------------------------------------------------------>
    # pototo chips
    ####<------------------------------------------------------------>
    # chicken level
    img_chips = Label(window, width=70, text="PATOTO CHIPS", font=("Arial Black", 15), background="red",
                      foreground="cyan")
    img_chips.place(x=80, y=440)
    # chicken price level
    chips_lbl1 = Label(window, text="PRICE-200 ", font=("Agency FB", 13), background="snow", foreground="red2")
    chips_lbl1.place(x=45, y=522)

    # chicken"+" button
    def chips_click():
        x = 200
        y = int(chips_ent.get())
        z = x * y
        chips_val = z
        val = str(z)
        chips_lbl2.configure(text=val)

    chips_btn = Button(window, text="=", width=3, command=chips_click)
    chips_btn.place(x=178, y=521)
    # poto
    chips_ent = Entry(window, width=5)
    chips_ent.place(x=138, y=523)
    # chicken price count level
    chips_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    chips_lbl2.place(x=220, y=521)
    ##<------------------------------------------------------------>
    # beverages
    ### <---------------------------------------------->
    # chicken level
    img_beve = Label(window, width=70, text="BEVERAGES", font=("Arial Black", 15), background="red", foreground="cyan")
    img_beve.place(x=380, y=100)
    # chicken price level
    beve_lbl1 = Label(window, text="PRICE-80 ", font=("Agency FB", 13), background="snow", foreground="red2")
    beve_lbl1.place(x=345, y=178)

    # chicken"+" button

    def beve_click():
        x = 80
        y = int(beve_ent.get())
        z = x * y
        beve_val = z
        val = str(z)
        beve_lbl2.configure(text=val)

    beve_btn = Button(window, text="=", width=3, command=beve_click)
    beve_btn.place(x=478, y=179)
    # beverages entry
    beve_ent = Entry(window, width=5)
    beve_ent.place(x=438, y=181)
    # chicken price count level
    beve_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    beve_lbl2.place(x=520, y=178)

    # <------------------------------------------------->
    # PIZZA
    ####<------------------------------------------------>

    # chicken level
    img_pizza = Label(window, width=70, text="PIZZA", font=("Arial Black", 15), background="red", foreground="cyan")
    img_pizza.place(x=410, y=270)
    # chicken price level
    pizza_lbl1 = Label(window, text="PRICE-500 ", font=("Agency FB", 13), background="snow", foreground="red2")
    pizza_lbl1.place(x=345, y=350)

    # chicken"+" button

    def pizza_click():
        x = 500
        y = int(pizza_ent.get())
        z = x * y
        pizza_val = z
        val = str(z)
        pizza_lbl2.configure(text=val)

    pizza_btn = Button(window, text="=", width=3, command=pizza_click)
    pizza_btn.place(x=478, y=350)
    # pizza entry
    pizza_ent = Entry(window, width=5)
    pizza_ent.place(x=438, y=352)
    # chicken price count level
    pizza_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    pizza_lbl2.place(x=520, y=350)
    ###<----------------------------------------------------------->
    # SNACKS
    ####<------------------------------------------------------------>
    # chicken level
    img_snacks = Label(window, width=70, text="SNACKS", font=("Arial Black", 15), background="red", foreground="cyan")
    img_snacks.place(x=400, y=440)
    # chicken price level
    snacks_lbl1 = Label(window, text="PRICE-200 ", font=("Agency FB", 13), background="snow", foreground="red2")
    snacks_lbl1.place(x=345, y=522)

    # chicken"+" button
    def snacks_click():
        x = 200
        y = int(snacks_ent.get())
        z = x * y
        snacks_val = z
        val = str(z)
        snacks_lbl2.configure(text=val)

    snacks_btn = Button(window, text="=", width=3, command=snacks_click)
    snacks_btn.place(x=478, y=521)
    # snacks
    snacks_ent = Entry(window, width=5)
    snacks_ent.place(x=437, y=523)
    # chicken price count level
    snacks_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    snacks_lbl2.place(x=520, y=521)
    ##<------------------------------------------------------------>
    # RICE BOWLZ
    ### <---------------------------------------------->
    # chicken level
    img_rice = Label(window, width=70, text="RICE BOWLZ", font=("Arial Black", 15), background="red", foreground="cyan")
    img_rice.place(x=680, y=100)
    # chicken price level
    rice_lbl1 = Label(window, text="PRICE-200 ", font=("Agency FB", 13), background="snow", foreground="red2")
    rice_lbl1.place(x=645, y=178)

    # chicken"+" button
    def rice_click():
        x = 200
        y = int(rice_ent.get())
        z = x * y
        rice_val = z
        val = str(z)
        rice_lbl2.configure(text=val)

    rice_btn = Button(window, text="=", width=3, command=rice_click)
    rice_btn.place(x=778, y=179)
    # rice ent
    rice_ent = Entry(window, width=5)
    rice_ent.place(x=737, y=181)
    # chicken price count level
    rice_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    rice_lbl2.place(x=820, y=178)

    # <------------------------------------------------->
    # BIRIYANI
    ####<------------------------------------------------>

    # chicken level
    img_biri = Label(window, width=70, text="BIRIYANI", font=("Arial Black", 15), background="red", foreground="cyan")
    img_biri.place(x=690, y=270)
    # chicken price level
    biri_lbl1 = Label(window, text="PRICE-120 ", font=("Agency FB", 13), background="snow", foreground="red2")
    biri_lbl1.place(x=645, y=350)

    # chicken"+" button

    def biri_click():
        x = 120
        y = int(biri_ent.get())
        z = x * y
        biri_val = z
        val = str(z)
        biri_lbl2.configure(text=val)

    biri_btn = Button(window, text="=", width=3, command=biri_click)
    biri_btn.place(x=778, y=350)
    # biriyani
    biri_ent = Entry(window, width=5)
    biri_ent.place(x=737, y=352)
    # chicken price count level
    biri_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    biri_lbl2.place(x=820, y=350)
    ###<----------------------------------------------------------->
    # MUTTON
    ####<------------------------------------------------------------>
    # chicken level
    img_mutton = Label(window, width=70, text="MUTTON", font=("Arial Black", 15), background="red", foreground="cyan")
    img_mutton.place(x=700, y=440)
    # chicken price level
    mutton_lbl1 = Label(window, text="PRICE-200 ", font=("Agency FB", 13), background="snow", foreground="red2")
    mutton_lbl1.place(x=645, y=522)

    # chicken"+" button

    def mutton_click():
        x = 200
        y = int(mutton_ent.get())
        z = x * y
        mutton_val = z
        val = str(z)
        mutton_lbl2.configure(text=val)

    mutton_btn = Button(window, text="=", width=3, command=mutton_click)
    mutton_btn.place(x=778, y=521)
    # mutton
    mutton_ent = Entry(window, width=5)
    mutton_ent.place(x=737, y=523)
    # chicken price count level
    mutton_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    mutton_lbl2.place(x=820, y=521)
    ##<------------------------------------------------------------>
    # MUGLAI
    ### <---------------------------------------------->
    # chicken level
    img_muglai = Label(window, width=70, text="MUGLAI", font=("Arial Black", 15), background="red", foreground="cyan")
    img_muglai.place(x=980, y=100)
    # chicken price level
    muglai_lbl1 = Label(window, text="PRICE-60 ", font=("Agency FB", 13), background="snow", foreground="red2")
    muglai_lbl1.place(x=945, y=178)

    # chicken"+" button

    def muglai_click():
        x = 60
        y = int(muglai_ent.get())
        z = x * y
        muglai_val = z
        val = str(z)
        muglai_lbl2.configure(text=val)

    muglai_btn = Button(window, text="=", width=3, command=muglai_click)
    muglai_btn.place(x=1078, y=179)
    # muglai
    muglai_ent = Entry(window, width=5)
    muglai_ent.place(x=1037, y=181)
    # chicken price count level
    muglai_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    muglai_lbl2.place(x=1120, y=178)

    # <------------------------------------------------->
    # CHOWMEIN
    ####<------------------------------------------------>

    # chicken level
    img_chow = Label(window, width=70, text="CHOWMEIN", font=("Arial Black", 15), background="red", foreground="cyan")
    img_chow.place(x=970, y=270)
    # chicken price level
    chow_lbl1 = Label(window, text="PRICE-50 ", font=("Agency FB", 13), background="snow", foreground="red2")
    chow_lbl1.place(x=945, y=350)

    # chicken"+" button

    def chow_click():
        x = 50
        y = int(chow_ent.get())
        z = x * y
        chow_val = z
        val = str(z)
        chow_lbl2.configure(text=val)

    chow_btn = Button(window, text="=", width=3, command=chow_click)
    chow_btn.place(x=1078, y=350)
    # chowmein
    chow_ent = Entry(window, width=5)
    chow_ent.place(x=1037, y=352)
    # chicken price count level
    chow_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    chow_lbl2.place(x=1120, y=350)
    ###<----------------------------------------------------------->
    # ROLL
    ####<------------------------------------------------------------>
    # chicken level
    img_roll = Label(window, width=70, text="ROLL", font=("Arial Black", 15), background="red", foreground="cyan")
    img_roll.place(x=1000, y=440)
    # chicken price level
    roll_lbl1 = Label(window, text="PRICE-40 ", font=("Agency FB", 13), background="snow", foreground="red2")
    roll_lbl1.place(x=945, y=522)

    # chicken"+" button
    def roll_click():

        x = 40
        y = int(roll_ent.get())
        z = x * y
        roll_val = z
        val = str(z)
        roll_lbl2.configure(text=val)

    roll_btn = Button(window, text="=", width=3, command=roll_click)
    roll_btn.place(x=1078, y=521)
    # roll
    roll_ent = Entry(window, width=5)
    roll_ent.place(x=1037, y=523)
    # chicken price count level
    roll_lbl2 = Label(window, text="0", font=("Arial Black", 12))
    roll_lbl2.place(x=1120, y=521)
    ##<------------------------------------------------------------>
    ## Part 2 or Customer Data Entry
    # <-------------------------------------------------------------->

    # costomer bill
    ##<--------------------------------------------------------------->
    bill_lbl = Label(window, text="BILL", font=("Algerian", 18), background="snow", foreground="SpringGreen4")
    bill_lbl.place(x=1300, y=220)
    ##<------------------------------------------------------------->
    # name
    # <----------------------------------------------------------->
    name_lbl = Label(window, text="COSTOMER NAME:", font=("Arial Black", 10), foreground="orange2")
    name_lbl.place(x=1210, y=290)
    name_ent = Entry(window, width=20)
    name_ent.place(x=1347, y=290)
    # <--------------------------------------------------------------->
    # mobile no.
    # <------------------------------------------------------------->
    mob_lbl = Label(window, text="MOBILE NO:", font=("Arial Black", 10), foreground="orange2")
    mob_lbl.place(x=1210, y=330)
    mob_ent = Entry(window, width=20)
    mob_ent.place(x=1347, y=330)
    # <------------------------------------------------------------------>
    # total price
    # <---------------------------------------------------------------------->
    total_lbl = Label(window, text="TOTAL PRICE", font=("Arial Black", 10), foreground="orange2")
    total_lbl.place(x=1210, y=416)
    total_ent = Label(window, text="        ", width=20)
    total_ent.place(x=1347, y=416)
    # <----------------------------------------------------------------------->
    # <----------------------------------------------------------------------->

    # thankyou
    # <-------------------------------------------------------------------------->
    thank_lbl = Label(window, text="THANK YOU", font=("Algerian", 25), foreground="blue2")
    thank_lbl.place(x=1240, y=655)
    # <-------------------------------------------------------------------------->
    # refresh button
    # <---------------------------------------------------------------------------->
    def refresh():
        window.destroy()
        w2()


    refresh_btn = Button(window, text="REFRESH", width=30,command=refresh)
    refresh_btn.place(x=180, y=665)

    # <------------------------------------------------------------------------->
    # exit button
    # <---------------------------------------------------------->

    def back():
        window.destroy()
        w1()

    exit_btn = Button(window, text="EXIT", width=30, command=back)
    exit_btn.place(x=850, y=665)

    # <----------------------------------------------------------->
    # confirm button
    # <-------------------------------------------------------------->

    def total_calc():

        if chicken_ent.get() != "":
            chi = int(chicken_ent.get())
            chi_fix = 120
        else:
            chi = 0
            chi_fix = 120
        if bergar_ent.get() != "":
            bur = int(bergar_ent.get())
            bur_fix = 150
        else:
            bur = 0
            bur_fix = 150

        if chips_ent.get() != "":
            chip = int(chips_ent.get())
            chip_fix = 200
        else:
            chip = 0
            chip_fix = 200
        if beve_ent.get() != "":
            bev = int(beve_ent.get())
            bev_fix = 80
        else:
            bev = 0
            bev_fix = 80
        if pizza_ent.get() != "":
            piz = int(pizza_ent.get())
            piz_fix = 500
        else:
            piz = 0
            piz_fix = 500
        if snacks_ent.get() != "":
            sna = int(snacks_ent.get())
            sna_fix = 200
        else:
            sna = 0
            sna_fix = 200
        if rice_ent.get() != "":
            rice = int(rice_ent.get())
            rice_fix = 200
        else:
            rice = 0
            rice_fix = 200
        if biri_ent.get() != "":
            biri = int(biri_ent.get())
            biri_fix = 120
        else:
            biri = 0
            biri_fix = 120
        if mutton_ent.get() != "":
            mutton = int(mutton_ent.get())
            mutton_fix = 200
        else:
            mutton = 0
            mutton_fix = 200
        if muglai_ent.get() != "":
            mug = int(muglai_ent.get())
            mug_fix = 60
        else:
            mug = 0
            mug_fix = 60
        if chow_ent.get() != "":
            chow = int(chow_ent.get())
            chow_fix = 50
        else:
            chow = 0
            chow_fix = 50
        if roll_ent.get() != "":
            roll = int(roll_ent.get())
            roll_fix = 40
        else:
            roll = 0
            roll_fix = 40

        total_cal = (chi * chi_fix) + (bur * bur_fix) + (chip * chip_fix) + (bev * bev_fix) + (piz * piz_fix) + (
                sna * sna_fix) + (rice * rice_fix) + (biri * biri_fix) + (mutton * mutton_fix) + (mug * mug_fix) + (
                            chow * chow_fix) + (roll * roll_fix)
        # print("Total Val ",total_cal)

        total_ent.configure(text=str(total_cal))

        chicken_lbl2.configure(text=str(chi * chi_fix))
        bergar_lbl2.configure(text=str(bur * bur_fix))
        chips_lbl2.configure(text=str(chip * chip_fix))
        beve_lbl2.configure(text=str(bev * bev_fix))
        pizza_lbl2.configure(text=str(piz * piz_fix))
        snacks_lbl2.configure(text=str(sna * sna_fix))
        rice_lbl2.configure(text=str(rice * rice_fix))
        biri_lbl2.configure(text=str(biri * biri_fix))
        mutton_lbl2.configure(text=str(mutton * mutton_fix))
        muglai_lbl2.configure(text=str(mug * mug_fix))
        chow_lbl2.configure(text=str(chow * chow_fix))
        roll_lbl2.configure(text=str(roll * roll_fix))
        total_str1 = str(total_cal)

        ####DataBase Connection

        link = "/home/samrat/Projects/Python_Projects/Billing_Management/database/"
        dbase = sql.connect(link + "billing_data.db")

        print("Creation Done")
        try:
            dbase.execute('''CREATE TABLE BILL_TABLE(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            BILL TEXT ,
            DATE TEXT ,
            TIME TEXT ,
            NAME TEXT ,
            PHONE TEXT ,
            CHICKEN TEXT,
            BURGER TEXT,
            CHIPS TEXT,
            BEVERAGES TEXT,
            PIZZA TEXT,
            SNACKS TEXT,
            RICE TEXT,
            BIRIYANI TEXT,
            MUTTON TEXT,
            MUGLAI TEXT ,
            CHOWMIN TEXT,
            ROLL TEXT,
            TOTAL TEXT ,



            );''')

        except:
            pass

        # print("Return Data {} is {} ".format(bill(),type(bill())))
        lll=str(bill())
        BILL1 = str(bill())
        DATE1 = date_lbl['text']
        TIME1 = time_lbl['text']
        NAME1 = name_ent.get()
        PHONE1 = str(mob_ent.get())
        CHICKEN1 = str(chicken_ent.get())
        BURGER1 = str(bergar_ent.get())
        CHIPS1 = str(chips_ent.get())
        BEVERAGES1 = str(beve_ent.get())
        PIZZA1 = str(pizza_ent.get())
        SNACKS1 = str(snacks_ent.get())
        RICE1 = str(rice_ent.get())
        BIRIYANI1 = str(biri_ent.get())
        MUTTON1 = str(mutton_ent.get())
        MUGLAI1 = str(muglai_ent.get())
        CHOWMIN1 = str(chow_ent.get())
        ROLL1 = str(roll_ent.get())

        TOTAL1 = str(total_str1)

        val = (
            BILL1, DATE1, TIME1, NAME1, PHONE1, CHICKEN1, BURGER1, CHIPS1, BEVERAGES1, PIZZA1, SNACKS1, RICE1, BIRIYANI1, MUTTON1,
            MUGLAI1,
            CHOWMIN1, ROLL1, TOTAL1)

        sql_val = "INSERT INTO BILL_TABLE (BILL,DATE,TIME,NAME,PHONE,CHICKEN,BURGER,CHIPS,BEVERAGES,PIZZA,SNACKS,RICE,BIRIYANI,MUTTON,MUGLAI,CHOWMIN, ROLL,TOTAL) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        dbase.execute(sql_val, val)
        dbase.commit()

        #### Generte Bill or Text file according to Input

        bill_file=open("/home/samrat/Projects/Python_Projects/Billing_Management/database/"+lll+".txt",'w+')
        bill_file.close()
        bill_file = open("/home/samrat/Projects/Python_Projects/Billing_Management/database/Gen_Bill.txt", 'w+')
        bill_file.write("Bill Date : "+DATE1+"                         "+"Time "+TIME1+"\n"+"Customer Name : "+NAME1+"\n"+"Phone No. : "+PHONE1+"\n"+"Chicken :"+CHICKEN1+" Price : "+str(chi*chi_fix)+"\n"+"Burger : "+BURGER1+" Price "+str(bur*bur_fix)+"\n"+"Chips : "+CHIPS1+" Price "+str(chip*chip_fix)+"\n"+"Beverage : "+BEVERAGES1+" Price "+str(bev*bev_fix)+"\n"+"Pizza : "+PIZZA1+" Price "+str(piz*piz_fix)+"\n"+"Snacks : "+SNACKS1+" Price "+str(sna*sna_fix)+"\n"+"Rice Bowel : "+RICE1+" Price "+str(rice*rice_fix)+"\n"+"Biriyani : "+BIRIYANI1+" Price "+str(biri*biri_fix)+"\n"+"Mutton : "+MUTTON1+" Price "+str(mutton*mutton_fix)+"\n"+"Muglai : "+MUGLAI1+" Price "+str(mug*mug_fix)+"\n"+"Chowmin : "+CHOWMIN1+" Price "+str(chow*chow_fix)+"\n"+"Burger : "+BURGER1+" Price "+str(roll*roll_fix)+"\n"+"Total"+"                                        "+TOTAL1)
        bill_file.close()





    ###random Bill Generate

    def bill():
        l1 = random.randint(1111, 9999)
        data = ("BILL" + str(l1))
        return data

    confirm_btn = Button(window, text="TOTAL", width=30, command=total_calc)
    confirm_btn.place(x=520, y=665)
    # <-------------------------------------------------------------------->
    # date&time
    # <------------------------------------------------------------------->
    date_lbl = Label(window, text=str(datetime.datetime.now())[0:10], background="thistle1")
    date_lbl.place(x=1340, y=30)
    time_lbl = Label(window, text=str(datetime.datetime.now())[-15:-7])
    time_lbl.place(x=1340, y=50)


    # All Logical Operations Done Here

    window.mainloop()


w1()

# %%


# %%


# %%


