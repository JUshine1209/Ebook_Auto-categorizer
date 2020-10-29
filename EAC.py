import joblib
import json
from tkinter import *
from tkinter import filedialog

class clfGUI:
    def __init__(self, clf, Loc_Class):
        self.txt_clf = clf
        self.clsdict = Loc_Class
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
        if self.txtindex != self.clfindex or self.clfindex == 0:
            pass
        else:
            first_write = True
            filename = filedialog.asksaveasfilename(title='Save as',filetypes=(('json files','*.json'),))
            Categorized_json = open(filename+'.json','w')
            Categorized_json.write('[\n')
            for i in range(0,self.resultlistbox.size()):
                if first_write:
                    first_write = False
                else:
                    Categorized_json.write(',\n')
                books_dict = {self.txtlistbox.get(i,i)[0].split('/')[-1][:-4]\
                    :self.resultlistbox.get(i,i)[0]}
                Categorized_json.write(json.dumps(books_dict))
            Categorized_json.write('\n]')
            Categorized_json.close()
               
    def Categorize(self):
        if self.txtlistbox.size() == 0:
            pass
        else:
            self.clfindex = 0
            if self.resultlistbox.size() != 0:
                self.resultlistbox.delete(0,self.resultlistbox.size()-1)
            classified_category_list = []
            for textfile in self.txtlistbox.get(0,self.txtlistbox.size()-1):
                txt_file = open(textfile,'r',encoding='UTF8')
                opened_txt_data = txt_file.read()
                txt_file.close()
                classified_category_list.append(chr(self.txt_clf.predict([opened_txt_data])[0]+64))
            for cl in classified_category_list:
                self.resultlistbox.insert(self.clfindex,self.clsdict[cl])
                self.clfindex += 1

    def Reset(self):
        self.txtindex = 0
        self.clfindex = 0
        if self.txtlistbox.size() != 0:
            self.txtlistbox.delete(0,self.txtlistbox.size()-1)
        if self.resultlistbox.size() != 0:
            self.resultlistbox.delete(0,self.resultlistbox.size()-1)

if __name__ == "__main__":
    print('Loading Classifier Model...')
    txt_clf = joblib.load('Tfidf_SVM_model.pkl')
    print('Loading Done!')

    LoC_Class_dict = {'A':'General Works','B':'Philosophy, Psychology, Religion',\
        'C':'Auxiliary Sciences of History','D':'World History','E':'History of Americas',\
            'F':'History of the Americas','G':'Geography, Anthropology, Recreation','H':'Social Sciences',\
                'J':'Political Sciences','K':'Law','L':'Education','M':'Music and Books on Music',\
                    'N':'Fine Arts','P':'Language and Literature','Q':'Sciences','R':'Medicine',\
                        'S':'Agriculture','T':'Technology','U':'Military Science','V':'Naval Science',\
                            'Z':'Bibliography, Library Science, Information Resources (General)'}

    EAC = clfGUI(txt_clf, LoC_Class_dict)


