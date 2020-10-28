import joblib
from tkinter import *
from tkinter import filedialog

'''
txt_file = open('27924.txt','r',encoding='UTF8')
opened_txt_data = txt_file.read()
txt_file.close()
print(chr(txt_clf.predict([opened_txt_data])[0]+64))
'''

class clfGUI:
    def __init__(self, clf):
        self.root = Tk()
        menubar = Menu(self.root)
        menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File',menu=menu)
        menu.add_command(label='Open',command=self.Load)
        menu.add_command(label='Save', command=self.Save)
        menu.add_separator()
        menu.add_command(label='Exit', command=self.root.quit)
    def Load(self):
        filename = filedialog.askopenfilenames(initialdir='/', title = 'Select txt file', filetypes = (('text files','*.txt')))

        


