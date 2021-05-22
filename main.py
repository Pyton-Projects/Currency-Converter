import tkinter.ttk
from tkinter import*
from ttkthemes import ThemedTk
from tkinter import messagebox
from google_currency import convert  
import re
root=ThemedTk(themebg=True)
currencies_form=('Us Dollar (USD)','Indian Rupee (INR)','Japanese yen (JPY)','Euro (EUR)','Bulgarian lev (BGN)','Czech koruna (CZK)','Danish krone (DKK)','Hungarian forint (HUF)','Polish zloty (PLN)','Swedish krona (SEK)','Swiss franc (CHF)','Icelandic krona (ISK)','Norwegian krone (NOK)','Croatian kuna (HRK)','Russian rouble (RUB)','Turkish lira (TRY)','Australian dollar (AUD)','Brazilian real (BRL)','Canadian dollar (CAD)','Hong Kong dollar (HKD)','Indonesian rupiah (IDR)','South Korean won (KRW)','Mexican peso (MXN)','Malaysian ringgit (MYR)','New Zealand dollar (NZD)','Philippine peso (PHP)','Singapore dollar (SGD)','Thai baht (THB)','South African rand (ZAR)','Vietnamese Dong (VND)','Uzbekistani Som (UZS)','Uruguayan Peso (UYU)','British Pound (GBP)','Ukrainian Hryvnia (UAH)','Ugandan Shilling (UGX)','Tunisian Dinar (TND)','Tanzanian Shilling (TZS)','New Taiwan Dollar (TWD)','Swiss Franc (CHF)','Sri Lankan Rupee (LKR)','Singapore Dollar (SGD)','Saudi Riyal (SAR)','Poland Złoty (PLN)','Peruvian Sol (PEN)','Paraguay Guarani (PYG)','Panamanian Balboa (PAB)','Pakistani Rupee (PKR)','Omani Rial (OMR)','Norwegian Krone (NOK)','Nigerian Naira (NGN)','Nicaraguan Cordoba (NIO)','New Zealand Dollar (NZD)','Nepalese Rupee (NPR)','Burmese Kyat (MMK)','Moroccan Dirham (MAD)','Mexican Peso (MXN)','Mauritian Rupee (MUR)','Malaysia Ringgit (MYR)','Lebanese Pound (LBP)','Kuwaiti Dinar (KWD)','Kenyan Shilling (KES)','Kazakhstani Tenge (KZT)','Jordanian Dinar (JOD)','Indonesian Rupiah (IDR)','Hungarian Forint (HUF)','Guatemalan Quetzal (GTQ)','Georgian Lari (GEL)','Ethiopian Birr (ETB)','Egyptian Pound (EGP)','Dominican Peso (DOP)','Costa Rican Colon (CRC)','Chilean Peso (CLP)','Canadian Dollar (CAD)','Cambodian Riel (KHR)','Brazilian Real (BRL)','Bangladeshi Taka (BDT)','Bahraini Dinar (BHD)','Argentinian Peso (ARS)','Angola Kwanza (AOA)','Algerian Dinar (DZD)')
currencies_to=('Us Dollar (USD)','Indian Rupee (INR)','Japanese yen (JPY)','Euro (EUR)','Bulgarian lev (BGN)','Czech koruna (CZK)','Danish krone (DKK)','Hungarian forint (HUF)','Polish zloty (PLN)','Swedish krona (SEK)','Swiss franc (CHF)','Icelandic krona (ISK)','Norwegian krone (NOK)','Croatian kuna (HRK)','Russian rouble (RUB)','Turkish lira (TRY)','Australian dollar (AUD)','Brazilian real (BRL)','Canadian dollar (CAD)','Hong Kong dollar (HKD)','Indonesian rupiah (IDR)','South Korean won (KRW)','Mexican peso (MXN)','Malaysian ringgit (MYR)','New Zealand dollar (NZD)','Philippine peso (PHP)','Singapore dollar (SGD)','Thai baht (THB)','South African rand (ZAR)','Vietnamese Dong (VND)','Uzbekistani Som (UZS)','Uruguayan Peso (UYU)','British Pound (GBP)','Ukrainian Hryvnia (UAH)','Ugandan Shilling (UGX)','Tunisian Dinar (TND)','Tanzanian Shilling (TZS)','New Taiwan Dollar (TWD)','Swiss Franc (CHF)','Sri Lankan Rupee (LKR)','Singapore Dollar (SGD)','Saudi Riyal (SAR)','Poland Złoty (PLN)','Peruvian Sol (PEN)','Paraguay Guarani (PYG)','Panamanian Balboa (PAB)','Pakistani Rupee (PKR)','Omani Rial (OMR)','Norwegian Krone (NOK)','Nigerian Naira (NGN)','Nicaraguan Cordoba (NIO)','New Zealand Dollar (NZD)','Nepalese Rupee (NPR)','Burmese Kyat (MMK)','Moroccan Dirham (MAD)','Mexican Peso (MXN)','Mauritian Rupee (MUR)','Malaysia Ringgit (MYR)','Lebanese Pound (LBP)','Kuwaiti Dinar (KWD)','Kenyan Shilling (KES)','Kazakhstani Tenge (KZT)','Jordanian Dinar (JOD)','Indonesian Rupiah (IDR)','Hungarian Forint (HUF)','Guatemalan Quetzal (GTQ)','Georgian Lari (GEL)','Ethiopian Birr (ETB)','Egyptian Pound (EGP)','Dominican Peso (DOP)','Costa Rican Colon (CRC)','Chilean Peso (CLP)','Canadian Dollar (CAD)','Cambodian Riel (KHR)','Brazilian Real (BRL)','Bangladeshi Taka (BDT)','Bahraini Dinar (BHD)','Argentinian Peso (ARS)','Angola Kwanza (AOA)','Algerian Dinar (DZD)')
root.set_theme('ubuntu')
root.title('CurrencyConverter')
root.minsize(450,200)
root.maxsize(450,200)
heading=ttk.Label(root,text='Currency Converter',font=('Courier',15,'bold'))
heading.pack()
currency_value=StringVar()#unit converter and add more sound effect to my dekstop remainder project!
currencies_value_to=StringVar()
Amount_value=StringVar()
from_=ttk.Combobox(root,value=currencies_form,width=24,textvariable=currency_value)
from_.place(x=50,y=40)
currency_value.set('Select Currency')
currencies_value_to.set('Select Currency')
to_=ttk.Combobox(root,value=currencies_to,width=24,textvariable=currencies_value_to)
to_.place(x=280,y=40)
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
		messagebox.showinfo('Info','Please Enter A Valid Number!')
	try:
		print('Converting... Amount Is Converting...')
		Va=convert(working_codes_from,working_codes_to,error_handling)
		reverse=(Va[::-1])
		check_1=(reverse[1:6])
		value11=(check_1[::-1])
		total_amount=(re.findall("\\d+\\.\\d+",Va))
		for value___ in total_amount:
			pass
		if value11==' true':
			Amount_.set(value___)
			amount_reslut.place(x=135)
			messagebox.showinfo('Info',f'Converted Amount:-{value___}')
			print('Converted!')
		else:
			messagebox.showinfo('Info','Not Converted! Currency Is Not Correct Or Check Your Network Connection Speed Is Slow Or Not If Slow Thats Why Currency Is Not Converted! If Your Connection Speed Is Fast MayBe Thats A Bug In My Programme You Are Free To Report Me At Mail:rishiratanpandey@gmail.com Or Check Network Connectivity!')
	except UnboundLocalError:
		 ''
from_indiacator=ttk.Label(root,text='From')
from_indiacator.place(x=1,y=40)
Label_=ttk.Label(root,text='Enter Amount Down Below To Convert',font=('Courier',9))
Label_.place(x=1,y=70)
input_=Entry(root,width=20,textvariable=Amount_value)
input_.place(x=1,y=100)
convert_=ttk.Button(root,text='Convert',width=8,command=conversion)
convert_.place(y=100,x=200)
Amount_=IntVar()
result=ttk.Label(root,text='Converted Amount--:')
result.place(x=1 ,y=140)
amount_reslut=ttk.Label(root,textvariable=Amount_)
amount_reslut.place(x=137 ,y=140)
to=ttk.Label(root,text='To')
to.place(y=40,x=235)
mainloop()

# hmm..end
