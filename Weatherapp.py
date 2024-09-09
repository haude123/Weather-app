from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

sp = Tk()
sp.title("Weather App")
sp.geometry("900x500+300+200")
sp.resizable(False,False)
def getWeather():
    try:
        city=textfield.get()
        geolocator= Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj= TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="Current Weather")


        ##weather api
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=" #appid=99ecbb3290774c9960663aa05e6cd6c7
        json_data=requests.get(api).json()
        condition= json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","feels","Like",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather app","Invalid entry")


##Search box##
Search_img=PhotoImage(file="search.png")
myimage=Label(image=Search_img)
myimage.place(x=20,y=20)
textfield=tk.Entry(sp,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

##Search Icon##
##Search Icon##
Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(sp, image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

##Logo##
logo=PhotoImage(file="logo.png")
myimage_logo=Label(image=logo)
myimage_logo.place(x=150,y=100)


##bottom box
box_img=PhotoImage(file="box.png")
box_img1=Label(image=box_img)
box_img1.pack(padx=5,pady=5,side=BOTTOM)

##time
name=Label(sp,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(sp,font=("helvetica",20))
clock.place(x=30,y=130)

##Label
label1=Label(sp,text="Wind",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(sp,text="Humidity",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(sp,text="Description",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(sp,text="Pressure",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)


t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",20,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

sp.mainloop()
