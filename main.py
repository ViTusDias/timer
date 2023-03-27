from tkinter import *
from tkinter import ttk

### cores ###
cor1 = "#0F0F0B"
cor2 = "#B5B5B5"

# criando Janelas ------

window = Tk()

window.title("")
window.geometry("300x180")
window.configure(bg=cor1)
window.resizable(width=FALSE, height=FALSE)

# definindo variaveis globais

global time
global turn
global accountante

time = "00:00:00"
turn = False
accountante = -5

def start():
    global time
    global accountante
    
    if turn:
        # antes do cronometro *****
        if accountante <=-1:
            inicio = 'Começando em' +str(accountante)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Constantia 10'
            
        else:
            print('Satisfeita')
        
        label_tempo.after(1000, start)
        accountante +=1

# Função Play --------

def play():
    global turn
    turn = True
    start()


# criando Serif's ------

label_app = Label(window, text='Cronômetro', font=('Constantia 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(window, text=time, font=('Bahnschrift 50 '), bg=cor1, fg=cor2)
label_tempo.place(x=20, y=25)

# criando Buttons ------

button_start = Button(window, command=start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Century 8'), relief='raised', overrelief='ridge')
button_start.place(x=20, y=130)

# criando Buttons ------ (Stop)

button_pausar = Button(window, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Century 8'), relief='raised', overrelief='ridge')
button_pausar.place(x=105, y=130)

# criando Buttons ------ (Restart)

button_restart = Button(window, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Century 8'), relief='raised', overrelief='ridge')
button_restart.place(x=190, y=130)





window.mainloop()