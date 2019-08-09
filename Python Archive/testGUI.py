from Tkinter import *

class App:
    name = 'no name'

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.label = Label(frame, text='Selection')
        self.label.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, " + self.name
        
root = Tk()


app = App(root)
app.name = 'william'
app2 =App(root)


root.mainloop()
root.destroy() # optional; see description below