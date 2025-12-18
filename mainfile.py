##importing tkinter module
import tkinter as tk
from tkinter  import *
from tkinter import messagebox,Tk,Label
from datetime import datetime
from time import strftime
import tempfile,os,random


def login():
    if usernameentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror('Error','Username And Password Cannot Be Empty')

    elif usernameentry.get()=='Mavericks' and passwordentry.get()=='12345678':
        messagebox.showinfo('Success','Login Successful  --  Welcome Mavericks')
        window.destroy()
                #***************    R E S T A R U N T   B I L I N G   S Y S T E M       *******************
        def total_():##defining total button as follows
            ##makking global use of a particular function
            global aprice,bprice,cprice,dprice,eprice,fprice,gprice,hprice,iprice,jprice
            global kprice,lprice,mprice,nprice,oprice,pprice,qprice,rprice,sprice,tprice
            global uprice,vprice,wprice,xprice,yprice,zprice,a1price,a2price,a3price,a4price
        #    global mytime
            ##giving the price for the dishes
            #**********************   S T A R T E R S     ********************#
            aprice=int(aEntry.get())*50.00
            bprice=int(bEntry.get())*150.00
            cprice=int(cEntry.get())*85.00
            dprice=int(dEntry.get())*35.00
            eprice=int(eEntry.get())*160.00
            fprice=int(fEntry.get())*190.00
            gprice=int(gEntry.get())*210.00
            hprice=int(hEntry.get())*150.00
            iprice=int(iEntry.get())*90.00
            jprice=int(jEntry.get())*60.00
            #**********************   M A I N   C O U R S E   V A L U E S ********************#
            kprice=int(kEntry.get())*200.00
            lprice=int(lEntry.get())*350.00
            mprice=int(mEntry.get())*210.00
            nprice=int(nEntry.get())*350.00
            oprice=int(oEntry.get())*250.00
            pprice=int(pEntry.get())*370.00
            qprice=int(qEntry.get())*400.00
            rprice=int(rEntry.get())*300.00
            sprice=int(sEntry.get())*250.00
            tprice=int(tEntry.get())*250.00
            #*********************    D E S S E R T   V A L U E S     *************************
            uprice=int(uEntry.get())*100.00
            vprice=int(vEntry.get())*250.00
            wprice=int(wEntry.get())*70.00
            xprice=int(xEntry.get())*230.00
            yprice=int(yEntry.get())*130.00
            zprice=int(zEntry.get())*70.00
            a1price=int(a1Entry.get())*350.00
            a2price=int(a2Entry.get())*80.00
            a3price=int(a3Entry.get())*250.00
            a4price=int(a4Entry.get())*250.00
            ##adding total costin the frame totframe
            totprice=(aprice+bprice+cprice+dprice+eprice+fprice+gprice+hprice+iprice
                        +jprice+kprice+lprice+mprice+nprice+oprice+pprice
                                +qprice+rprice+sprice+tprice+uprice+vprice+wprice
                        +xprice+yprice+zprice+a1price+a2price+a3price+a4price)
            totEntry.config(state='normal')
            totEntry.delete(0,END)##deleting preivious text wriiten in the entry field
            totEntry.insert(0,str(totprice)+' Rs')## inserting total price in the entry field
            totEntry.config(state='disabled')    
        #********************************************************************************************
        def bill_():
            billno = random.randint(100, 5000)
            billnoEntry.config(state='normal')
            billnoEntry.delete(0, END)
            billnoEntry.insert(0, billno)
            billnoEntry.config(state='disabled')    
            textarea.config(state='normal')
            currentdate = datetime.now().strftime('%d/%m/%y')
            currenttime = datetime.now().strftime('%I:%M:%S %p')
            dateEntry.config(state='normal')
            dateEntry.delete(0, END)
            timeEntry.config(state='normal')
            timeEntry.delete(0, END)
            dateEntry.insert(0, currentdate)
            dateEntry.config(state='disabled')
            timeEntry.insert(0, currenttime)
            timeEntry.config(state='disabled')

            if totEntry.get() == '':
                messagebox.showerror('Error', 'Select The Item')
                return
            elif totEntry.get() == '0 Rs':
                messagebox.showerror('Error', 'Select The Item')
                return
            elif modEntry.get() == '':
                messagebox.showerror('Error', 'Mode Of Payment -- Not Selected')
                return

            textarea.delete(1.0, END)
            textarea.insert(END, '\n\n          MAVERICKS  RESTAURANT (Pure non-veg)\n')
            textarea.insert(END, '\n' + '-' * 55)
            textarea.insert(END, f'\nBill Number: {billnoEntry.get()}')
            textarea.insert(END, '\n' + '-' * 55)
            if dateEntry.get() != '':
                textarea.insert(END, f'\nDate: {dateEntry.get()}')   
            if timeEntry.get() != '':
                textarea.insert(END, f'\nTime: {timeEntry.get()}')
            textarea.insert(END, '\n' + '-' * 55)
            textarea.insert(END, f"\n{'Dish':25}{'Qty':>5}{'Price':>12}")
            textarea.insert(END, '\n' + '-' * 55)

            

            def add_item(name, qty, price):
                if qty != '0':
                    line = f"\n{name:25}{qty:>5}{str(price)+' Rs':>12}"
                    textarea.insert(END, line)
                    

            # Add items if ordered
            add_item('Chicken Rolls', aEntry.get(), aprice)
            add_item('Chicken Burger', bEntry.get(), bprice)
            add_item('Chicken Fries', cEntry.get(), cprice)
            add_item('Bread Omellette', dEntry.get(), dprice)
            add_item('Meat Balls', eEntry.get(), eprice)
            add_item('Chicken Manchurian', fEntry.get(), fprice)
            add_item('Chilli Prawns', gEntry.get(), gprice)
            add_item('Fish Fries', hEntry.get(), hprice)
            add_item('Special Shawarma', iEntry.get(), iprice)
            add_item('Soups', jEntry.get(), jprice)
            add_item('Chicken Biriyani', kEntry.get(), kprice)
            add_item('Mutton Biriyani', lEntry.get(), lprice)
            add_item('Fish Biriyani', mEntry.get(), mprice)
            add_item('Prawn Biriyani', nEntry.get(), nprice)
            add_item('Butter Chicken', oEntry.get(), oprice)
            add_item('Tandoori Chicken', pEntry.get(), pprice)
            add_item('Grilled Chicken', qEntry.get(), qprice)
            add_item('Schezwan Chicken', rEntry.get(), rprice)
            add_item('Egg Curry', sEntry.get(), sprice)
            add_item('Fish Curry', tEntry.get(), tprice)
            add_item('Bread Halwa', uEntry.get(), uprice)
            add_item('Vanilla Frosting', vEntry.get(), vprice)
            add_item('Kulfi', wEntry.get(), wprice)
            add_item('Apple Pie', xEntry.get(), xprice)
            add_item('Chocolate Brownie', yEntry.get(), yprice)
            add_item('Pumpkin Cupcakes', zEntry.get(), zprice)
            add_item('Chocolate Cake', a1Entry.get(), a1price)
            add_item('Banana Bars', a2Entry.get(), a2price)
            add_item('Choco Truffle', a3Entry.get(), a3price)
            add_item('Red Velvet', a4Entry.get(), a4price)

            textarea.insert(END, '\n' + '-' * 55)
            totalbill = totEntry.get()
            textarea.insert(END, f"\n{'Total Bill':>30}{totalbill:>20}")
            textarea.insert(END, '\n' + '-' * 55)

            corc = modEntry.get()
            if modEntry.get() != '':
                textarea.insert(END, f'\nMode Of Payment: {corc}') 
                textarea.insert(END, '\n' + '-' * 55)

            textarea.insert(END, '\n        Thank you For Dining With Us :)')
            textarea.config(state='disable')

        #***************************************************************************************      
        #deleting all the values in he entryfields after clicking of clear button   
        def clear_():##deffining the clear button as follows
            aEntry.delete(0,END)
            bEntry.delete(0,END)
            cEntry.delete(0,END)
            dEntry.delete(0,END)
            eEntry.delete(0,END)
            fEntry.delete(0,END)
            gEntry.delete(0,END)
            hEntry.delete(0,END)
            iEntry.delete(0,END)
            jEntry.delete(0,END)
            kEntry.delete(0,END)
            lEntry.delete(0,END)
            mEntry.delete(0,END)
            nEntry.delete(0,END)
            oEntry.delete(0,END)
            pEntry.delete(0,END)
            qEntry.delete(0,END)
            rEntry.delete(0,END)
            sEntry.delete(0,END)
            tEntry.delete(0,END)
            uEntry.delete(0,END)
            vEntry.delete(0,END)
            wEntry.delete(0,END)
            xEntry.delete(0,END)
            yEntry.delete(0,END)
            zEntry.delete(0,END)
            a1Entry.delete(0,END)
            a2Entry.delete(0,END)
            a3Entry.delete(0,END)
            a4Entry.delete(0,END)
            totEntry.config(state='normal')
            totEntry.delete(0,END)
            totEntry.config(state='disabled')    
            ##deleting the text written on the text area after clicking the clear button
            textarea.config(state='normal')
            textarea.delete(1.0,END)
            textarea.config(state='disabled')
            ##deleting the text written on the entryfields of dt after clicking the clear button
            dateEntry.config(state='normal')
            dateEntry.delete(0,END)
            dateEntry.config(state='disabled')
            timeEntry.config(state='normal')
            timeEntry.delete(0,END)
            timeEntry.config(state='disabled')
            modEntry.config(state='normal')
            modEntry.delete(0,END)
            modEntry.config(state='disabled')
            billnoEntry.config(state='normal')
            billnoEntry.delete(0,END)
            billnoEntry.config(state='disabled')
        ##again we are inserting the value 0
            aEntry.insert(0,0)
            bEntry.insert(0,0)
            cEntry.insert(0,0)
            dEntry.insert(0,0)
            eEntry.insert(0,0)
            fEntry.insert(0,0)
            gEntry.insert(0,0)
            hEntry.insert(0,0)
            iEntry.insert(0,0)
            jEntry.insert(0,0)
            kEntry.insert(0,0)
            lEntry.insert(0,0)
            mEntry.insert(0,0)
            nEntry.insert(0,0)
            oEntry.insert(0,0)
            pEntry.insert(0,0)
            qEntry.insert(0,0)
            rEntry.insert(0,0)
            sEntry.insert(0,0)
            tEntry.insert(0,0)
            uEntry.insert(0,0)
            vEntry.insert(0,0)
            wEntry.insert(0,0)
            xEntry.insert(0,0)
            yEntry.insert(0,0)
            zEntry.insert(0,0)
            a1Entry.insert(0,0)
            a2Entry.insert(0,0)
            a3Entry.insert(0,0)
            a4Entry.insert(0,0)
        #*************************************************************************************
        def close_():
            win.destroy()

        def print_():
            if textarea.get(1.0,END)=='\n':
                messagebox.showerror('Error','Bill Is Empty')
            else:
                file=tempfile.mktemp('.txt')
                open(file,'w').write(textarea.get(1.0,END))
                os.startfile(file,'print')

            
            
                #**********  G U I (GRAPHICAL USER INTERFACE)  P A R T  *********#
                        #********   T K I N T E R   *******#
        
        win=tk.Tk()
        win.title('Restaurant Billing System')  ##giving title for the new window
        win.config(bg='#FAF3E0')  ##bg colour for window
        win.geometry('1319x634')  #giving geometry for the new window length x bregth
        win.resizable(0,0)  ##dont want to maximize the window

        headinglabel = Label(win, text="Mavericks Restaurant  (Pure non-veg) :)"
                            ,fg='yellow',bg='dark blue', font=("segoe script", 25, 'bold'))
        headinglabel.pack(fill='both',pady='2')  ##positioning the label
        ##making a frame
        dish1frame=Frame(win)
        dish1frame.config(bg='#FAF3E0')
        dish1frame.pack(fill='both')  ##positioning the frame
        ##making a frame for starters
        startersFrame=LabelFrame(dish1frame, text="Starters"
                                , font=("segoe script",21, 'bold',))
        startersFrame.config(fg='yellow')  ##foreground colour
        startersFrame.config(bg='dark blue')  ##background
        startersFrame.grid(row=0,column=0,padx='3')  #positioning
        # Allow only numbers or empty string
        def validate_int(P):
            if P.isdigit() or P == "":  
                return True
            return False
        vcmd = (win.register(validate_int), "%P")##copied from chatGPT
        #***************************************************************************************************
        def aclick(event):
            messagebox.showinfo('Message','Chicken Rolls - 50.00 Rs')
        def bclick(event):
            messagebox.showinfo('Message','Chicken Burger - 150.00 Rs')
        def cclick(event):
            messagebox.showinfo('Message','Chicken Fries - 85.00 Rs')
        def dclick(event):
            messagebox.showinfo('Message','Bread Omelette - 35.00')
        def eclick(event):
            messagebox.showinfo('Message','Meat Balls - 160.00 Rs')
        def fclick(event):
            messagebox.showinfo('Message','Chicken Manchurian - 190.00 Rs')
        def gclick(event):
            messagebox.showinfo('Message','Chilli Prawns - 210.00 Rs')
        def hclick(event):
            messagebox.showinfo('Message','Fish Fries - 150.00 Rs')
        def iclick(event):
            messagebox.showinfo('Message','Special Shawarma - 90.00 Rs')
        def jclick(event):
            messagebox.showinfo('Message','Soups - 60.00 Rs')
        def kclick(event):
            messagebox.showinfo('Message','Chicken Biriyani - 200.00 Rs')
        def lclick(event):
            messagebox.showinfo('Message','Mutton Biriyani - 350.00 Rs')
        def mclick(event):
            messagebox.showinfo('Message','Fish Biriyani - 210.00 Rs')
        def nclick(event):
            messagebox.showinfo('Message','Prawn Biriyani - 350.00 Rs')
        def oclick(event):
            messagebox.showinfo('Message','Butter Chicken - 250.00 Rs')
        def pclick(event):
            messagebox.showinfo('Message','Tandoori Chicken - 370.00 Rs')
        def qclick(event):
            messagebox.showinfo('Message','Grilled Chicken - 400.00 Rs')
        def rclick(event):
            messagebox.showinfo('Message',' Schezwan Chicken - 300.00 Rs')
        def sclick(event):
            messagebox.showinfo('Message',' Egg Curry - 250.00 Rs')
        def tclick(event):
            messagebox.showinfo('Message',' Fish Curry - 250.00 Rs')
        def uclick(event):
            messagebox.showinfo('Message',' Bread Halwa - 100.00 Rs')
        def vclick(event):
            messagebox.showinfo('Message','Vanilla Frosting  - 250.00 Rs')
        def wclick(event):
            messagebox.showinfo('Message',' Kulfi - 70.00 Rs')
        def xclick(event):
            messagebox.showinfo('Message',' Apple Pie - 230.00 Rs')
        def yclick(event):
            messagebox.showinfo('Message',' Chocolate Brownie - 130.00 Rs')
        def zclick(event):
            messagebox.showinfo('Message',' Pumpkin Cupcakes - 70.00 Rs')
        def a1click(event):
            messagebox.showinfo('Message',' Chocolate Cake - 350.00 Rs')
        def a2click(event):
            messagebox.showinfo('Message',' Banana Bars - 80.00 Rs')
        def a3click(event):
            messagebox.showinfo('Message',' Choco Truffle - 250.00 Rs')
        def a4click(event):
            messagebox.showinfo('Message',' Red Velvet - 250.00 Rs')
        ##copied from chatGPT
        #***************************************************************************************************************
        ##adding of chiken spring roll in starters frame
        ##a(chicken)
        aLabel=Label(startersFrame, text="Chicken Rolls"
                                , font=("times new roman", 17, 'bold'))
        aLabel.config(fg='#FAF3E0')  ##foreground colour
        aLabel.config(bg='dark blue')  ##background colour
        aLabel.grid(row=0,column=0)  ##positioning
        aLabel.bind('<Button-1>',aclick)
        aEntry=Entry(startersFrame, validate="key", validatecommand=vcmd,width=5,bd='3')  ##entry field
        aEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        aEntry.grid(row=0,column=1)  ##positioning into the startersframe
        ##acheck=tk.Checkbutton(startersFrame)
        ##acheck.grid(row=0,column=0)
        ##adding of burger in starters frame
        ##b(burger)
        bLabel=Label(startersFrame, text="Chicken Burger"
                                , font=("times new roman", 17, 'bold',))
        bLabel.config(fg='#FAF3E0')  ## foreground colour
        bLabel.config(bg='dark blue')  ##background colour
        bLabel.grid(row=1,column=0)   #positioning
        bLabel.bind('<Button-1>',bclick)
        bEntry=Entry(startersFrame, validate="key", validatecommand=vcmd,width=5,bd='3')  ##entry field
        bEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        bEntry.grid(row=1,column=1)   ##positioning into the startersframe
        ##adding of Chicken Fries in starters frame
        ##c(Chicken Fries)
        cLabel=Label(startersFrame, text="Chicken Fries"
                                , font=("times new roman", 17, 'bold',))
        cLabel.config(fg='#FAF3E0')  ##foreground colour
        cLabel.config(bg='dark blue')  ##background colour
        cLabel.grid(row=2,column=0)    #positioning
        cLabel.bind('<Button-1>',cclick)
        cEntry=Entry(startersFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        cEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        cEntry.grid(row=2,column=1)     ##positioning into the startersframe
        ##adding of bread omllette in starters frame
        ##d(bread omellete)
        dLabel=tk.Label(startersFrame, text="Bread Omellette"
                                , font=("times new roman", 17, 'bold',))
        dLabel.config(fg='#FAF3E0')  ##foreground colour colour
        dLabel.config(bg='dark blue')  ##background colour
        dLabel.grid(row=3,column=0)    #positioning
        dLabel.bind('<Button-1>',dclick)
        dEntry=Entry(startersFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        dEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        dEntry.grid(row=3,column=1)     ##positioning into the startersframe
        ##adding of meat balls in starters frame
        ##e(meat balls)
        eLabel=Label(startersFrame, text="Meat Balls "
                                , font=("times new roman", 17, 'bold',))
        eLabel.config(fg='#FAF3E0')  ##foreground colour colour
        eLabel.config(bg='dark blue')  ##background colour
        eLabel.grid(row=4,column=0)    #positioning
        eLabel.bind('<Button-1>',eclick)
        eEntry=Entry(startersFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        eEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        eEntry.grid(row=4,column=1)     ##positioning into the startersframe
        ##adding of chicken manchurian in starters frame
        ##f(chicken manchurian)
        fLabel=Label(startersFrame, text="Chicken Manchurian "
                                , font=("times new roman", 17, 'bold',))
        fLabel.config(fg='#FAF3E0')  ##foreground colour colour
        fLabel.config(bg='dark blue')  ##background colour
        fLabel.grid(row=5,column=0)    #positioning
        fLabel.bind('<Button-1>',fclick)
        fEntry=Entry(startersFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        fEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        fEntry.grid(row=5,column=1)     ##positioning into the startersframe                     
        ##adding of chilli prawns in starters frame
        ##g(chilli prawns)
        gLabel=Label(startersFrame, text="Chilli Prawns "
                                , font=("times new roman", 17, 'bold',))
        gLabel.config(fg='#FAF3E0')  ##foreground colour colour
        gLabel.config(bg='dark blue')  ##background colour
        gLabel.grid(row=6,column=0)    #positioning
        gLabel.bind('<Button-1>',gclick)
        gEntry=Entry(startersFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        gEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        gEntry.grid(row=6,column=1)     ##positioning into the startersframe
        ##adding of fish Chicken Fries in starters frame
        ##h(Chicken Fries )
        hLabel=Label(startersFrame, text="Fish Fries"
                                , font=("times new roman", 17, 'bold',))
        hLabel.config(fg='#FAF3E0')  ##foreground colour colour
        hLabel.config(bg='dark blue')  ##background colour
        hLabel.grid(row=7,column=0)    #positioning
        hLabel.bind('<Button-1>',hclick)
        hEntry=Entry(startersFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        hEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        hEntry.grid(row=7,column=1)     ##positioning into the startersframe
        ##adding of chicken shawarma in starters frame
        ##i(chicken shawarma)
        iLabel=Label(startersFrame, text="Special Shawarma"
                        , font=("times new roman", 17, 'bold',))
        iLabel.config(fg='#FAF3E0')  ##foreground colour colour
        iLabel.config(bg='dark blue')  ##background colour
        iLabel.grid(row=8,column=0)    #positioning
        iLabel.bind('<Button-1>',iclick)
        iEntry=Entry(startersFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        iEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        iEntry.grid(row=8,column=1)     ##positioning into the startersframe
        ##adding of soups in starters frame
        ##j(soups)
        jLabel=Label(startersFrame, text="Soups"
                                , font=("times new roman", 17, 'bold',))
        jLabel.config(fg='#FAF3E0')  ##foreground colour colour
        jLabel.config(bg='dark blue')  ##background colour
        jLabel.grid(row=9,column=0)    #positioning
        jLabel.bind('<Button-1>',jclick)
        jEntry=Entry(startersFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        jEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        jEntry.grid(row=9,column=1,padx=7)     ##positioning into the startersframe
            #*************    M A I N   C O U R C E   F R A M E      *************#
        ##making a frame2 for starters
        maincourseFrame=LabelFrame(dish1frame, text="Main Course"
                                , font=("segoe script", 21, 'bold',))
        maincourseFrame.config(fg='yellow')  ##foreground colour
        maincourseFrame.config(bg='dark blue')  ##background
        maincourseFrame.grid(row=0,column=1,padx='3')  #positioning
        ##adding of chicken biriyani in main course frame
        ##k(chicken biriyani)
        kLabel=Label(maincourseFrame, text="Chicken Biriyani "
                                ,font=("times new roman", 17, 'bold',))
        kLabel.config(fg='#FAF3E0')  ##foreground colour colour
        kLabel.config(bg='dark blue')  ##background colour
        kLabel.grid(row=0,column=0)    #positionin
        kLabel.bind('<Button-1>',kclick)
        kEntry=Entry(maincourseFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        kEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        kEntry.grid(row=0,column=1,padx=7)  ##positioning into the maincourseframe
        ##adding of Mutton biriyani in main course frame
        ##l(muttoon biriyani)
        lLabel=Label(maincourseFrame, text="Mutton Biriyani "
                                , font=("times new roman", 17, 'bold',))
        lLabel.config(fg='#FAF3E0')  ##foreground colour colour
        lLabel.config(bg='dark blue')  ##background colour
        lLabel.grid(row=1,column=0)    #positionin
        lLabel.bind('<Button-1>',lclick)
        lEntry=Entry(maincourseFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        lEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        lEntry.grid(row=1,column=1)   ##positioning into the maincourseframe
        ##adding of fish biriyani in main course frame
        #m(fish biriyani)
        mLabel=Label(maincourseFrame, text="Fish Biriyani "
                                , font=("times new roman", 17, 'bold',))
        mLabel.config(fg='#FAF3E0')  ##foreground colour colour
        mLabel.config(bg='dark blue')  ##background colour
        mLabel.grid(row=2,column=0)    #positioning
        mLabel.bind('<Button-1>',mclick)
        mEntry=Entry(maincourseFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        mEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        mEntry.grid(row=2,column=1)     ##positioning into the maincourseframe
        ##adding of prawn biriyani in main course frame
        ##n(prawn biriyani)
        nLabel=Label(maincourseFrame, text="Prawn Biriyani "
                                , font=("times new roman", 17, 'bold',))
        nLabel.config(fg='#FAF3E0')  ##foreground colour colour
        nLabel.config(bg='dark blue')  ##background colour
        nLabel.grid(row=3,column=0)    #positioning
        nLabel.bind('<Button-1>',nclick)
        nEntry=Entry(maincourseFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        nEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        nEntry.grid(row=3,column=1)     ##positioning into the maincourseframe
        ##adding of butter chicken in main course frame2
        ##o(butter chicken)
        oLabel=Label(maincourseFrame, text="Butter Chicken "
                                , font=("times new roman", 17, 'bold',))
        oLabel.config(fg='#FAF3E0')  ##foreground colour colour
        oLabel.config(bg='dark blue')  ##background colour
        oLabel.grid(row=4,column=0)    #positioning
        oLabel.bind('<Button-1>',oclick)
        oEntry=Entry(maincourseFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        oEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        oEntry.grid(row=4,column=1)     ##positioning into the maincourseframe
        ##adding of tandoori chicken in main course frame
        ##p(tandoori chicken)
        pLabel=Label(maincourseFrame, text="Tandoori Chicken "
                            , font=("times new roman", 17, 'bold',))
        pLabel.config(fg='#FAF3E0')  ##foreground colour colour
        pLabel.config(bg='dark blue')  ##background colour
        pLabel.grid(row=5,column=0)    #positioning
        pLabel.bind('<Button-1>',pclick)
        pEntry=Entry(maincourseFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        pEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        pEntry.grid(row=5,column=1)     ##positioning into the maincourseframe
        ##adding of grillled chicken in main course frame
        ##q(grilled chicken)
        qLabel=Label(maincourseFrame, text="Grilled Chicken "
                            , font=("times new roman", 17, 'bold',))
        qLabel.config(fg='#FAF3E0')  ##foreground colour colour
        qLabel.config(bg='dark blue')  ##background colour
        qLabel.grid(row=6,column=0)    #positioning
        qLabel.bind('<Button-1>',qclick)
        qEntry=Entry(maincourseFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        qEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        qEntry.grid(row=6,column=1)     ##positioning into the maincourseframe
        ##adding of schezwan chicken in main course frame
        ##r(schezwan chicken)
        rLabel=Label(maincourseFrame, text="Schezwan Chicken  "
                            , font=("times new roman", 17, 'bold',))
        rLabel.config(fg='#FAF3E0')  ##foreground colour colour
        rLabel.config(bg='dark blue')  ##background colour
        rLabel.grid(row=7,column=0)    #positioning
        rLabel.bind('<Button-1>',rclick)
        rEntry=Entry(maincourseFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        rEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        rEntry.grid(row=7,column=1)     ##positioning into the maincourseframe
        ##adding of egg curry in main course frame
        ##s(egg curry)
        sLabel=Label(maincourseFrame, text="Egg Curry "
                            , font=("times new roman", 17, 'bold',))
        sLabel.config(fg='#FAF3E0')  ##foreground colour colour
        sLabel.config(bg='dark blue')  ##background colour
        sLabel.grid(row=8,column=0)    #positioning
        sLabel.bind('<Button-1>',sclick)
        sEntry=Entry(maincourseFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        sEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        sEntry.grid(row=8,column=1)     ##positioning into maincourseframe
        ##adding of fish curry in main course frame
        ##t(fish curry)
        tLabel=Label(maincourseFrame, text="Fish Curry "
                            , font=("times new roman", 17, 'bold',))
        tLabel.config(fg='#FAF3E0')  ##foreground colour colour
        tLabel.config(bg='dark blue') ##background colour
        tLabel.grid(row=9,column=0)    ##positioning
        tLabel.bind('<Button-1>',tclick)
        tEntry=Entry(maincourseFrame, validate="key", validatecommand=vcmd,width=5,bd='3')  ##entry field
        tEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        tEntry.grid(row=9,column=1)     ##positioning into the maincourseframe

            #***********************    D E S E R T  F R A M E     *********************#
        ##making a frame3 for dessert
        dessertFrame=LabelFrame(dish1frame, text="Dessert"
                                , font=("segoe script", 21, 'bold',))
        dessertFrame.config(fg='yellow')  ##foreground colour
        dessertFrame.config(bg='dark blue')  ##background colour
        dessertFrame.grid(row=0,column=2,padx=3)  #positioning
        ##adding of bread halwa in main course frame
        ##u(breadhalwa)
        uLabel=Label(dessertFrame, text="Bread Halwa "
                                , font=("times new roman", 17, 'bold',))
        uLabel.config(fg='#FAF3E0')  ##foreground colour colour
        uLabel.config(bg='dark blue')  ##background colour
        uLabel.grid(row=0,column=0)    #positioning
        uLabel.bind('<Button-1>',uclick)
        uEntry=Entry(dessertFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        uEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        uEntry.grid(row=0,column=1)     ##positioning into the dessertsframe
        ##adding of  Vanilla Frosting in main course frame
        ##v(chocolate Cake With Vanilla Frosting
        vLabel=Label(dessertFrame, text="Vanilla Frosting "
                    , font=("times new roman", 17, 'bold',))
        vLabel.config(fg='#FAF3E0')  ##foreground colour colour
        vLabel.config(bg='dark blue')  ##background colour
        vLabel.grid(row=1,column=0)    #positioning
        vLabel.bind('<Button-1>',vclick)
        vEntry=Entry(dessertFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        vEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        vEntry.grid(row=1,column=1)     ##positioning into the dessertframe)
        ##adding of kulfi in main course frame
        ##w(kulfi)
        wLabel=Label(dessertFrame, text="Kulfi "
                            , font=("times new roman", 17, 'bold',))
        wLabel.config(fg='#FAF3E0')  ##foreground colour colour
        wLabel.config(bg='dark blue')  ##background colour
        wLabel.grid(row=2,column=0)    #positioning
        wLabel.bind('<Button-1>',wclick)
        wEntry=Entry(dessertFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        wEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        wEntry.grid(row=2,column=1)     ##positioning into the dessertframe
        ##adding of apple pie in main course frame
        ##x(apple pie)
        xLabel=Label(dessertFrame, text="Apple Pie "
                                , font=("times new roman", 17, 'bold',))
        xLabel.config(fg='#FAF3E0')  ##foreground colour colour
        xLabel.config(bg='dark blue')  ##background colour
        xLabel.grid(row=3,column=0)    #positioning
        xLabel.bind('<Button-1>',xclick)
        xEntry=Entry(dessertFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        xEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        xEntry.grid(row=3,column=1)     ##positioning into the dessertframe
        ##adding of chocolate brownie in main course frame
        ##y(cbrownie)
        yLabel=Label(dessertFrame, text="Chocolate brownie "
                                , font=("times new roman", 17, 'bold',))
        yLabel.config(fg='#FAF3E0')  ##foreground colour colour
        yLabel.config(bg='dark blue')  ##background colour
        yLabel.grid(row=4,column=0)    #positioning
        yLabel.bind('<Button-1>',yclick)
        yEntry=Entry(dessertFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field\
        yEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        yEntry.grid(row=4,column=1)     ##positioning into the dessertframe
        ##adding of Pumpkin cupcakes in main course frame
        ##z(Pumpkin cupcakes)
        zLabel=Label(dessertFrame, text="Pumpkin Cupcakes "
                        , font=("times new roman", 17, 'bold',))
        zLabel.config(fg='#FAF3E0')  ##foreground colour colour
        zLabel.config(bg='dark blue')  ##background colour
        zLabel.grid(row=5,column=0)    #positioning
        zLabel.bind('<Button-1>',zclick)
        zEntry=Entry(dessertFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        zEntry.insert(0,0)  ##inserting '0' after clicking the button clear
        zEntry.grid(row=5,column=1)     ##positioning into the dessertframe)
        ##adding of chocolate cake in main course frame
        ##a1(chocolate cake)
        a1Label=Label(dessertFrame, text="Chocolate Cake "
                        , font=("times new roman", 17, 'bold',))
        a1Label.config(fg='#FAF3E0')  ##foreground colour colour
        a1Label.config(bg='dark blue')  ##background colour
        a1Label.grid(row=6,column=0)    #positioning
        a1Label.bind('<Button-1>',a1click)
        a1Entry=Entry(dessertFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        a1Entry.insert(0,0)  ##inserting '0' after clicking the button clear
        a1Entry.grid(row=6,column=1)     ##positioning into the dessertframe)
        ##adding of Banana bars in main course frame
        ##a2(Banana bars)
        a2Label=Label(dessertFrame, text="Banana Bars "
                        , font=("times new roman", 17, 'bold',))
        a2Label.config(fg='#FAF3E0')  ##foreground colour colour
        a2Label.config(bg='dark blue')  ##background colour
        a2Label.grid(row=7,column=0)    #positioning
        a2Label.bind('<Button-1>',a2click)
        a2Entry=Entry(dessertFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        a2Entry.insert(0,0)  ##inserting '0' after clicking the button clear
        a2Entry.grid(row=7,column=1)     ##positioning into the dessertframe)
        ##adding of choco truffle in main course frame
        ##a3(choco truffle)
        a3Label=Label(dessertFrame, text="Choco Truffle "
                        , font=("times new roman", 17, 'bold',))
        a3Label.config(fg='#FAF3E0')  ##foreground colour colour
        a3Label.config(bg='dark blue')  ##background colour
        a3Label.grid(row=8,column=0)    #positioning
        a3Label.bind('<Button-1>',a3click)
        a3Entry=Entry(dessertFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        a3Entry.insert(0,0)  ##inserting '0' after clicking the button clear
        a3Entry.grid(row=8,column=1)     ##positioning into the dessertframe)
        ##adding of red velvet in main course frame
        ##a4(red velvet)
        a4Label=Label(dessertFrame, text="Red Velvet "
                        , font=("times new roman", 17, 'bold',))
        a4Label.config(fg='#FAF3E0')  ##foreground colour colour
        a4Label.config(bg='dark blue')  ##background colour
        a4Label.grid(row=9,column=0)    #positioning
        a4Label.bind('<Button-1>',a4click)
        a4Entry=Entry(dessertFrame, validate="key", validatecommand=vcmd,width=5,bd='3')   ##entry field
        a4Entry.insert(0,0)  ##inserting '0' after clicking the button clear
        a4Entry.grid(row=9,column=1,padx=5)     ##positioning into the dessertframe)

            #*********************   B I L L I N G  A R E A   **********************
        ##making billframe
        billframe=Frame(dish1frame)
        billframe.grid(row=0,column=3,padx='5',sticky='s')
        ##making bilarealabel inside the billfframe
        billarealabel=Label(billframe ,text="C u s t o m e r  B i l l"
                        , font=("Courier New", 17, 'bold'),bg='dark blue',fg='yellow')
        billframe.config(bg='dark blue')
        billframe.config(bd='8')
        billframe.config(relief='groove')
        billarealabel.pack()
        ##making sccroolbar in billframe
        scrollbar=Scrollbar(billframe,orient='vertical')##placiing scroolbar in vertical
        scrollbar.pack(side='right',fill='y')##positioning at right side to the text area
        ##making textarea in billframe
        textarea=Text(billframe,height=16,width=57,yscrollcommand=scrollbar.set,state='disabled')
        textarea.pack()
        ##configuring scrollbar too view text
        scrollbar.config(command=textarea.yview)

        billnoframe=LabelFrame(dish1frame,bd='8',bg='dark blue')
        billnoframe.grid(row=0,column=3,sticky='n')
        billnolabel=Label(billnoframe,text='                Bill Number :  '
                        ,font=('segoe script',13,'bold'),fg='yellow',bg='dark blue',bd='1')
        billnolabel.grid(row=0,column=0)
        billnoEntry=Entry(billnoframe,width=5,font=('arial',12),bd='5')
        billnoEntry.config(state='disabled')
        billnoEntry.grid(row=0,column=1,padx=20)
        space=Label(billnoframe,text='                                     ',bg='dark blue')
        space.grid(row=0,column=2)
        ##making a labelframe for bil menu
        ##bm(billmenu)
        bmFrame=LabelFrame(win, text=""
                                , font=("times new roman", 21, 'bold',))
        bmFrame.config(fg='yellow')  ##foreground colour
        bmFrame.config(bg='dark blue')  ##background colour
        bmFrame.config(bd='7')  ## border size
        bmFrame.pack(fill='both',padx=7,pady=7)  #positioning
        ##adding of total price in  frame
        ##tot(total price)
        totprice=Label(bmFrame, text="Total Price : "
                                , font=("segoe script", 25, 'bold',))
        totprice.config(fg='yellow')  ##foreground colour colour
        totprice.config(bg='dark blue')  ##background colour
        totprice.grid(row=0,column=0,padx=15)    #positioning
        totEntry=Entry(bmFrame,font=('arial',28),width=12,bd='5')   ##entry field
        totEntry.config(state='disabled')
        totEntry.grid(row=0,column=1,padx=10,pady=5)     ##positioning
        ##adding of total price in  frame
        ##mod(mod of pyment)
        modpay=Label(bmFrame, text="Mode Of Payment : "
                                , font=("segoe script", 18, 'bold',))
        modpay.config(fg='yellow')  ##foreground colour colour
        modpay.config(bg='dark blue')  ##background colour
        modpay.grid(row=0,column=2,padx=5)    #positioning

        def cash_():  
            modEntry.config(state='normal')
            modEntry.delete(0,END)
            modEntry.insert(0,'CASH')
            modEntry.config(state='disabled')
        ##creating total button
        cashbutton=Button(bmFrame, text="Cash"
                            , font=("times new roman", 17, 'bold',))
        cashbutton.config(fg='#FAF3E0')  ##foreground colour colour
        cashbutton.config(bg='dark blue')  ##background colour
        cashbutton.config(bd='5')
        cashbutton.config(width='5')
        cashbutton.config(command=cash_)
        cashbutton.grid(row=0,column=3,pady=5,)
        def card_():
            modEntry.config(state='normal')
            modEntry.delete(0,END)
            modEntry.insert(0,'CARD')
            modEntry.config(state='disabled')
        ##creating total button
        cardbutton=Button(bmFrame, text="Card"
                            , font=("times new roman", 17, 'bold',))
        cardbutton.config(fg='#FAF3E0')  ##foreground colour colour
        cardbutton.config(bg='dark blue')  ##background colour
        cardbutton.config(command=card_)
        cardbutton.grid(row=0,column=4,padx=35,pady=5)
        def upi_():
            modEntry.config(state='normal')
            modEntry.delete(0,END)
            modEntry.insert(0,'UPI')
            modEntry.config(state='disabled')
        ##creating total button
        upibutton=Button(bmFrame, text="UPI"
                            , font=("times new roman", 17, 'bold',))
        cardbutton.config(bd='5')
        cardbutton.config(width='5')
        upibutton.config(fg='#FAF3E0')  ##foreground colour colour
        upibutton.config(bg='dark blue')  ##background colour
        upibutton.config(bd='5')
        upibutton.config(width='5')
        upibutton.config(command=upi_)
        upibutton.grid(row=0,column=5,pady=5,)

        modEntry=Entry(bmFrame,font=('arial',20),width=5,bd='5')   ##entry field
        #******************************************************************************************
        modEntry.config(state='disabled')
        modEntry.grid(row=0,column=6,padx=37,pady=5)     ##positioning

        ##making a labelframe for bil menu
        ##button
        buttonframe=LabelFrame(win, text=""
                                , font=("times new roman", 21, 'bold',))
        buttonframe.config(fg='yellow')  ##foreground
        buttonframe.config(bg='dark blue')  ##background colour
        buttonframe.config(bd='7')  ## border size
        buttonframe.pack()  #positioning
        ##creating total button
        totalbutton=Button(buttonframe, text="Total "
                            , font=("times new roman", 20, 'bold',))
        totalbutton.config(fg='#FAF3E0')  ##foreground colour colour
        totalbutton.config(bg='dark blue')  ##background colour
        totalbutton.config(bd='5')
        totalbutton.config(width='7')
        totalbutton.config(command=total_)
        totalbutton.grid(row=1,column=0,padx=40,pady=5,rowspan=2)
        ##creating bill button
        billbutton=Button(buttonframe, text="Bill "
                            , font=("times new roman", 20, 'bold',))
        billbutton.config(fg='#FAF3E0')  ##foreground colour colour
        billbutton.config(bg='dark blue')  ##background colour
        billbutton.config(bd='5')
        billbutton.config(width='7')
        billbutton.config(command=bill_)
        billbutton.grid(row=1,column=1,padx=40,rowspan=2)
        ##creating print button
        printbutton=Button(buttonframe, text="Print "
                            , font=("times new roman", 20, 'bold',))
        printbutton.config(fg='#FAF3E0')  ##foreground colour colour
        printbutton.config(bg='dark blue')  ##background colour
        printbutton.config(bd='5')
        printbutton.config(width='7')
        printbutton.config(command=print_)
        printbutton.grid(row=1,column=2,padx=40,rowspan=2)
        ##creating clear button
        clearbutton=Button(buttonframe, text="Clear "
                            , font=("times new roman", 20, 'bold'))
        clearbutton.config(fg='#FAF3E0')  ##foreground colour colour
        clearbutton.config(bg='dark blue')  ##background colour
        clearbutton.config(bd='5')
        clearbutton.config(width='7')
        clearbutton.config(command=clear_)
        clearbutton.grid(row=1,column=3,padx=40,rowspan=2)

        ##creating close button
        closebutton=Button(buttonframe, text="Close "
                            , font=("times new roman", 20, 'bold',))
        closebutton.config(fg='#FAF3E0')  ##foreground colour colour
        closebutton.config(bg='dark blue')  ##background colour
        closebutton.config(bd='5')
        closebutton.config(width='7')
        closebutton.config(command=close_)
        closebutton.grid(row=1,column=4,padx=40,rowspan=2)

        datelabel=Label(buttonframe,text='Date: ',font=('segoe script',20))
        datelabel.config(fg='yellow',bg='dark blue')
        datelabel.grid(row=1,column=5,)
        dateEntry=Entry(buttonframe,font=('arial',17),width=7,bd='5',state='disabled')   ##entry field
        dateEntry.grid(row=1,column=6,pady=6)     ##positioning

        timelabel=Label(buttonframe,text='Time: ',font=('segoe script',20))
        timelabel.config(fg='yellow',bg='dark blue')
        timelabel.grid(row=2,column=5)
        timeEntry=Entry(buttonframe,font=('arial',17),width=10,bd='5',state='disabled')   ##entry field
        timeEntry.grid(row=2,column=6,pady=6,padx=10)     ##positioning
        #*************************************************************************************
        ##for looping
        win.mainloop()
                            ###################################################

        
        
    else:
        messagebox.showerror('Error','Please Enter The Correct Credentials')


def close():
    window.destroy()

window=tk.Tk()
window.geometry('700x460+330+100')
window.title('Restaurunt Billing System')  ##giving title for the new window
window.config(bg='dark blue')  ##bg colour for window
window.resizable(False,False)

loginlabel=Label(window,text='LOGIN',fg='yellow',bg='dark blue',font=("times new roman", 40, 'bold'),bd=7,relief='groove')
loginlabel.pack(fill='x')

loginframe=Frame(window,bg='dark blue',bd=7,relief='groove')
loginframe.place(x=400,y=150)
loginframe.pack(fill='both')

usernamelabel=Label(loginframe,text='Username',fg='white',bg='dark blue', font=("segoe script", 25, 'bold'))
usernamelabel.grid(row=0,column=0,ipadx=100,ipady=50,)

usernameentry=Entry(loginframe,width=15,font=('arial',17),bd=5)
usernameentry.grid(row=0,column=1)

passwordlabel=Label(loginframe,text='Password',fg='white',bg='dark blue', font=("segoe script", 25, 'bold'))
passwordlabel.grid(row=1,column=0,)

passwordentry=Entry(loginframe,width=15,font=('arial',17),bd=5)
passwordentry.grid(row=1,column=1)

loginbutton=Button(loginframe,text='Login',fg='white',bg='dark blue', font=("segoe script", 20, 'bold')
                   ,bd=7,cursor='hand2',command=login)
loginbutton.grid(row=2,column=0,ipadx=30,pady=45,columnspan=1)

closebutton=Button(loginframe,text='Close',fg='white',bg='dark blue', font=("segoe script", 20, 'bold')
                   ,bd=7,cursor='hand2',command=close)
closebutton.grid(row=2,column=1,ipadx=30,pady=45,columnspan=1)


window.mainloop()

