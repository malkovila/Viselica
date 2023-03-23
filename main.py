from tkinter import *
import random
import threading
import tkinter as tk

class Game:
    def random_choise(self):
        lis = ['Россия']
        self.word = list(i for i in random.choice(lis))
        print(self.word)
        return self.play()

    def check_latter(self, v):
        if v in self.word:
            return True
        else:
            return False
    def play(self):
        wordd = ['' for i in range(len(self.word))]
        while True:
            v = input('Введите букву ')
            if self.check_latter(v):
                for i in range(len(self.word)):
                    if v == self.word[i]:
                        print('yes ', v)
                        wordd[i] = v
                        self.word[i] = ''
                        print(self.word)
                        print('Ваше слово: ' + str(wordd))
                        break
            else:
                if G.draw():
                    break

            if '' not in wordd:
                break


class Graphics:
    def show(self):
        self.window = Tk()
        self.window.title('Работа с canvas')
        self.canvas = Canvas(self.window,width=600,height=600,bg="gray",
                  cursor="pencil")
        self.canvas.pack()
        self.window.mainloop()

    def __init__(self):
        self.count = 0
    def draw(self):
        self.count += 1
        if self.count == 1:
            self.l1 = self.canvas.create_line(200, 100, 200, 500, width=5, fill="yellow")
        if self.count == 2:
            self.l2 = self.canvas.create_line(200, 500, 500, 500, width=5, fill="yellow")
        if self.count == 3:
            self.l3 = self.canvas.create_line(200, 100, 400, 100, width=5, fill="yellow")
        if self.count == 4:
            self.l4 =self.canvas.create_line(400, 100, 400, 200, width=5, fill="yellow")
        if self.count == 5:
            self.l5 =self.canvas.create_oval([345, 195], [440, 290], fill="yellow")
        if self.count == 6:
            self.l6 =self.canvas.create_line(392, 290, 392, 310, width=5, fill="yellow")
        if self.count == 7:
            self.l7 =self.canvas.create_line(392, 310, 342, 360, width=5, fill="yellow")
        if self.count == 8:
            self.l8 =self.canvas.create_line(392, 310, 442, 360, width=5, fill="yellow")
        if self.count == 9:
            self.l9 =self.canvas.create_line(392, 310, 392, 430, width=5, fill="yellow")
        if self.count == 10:
            self.l10 =self.canvas.create_line(392, 430, 342, 460, width=5, fill="yellow")
        if self.count == 11:
            self.l11 =self.canvas.create_line(392, 430, 442, 460, width=5, fill="yellow")

        if self.count == 12:
            self.canvas.delete(self.l1)
            self.canvas.delete(self.l2)
            self.canvas.delete(self.l3)
            self.canvas.delete(self.l4)
            self.canvas.delete(self.l5)
            self.canvas.delete(self.l6)
            self.canvas.delete(self.l7)
            self.canvas.delete(self.l8)
            self.canvas.delete(self.l9)
            self.canvas.delete(self.l10)
            self.canvas.delete(self.l11)
            txt_label = tk.Label(self.window, text='Вы проиграли...', bg='gray', font=("Arial", 26))
            txt_label.place(x=120, y=308)
        if self.count == 13:
            self.window.destroy()
            return True



G = Graphics()
thr = threading.Thread(target=G.show, name='thr-1')
thr.start()
F = Game()
F.random_choise()

