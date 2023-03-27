#-- Biblioteca --#

from tkinter import *
import tkinter

#--- Cores ---#

cor1 = '#000000' # Black
cor2 = '#FFFFFF' # white 
cor3 = '' # green
cor4 = '' # red
cor5 = '' # gray
cor6 = '' # blue

#--- Janela (tkk) ---#

janela = Tk ()
janela.title("")
janela.geometry('300x180')
janela.configure(bg=cor1)
janela.resizable(width=False, height=False)

#-- Variaveis Globais --#

global tempo
global rodar
global contador 
global limitador 

#--- Função (Tempo) ---#

limitador = 59 
tempo = "00:00:00"
rodar = False
contador = -5

#-- função iniciar --#

def iniciar():
    global tempo
    global contador
    global limitador 
    
    if rodar:
        ##(Antes do Cronômetro começar)##
        if contador <=-1:
            inicio = 'começando em' +str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'
        
        ##(Rodando o Cronômetro)##
        else:
            label_tempo['font'] = 'Times 50 bold'
            
            temporario = str(tempo)
            h,m,s = map(int, temporario.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)
            
            if (s>=limitador):
                contador = 0
                m+=1
                
            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

#--- Atualizando os valores atuais --#
            
            temporario = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            label_tempo['text'] = temporario
            tempo = temporario
            
        label_tempo.after(1000, iniciar)
        contador +=1
            
#-- funçao para dar inicio --#

def start():
    global rodar
    rodar = True
    iniciar()
    
#-- funçao para dar Pause --#

def pausar():
    global rodar
    rodar = False

#-- funçao para reiniciar --#

def reiniciar():
    global contador
    global tempo
    
#--- reiniciando o contador --#
 
    contador = 0
    
#--- reiniciando o tempo --#

    tempo = "00:00:00"
    label_tempo['text'] = tempo

#--- Label(Rótulo) ---#

label_app = Label(janela, text= 'Cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5) ##('Cronômetro')##

label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor2)
label_tempo.place(x=20, y=30) ##('00:00:00')(Relógio)##

#--- Botões ---#

botao_iniciar = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Arial 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=130) ##(''Botão Iniciar')##

botao_pausar = Button(janela, command=pausar, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Arial 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=105, y=130) ##(''Botão Pausar')##

botao_reiniciar = Button(janela, command=reiniciar, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Arial 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=190, y=130) ##(''Botão Reiniciar')##


janela.mainloop()