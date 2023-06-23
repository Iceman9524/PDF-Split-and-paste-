
from tkinter import *
from tkinter import filedialog
from pdf_split import *

class canvas_pdf:
    title = "PDF Splitter"
    geometry = (600,500)
    background = "#202020"
    background_frame = "#505050"
    text_color= "#ffffff"
    error_color = "#f90000"
    def __init__(self):
        self.window = Tk()
        self.window.title(self.title)
        dark_title_bar(self.window)
        p1 = PhotoImage(file = 'pdf_logo.png')
        self.window.iconphoto(False, p1)
        self.window.geometry("{}x{}".format(self.geometry[0],self.geometry[1]))
        self.window.config(bg=self.background)
        self.files = []
        self.filenames = []
        self.split_widgets = {}
        self.next_id = 0
    def home(self):
         self.Hcanvas = Canvas(self.window, bg= self.background, height = self.geometry[0], width=self.geometry[1],highlightthickness=0)
         self.frame_1 = Frame(self.Hcanvas, bg=self.background)
         intro_label = Label(self.frame_1, text="Please select a file.", font=("Arial", 15), fg=self.text_color, bg=self.background)
         intro_label.pack(pady=5)
         self.frame_1.pack()
         self.frame_2 = Frame(self.Hcanvas, bg=self.background)
         button = Button(self.frame_2, text="Browse trough files", height=2, width=20,command=self.openFexplorer,font=("Arial", 15), bg=self.background_frame, fg=self.text_color)
         button.pack()
         """""
         if self.next_id >= 2:
              status = NORMAL
         else:
              status = DISABLED
          """""
         self.H_paste = Button(self.frame_2, text="Merge files together", height=2, width=20,command=self.openFexplorer,font=("Arial", 15), bg=self.background_frame, fg=self.text_color, state=DISABLED)
         self.H_paste.pack(pady=(10,0))
         self.frame_2.pack()
         self.Hcanvas.pack()

    def restore_home(self):
         self.Scanvas.destroy()
         self.home()
         for i in self.files:
              self.Label_pdfs(i)
              
    def split_canvas(self):
         self.Scanvas = Canvas(self.window,  bg= self.background, height = self.geometry[0], width=self.geometry[1],highlightthickness=0)
         self.Scanvas.pack()
         text_label = Label(self.Scanvas, text="Would you like to split:\n {}?\nIf so please enter the page number.\nYour PDF will split after the given page number.".format(self.filenames[self.split_widgets[self.sbutton]]),
                             font=("Arial", 15), fg=self.text_color, bg=self.background)
         text_label.pack()
         entry_frame = Frame(self.Scanvas, bg=self.background)
         self.number_entry = Entry(entry_frame, width= 40, font=("Arial", 15),bg=self.background_frame, fg=self.text_color)
         self.number_entry.insert(0, "Please enter a page number here.")
         self.number_entry.pack(pady = 5, ipady= 10)
         self.name_entry = Entry(entry_frame, width= 40, font=("Arial", 15),bg=self.background_frame, fg=self.text_color)
         self.name_entry.insert(0, "Please enter the new filename for the first file.")
         self.name_entry.pack(pady = 5, ipady= 10)
         self.name_entry_2 = Entry(entry_frame, width= 40, font=("Arial", 15),bg=self.background_frame, fg=self.text_color)
         self.name_entry_2.insert(0, "Please enter the new filename for the second file.")
         self.name_entry_2.pack(pady = 5, ipady= 10)
         entry_frame.pack()
         buttons_frame = Frame(self.Scanvas, bg=self.background)
         split_pdf_button = Button(buttons_frame, text="Split PDF",font=("Arial", 15), command=self.split_pdf,bg=self.background_frame, fg=self.text_color )
         split_pdf_button.pack()
         return_button = Button(buttons_frame, text="return to home page", font=("Arial", 15), command=self.restore_home,bg=self.background_frame, fg=self.text_color)
         return_button.pack()
         buttons_frame.pack(pady= (10,0))

    def split_pdf(self):
         i = 4
         try:
                self.Error_frame.destroy()
         except:
              pass
         page_num = self.number_entry.get()
         self.Error_frame = Frame(self.Scanvas, bg= self.background)
         self.Error_frame.pack()
         file_path = self.files[self.split_widgets[self.sbutton]]
         end = count_pdf_pages(file_path)
         try:
              page_num = int(page_num)
              if end < page_num or page_num<0:
                  self.Error = Label(self.Error_frame, text="Please enter a valid pagenumber.", font=("Arial", 15), bg=self.background, fg=self.error_color)
                  self.Error.pack()
                  i -= 1
         except:
              self.Error = Label(self.Error_frame, text="Please enter a number before clicking.", font=("Arial", 15), bg=self.background, fg=self.error_color)
              self.Error.pack()
              i -= 1
         
         
                   
         new_name_1 = self.name_entry.get()
         if new_name_1 == "Please enter the new filename for the first file.":
              self.Error = Label(self.Error_frame, text="Please enter a new first filename before clicking.", font=("Arial", 15), bg=self.background, fg=self.error_color)
              self.Error.pack()
              i -= 1
              
         new_name_2 = self.name_entry_2.get()
         if new_name_2 == "Please enter the new filename for the second file.":
               self.Error = Label(self.Error_frame, text="Please enter a new second filename before clicking.", font=("Arial", 15), bg=self.background, fg=self.error_color)
               self.Error.pack()
               i -= 1
       
         
         if i == 4:
              try:
                   split_pdf((0,page_num), file_path, new_name_1)
                   split_pdf((page_num+1,end), file_path, new_name_2)
                   good = Label(self.Error_frame, text= "The files are made and are located in your folder.",font=("Arial", 15), bg=self.background, fg=self.error_color)
                   good.pack()

              except:
                   self.Error = Label(self.Error_frame, text="Something went wrong check.", font=("Arial", 15), bg=self.background, fg=self.error_color)
                   self.Error.pack()
    def split_button(self):
         self.Hcanvas.destroy()
         self.split_canvas()     
      
    def Label_pdfs(self, file):
                temp = file.rfind("/")
                filename = file[temp+1:]
                self.filenames.append(filename)
                label_frame = Frame(self.frame_1, bg=self.background_frame)
                flabel = Label(label_frame, text=filename, bg=self.background_frame, fg=self.text_color, font=("Arial", 15))
                flabel.pack(side=LEFT, padx=(0, 25))
                self.sbutton = Button(label_frame, text="split", bg=self.background_frame, font=("Arial", 15), command=self.split_button, fg=self.text_color)
                self.sbutton.pack(side=LEFT)
                self.split_widgets[self.sbutton] = self.next_id
                self.next_id += 1
                if self.next_id >= 2:
                    self.H_paste.config(state=NORMAL)
                label_frame.pack(pady=(0,10))
                
    def openFexplorer(self):
        ftypes = [('PDF files', '*.pdf'), ('All files', '*')]
        f_path = filedialog.askopenfilenames(filetypes=ftypes)
        self.files.append(f_path[0])
        file = f_path[0]
        self.Label_pdfs(file)

    def run(self):
        self.home()
        self.window.mainloop()


TK = canvas_pdf()
TK.run()
