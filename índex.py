from tkinter import *
import tkinter

### Cores ###

cor1 = "#000000" # black / 
cor2 = "#FFFFFF" # white / 
cor3 = "#1BFA00" # green / 
cor4 = "#FA1201" # red /
cor5 = "#4D4645" # gray /
cor6 = "#00B5E0" # blue /

janela = Tk()
janela.title("")
janela.geometry("300x180")
janela.configure(bg = cor1)
janela.resizable(width = False, height = False)

### 

label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=cor1, fg= cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text='00:00:00', font=('Times 50'), bg=cor1, fg=cor2)
label_tempo.place(x=20, y=25)







janela.mainloop()