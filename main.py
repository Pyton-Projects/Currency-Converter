import tkinter.ttk
from tkinter import*
from ttkthemes import ThemedTk
from tkinter import messagebox
from currency_converter import CurrencyConverter
converter_=CurrencyConverter()
root=ThemedTk(themebg=True)
currencies_form=('Us Dollar (USD)','Indian Rupee (INR)','Japanese yen (JPY)','Bulgarian lev (BGN)','Czech koruna (CZK)','Danish krone (DKK)','Hungarian forint (HUF)','Polish zloty (PLN)','Romanian leu (RON)','Swedish krona (SEK)','Swiss franc (CHF)','Icelandic krona (ISK)','Norwegian krone (NOK)','Croatian kuna (HRK)','Russian rouble (RUB)','Turkish lira (TRY)','Australian dollar (AUD)','Brazilian real (BRL)','Canadian dollar (CAD)','Hong Kong dollar (HKD)','Indonesian rupiah (IDR)','Israeli shekel (ILS)','South Korean won (KRW)','Mexican peso (MXN)','Malaysian ringgit (MYR)','New Zealand dollar (NZD)','Philippine peso (PHP)','Singapore dollar (SGD)','Thai baht (THB)','South African rand (ZAR)')
currencies_to=('Us Dollar (USD)','Indian Rupee (INR)','Japanese yen (JPY)','Bulgarian lev (BGN)','Czech koruna (CZK)','Danish krone (DKK)','Hungarian forint (HUF)','Polish zloty (PLN)','Romanian leu (RON)','Swedish krona (SEK)','Swiss franc (CHF)','Icelandic krona (ISK)','Norwegian krone (NOK)','Croatian kuna (HRK)','Russian rouble (RUB)','Turkish lira (TRY)','Australian dollar (AUD)','Brazilian real (BRL)','Canadian dollar (CAD)','Hong Kong dollar (HKD)','Indonesian rupiah (IDR)','Israeli shekel (ILS)','South Korean won (KRW)','Mexican peso (MXN)','Malaysian ringgit (MYR)','New Zealand dollar (NZD)','Philippine peso (PHP)','Singapore dollar (SGD)','Thai baht (THB)','South African rand (ZAR)')
root.set_theme('ubuntu')
root.title('CurrencyConverter')
root.minsize(450,200)
root.maxsize(450,200)
heading=ttk.Label(root,text='Currency Converter',font=('Courier',15,'bold'))
heading.pack()
currency_value=StringVar()
currencies_value_to=StringVar()
Amount_value=StringVar()
from_=ttk.Combobox(root,value=currencies_form,width=22,textvariable=currency_value)
from_.place(x=50,y=40)
currency_value.set('Us Dollar (USD)')
currencies_value_to.set('Indian Rupee (INR)')
to_=ttk.Combobox(root,value=currencies_to,width=22,textvariable=currencies_value_to)
to_.place(x=295,y=40)
from_['state']='readonly'
to_['state']='readonly'
def conversion():
	reverse=(currency_value.get()[::-1])
	codes_=(reverse[1:4:])
	working_codes_from=codes_[::-1]
	reverse_1=(currencies_value_to.get()[::-1])
	codes_1=(reverse_1[1:4:])
	working_codes_to=codes_1[::-1]
	try:
		error_handling=int(Amount_value.get())
	except Exception:
		messagebox.showinfo('Info','Please Enter A Number!')
	try:

		Va=converter_.convert(error_handling,working_codes_from,working_codes_to)
		four_value=format(Va,'.4f')
		amount=Amount_.set(four_value)
		messagebox.showinfo('Info',f'Converted Value Is {four_value}')
	except UnboundLocalError:
		''
from_indiacator=ttk.Label(root,text='From')
from_indiacator.place(x=1,y=40)
Label_=ttk.Label(root,text='Enter Amount Down Below To Convert',font=('Courier',8))
Label_.place(x=1,y=70)
input_=Entry(root,width=20,textvariable=Amount_value)
input_.place(x=1,y=100)
convert_=ttk.Button(root,text='Convert',width=8,command=conversion)
convert_.place(y=90,x=200)
Amount_=IntVar()
result=ttk.Label(root,text='Converted Amount--:')
result.place(x=1 ,y=140)
amount_reslut=ttk.Label(root,textvariable=Amount_,text='bruh')
amount_reslut.place(x=137 ,y=140)
to=ttk.Label(root,text='To')
to.place(y=40,x=235)
mainloop()
# short the value
