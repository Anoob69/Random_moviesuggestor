import numpy as np
import pandas as pd
import random
import tkinter as tk
 
data = pd.read_csv("indian movies.csv")
data = np.array(data)
l_movies=[]
for i in data:
    l_movies.append((i[1],i[2]))
 
def suggest():
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    r = random.choice(l_movies)
    name = r[0]
    year = r[1]
    msg = r[0] +"(" + r[1] + ")"
    t1.insert(tk.END,msg)
    t1.config(state='disabled')
window = tk.Tk()
window.geometry("600x200")
window.config(bg="#ABEBC6")
window.resizable(width=False,height=False)
window.title('Movie Name Suggestor')
 
l1 = tk.Label(window,text="Click on the button to suggest you a movie",font=("Arial",20),fg="Black",bg="White")
b1 = tk.Button(window,text="Suggest Movie",font=("Arial",15),bg="darkgreen",fg="white",command=suggest)
t1 = tk.Text(window,width=50,height=1,font=("Arial",15),state='disabled')
 
l1.place(x=30,y=10)
b1.place(x=200,y=60)
t1.place(x=15,y=120)
window.mainloop()