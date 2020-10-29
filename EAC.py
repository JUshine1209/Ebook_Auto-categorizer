import joblib
from tkinter import *
from tkinter import filedialog

'''
opened_txt_data = txt_file.read()
txt_file.close()
print(chr(txt_clf.predict([opened_txt_data])[0]+64))
'''

class clfGUI:
    def __init__(self, clf):
        self.loc_class_dict = {}
        self.loc_class_dict['A'] = 'General Works'

        self.txt_clf = clf
        self.root = Tk()
        self.root.title('E-book Auto-Categorizer')
        self.root.geometry('640x480')
        self.txtindex = 0
        self.clfindex = 0
        menubar = Menu(self.root)
        self.txtlistbox = Listbox(self.root,width=90,height=14)
        self.txtlistbox.pack()
        self.button = Button(self.root,text='Categorize',command=self.Categorize)
        self.button.pack()
        self.resultlistbox = Listbox(self.root,width=90,height=14)
        self.resultlistbox.pack()
        menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File',menu=menu)
        menu.add_command(label='Open',command=self.Load)
        menu.add_command(label='Reset', command=self.Reset)
        menu.add_command(label='Save', command=self.Save)
        menu.add_separator()
        menu.add_command(label='Exit', command=self.root.quit)
        self.root.config(menu=menubar)
        self.root.mainloop()
        
    def Load(self):
        filename = filedialog.askopenfilenames(title = 'Select txt file', filetypes = (('text files','*.txt'),))
        for file in filename:
            self.txtlistbox.insert(self.txtindex,file)
            self.txtindex += 1
    def Save(self):
        pass
    def Categorize(self):
        if self.txtlistbox.size() == 0:
            pass
        else:
            classified_category_list = []
            for textfile in self.txtlistbox.get(0,self.txtlistbox.size()-1):
                txt_file = open(textfile,'r',encoding='UTF8')
                opened_txt_data = txt_file.read()
                txt_file.close()
                classified_category_list.append(chr(self.txt_clf.predict([opened_txt_data])[0]+64))
            
    def Reset(self):
        pass

if __name__ == "__main__":
    print('Loading Classifier Model...')
    txt_clf = joblib.load('Tfidf_SVM_model.pkl')
    print('Loading Done!')
    EAC = clfGUI(txt_clf)


