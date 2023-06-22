
from tkinter import *
from tkinter import filedialog
from pdf_split import *

class canvas_pdf:
    title = "PDF Splitter"
    geometry = (600,500)
    background = "#202020"
    background_frame = "#ffffff"
    buttons_color = "#f2f2f2"

    def __init__(self):
        self.window = Tk()
        self.window.title(self.title)
        self.window.geometry("{}x{}".format(self.geometry[0],self.geometry[1]))
        self.window.config(bg=self.background)
        self.files = []
        self.filenames = []
        self.split_widgets = {}
        self.next_id = 0
    def home(self):
         try:
              self.Scanvas.destroy()
              self.Label_pdfs()
         except:
              pass
         self.Hcanvas = Canvas(self.window, bg= self.background, height = self.geometry[0], width=self.geometry[1],highlightthickness=0)
         self.frame_1 = Frame(self.Hcanvas, bg=self.background_frame)
         self.frame_1.pack()
         self.frame_2 = Frame(self.Hcanvas, bg=self.background_frame)
         button = Button(self.frame_2, text="Browse trough files", bg=self.buttons_color, height=2, width=20,command=self.openFexplorer,font=("Arial", 15))
         button.pack()
         self.frame_2.pack()
         self.Hcanvas.pack()

    def split_canvas(self):
         self.Scanvas = Canvas(self.window,  bg= self.background, height = self.geometry[0], width=self.geometry[1],highlightthickness=0)
         self.Scanvas.pack()
         text_label = Label(self.Scanvas, text="Would you like to split:\n {}?\nIf so please enter the page number.\nYour PDF will split after the given page number.".format(self.filenames[self.split_widgets[self.sbutton]]),
                             font=("Arial", 15), fg="#ffffff", bg=self.background)
         text_label.pack()
         entry_frame = Frame(self.Scanvas)
         self.number_entry = Entry(entry_frame, width= 40, font=("Arial", 15))
         self.number_entry.insert(0, "Please enter a page number here.")
         self.number_entry.pack(pady = 5, ipady= 10)
         self.name_entry = Entry(entry_frame, width= 40, font=("Arial", 15))
         self.name_entry.insert(0, "Please enter the new filename for the first file.")
         self.name_entry.pack(pady = 5, ipady= 10)
         self.name_entry_2 = Entry(entry_frame, width= 40, font=("Arial", 15))
         self.name_entry_2.insert(0, "Please enter the new filename for the second file.")
         self.name_entry_2.pack(pady = 5, ipady= 10)
         entry_frame.pack()
         buttons_frame = Frame(self.Scanvas)
         split_pdf_button = Button(buttons_frame, text="Split PDF",font=("Arial", 15), command=self.split_pdf )
         split_pdf_button.pack()
         return_button = Button(buttons_frame, text="return to home page", font=("Arial", 15), command=self.home)
         return_button.pack()
         buttons_frame.pack()
    def split_pdf(self):
         i = 3
         try:
                self.Error_frame.destroy()
         except:
              pass
         page_num = self.number_entry.get()
         self.Error_frame = Frame(self.Scanvas, bg= self.background)
         self.Error_frame.pack()
         try:
              page_num = int(page_num)
         except:
              self.Error = Label(self.Error_frame, text="Please enter a number before clicking.", font=("Arial", 15), bg=self.background, fg="#f90000")
              self.Error.pack()
              i -= 1
              
         new_name_1 = self.name_entry.get()
         if new_name_1 == "Please enter the new filename for the first file.":
              self.Error = Label(self.Error_frame, text="Please enter a new first filename before clicking.", font=("Arial", 15), bg=self.background, fg="#f90000")
              self.Error.pack()
              i -= 1
              
         new_name_2 = self.name_entry_2.get()
         if new_name_2 == "Please enter the new filename for the second file.":
               self.Error = Label(self.Error_frame, text="Please enter a new second filename before clicking.", font=("Arial", 15), bg=self.background, fg="#f90000")
               self.Error.pack()
               i -= 1
         file_path = self.files[self.split_widgets[self.fbutton]]
         end = count_pdf_pages(file_path)
         
         if i == 3:
              try:
                   split_pdf((0,page_num), file_path, new_name_1)
                   split_pdf((page_num+1,end), file_path, new_name_2)
                   good = Label(self.Error_frame, text= "The files are made and are located in your folder.",font=("Arial", 15), bg=self.background, fg="#00f900")
                   good.pack()

              except:
                   self.Error = Label(self.Error_frame, text="Something went wrong check.\nCheck if your entered page number is correct.", font=("Arial", 15), bg=self.background, fg="#f90000")
                   self.Error.pack()
    def split_button(self):
         self.Hcanvas.destroy()
         self.split_canvas()     
    
    def Label_pdfs(self):
                temp = self.file.rfind("/")
                filename = self.file[temp+1:]
                self.filenames.append(filename)
                label_frame = Frame(self.frame_1)
                flabel = Label(label_frame, text=filename, bg="#ffffff", font=("Arial", 15))
                flabel.pack(side=LEFT, padx=(0, 25))
                self.sbutton = Button(label_frame, text="split", bg="#ffffff", font=("Arial", 15), command=self.split_button)
                self.sbutton.pack(side=LEFT)
                self.split_widgets[self.sbutton] = self.next_id
                self.pbutton = Button(label_frame, text="paste", bg="#ffffff", font=("Arial", 15))
                self.pbutton.pack(side=LEFT, padx = (5,0))
                self.split_widgets[self.pbutton] = self.next_id
                self.next_id += 1
                label_frame.pack()
            
    def openFexplorer(self):
        ftypes = [('PDF files', '*.pdf'), ('All files', '*')]
        f_path = filedialog.askopenfilenames(filetypes=ftypes)
        self.files.append(f_path[0])
        self.file = f_path[0]
        self.Label_pdfs()

    def run(self):
        self.home()
        self.window.mainloop()


TK = canvas_pdf()
TK.run()
