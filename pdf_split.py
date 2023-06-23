from PyPDF2 import PdfReader, PdfWriter

# Function to split a PDF file into a specified range of pages
"""""
From and with page to with page
"""""
def split_pdf(pages, file_name, nfilename=None):
    # Read the input PDF file
    reader = PdfReader(file_name)
    # Create a new PDF writer
    writer = PdfWriter()
    # Determine the range of pages to extract
    page_range = range(pages[0], pages[1] + 1)
    # If no new file name is provided, create a default name based on the input file name and page range
    if nfilename == None:
        nfilename = f'{file_name}_page_{pages[0]}-{pages[1]}.pdf'
    
    # Iterate through each page in the input PDF
    for page_num, page in enumerate(reader.pages, 1):
        # If the current page number is within the specified range, add it to the writer
        if page_num in page_range:
            writer.add_page(page)
    
    # Write the extracted pages to the new PDF file
    with open(nfilename + ".pdf", 'wb') as out:
        writer.write(out)

# Function to paste one PDF file between a specified range of pages in another PDF file
def paste_pdf(betweenpages, pastepages, file_name1, file_name2, nfilename=None):
    # Read the input PDF files
    reader1 = PdfReader(file_name1)
    reader2 = PdfReader(file_name2)
    # Create a new PDF writer
    writer = PdfWriter()

    # If no new file name is provided, create a default name based on the input file names
    if nfilename == None:
        nfilename = f'{file_name1}_paste_{file_name2}.pdf'
    else:
        nfilename = nfilename + ".pdf"
    
    # Iterate through each page in the first input PDF
    for page_num, page in enumerate(reader1.pages, 1):
        # If the current page number is before or equal to the specified insertion point, add it to the writer
        if page_num <= betweenpages[0]:
            writer.add_page(page)
        
    # Iterate through each page in the second input PDF
    for page_num, page in enumerate(reader2.pages, 1):
        # If the current page number is within the specified range for pasting, add it to the writer
        if pastepages[0] <= page_num <= pastepages[1]:
            writer.add_page(page)
    
    # Iterate through each remaining page in the first input PDF
    for page_num, page in enumerate(reader1.pages, 1):
        # If the current page number is after the specified insertion point, add it to the writer
        if page_num > betweenpages[0]:
            writer.add_page(page)
    
    # Write the combined pages to the new PDF file
    with open(nfilename, 'wb') as out:
        writer.write(out)

def count_pdf_pages(file_name):
        # Open the PDF file in read-binary mode
        with open(file_name, 'rb') as file:
            # Create a PdfReader object
            pdf_reader = PdfReader(file)
            # Get the total number of pages in the PDF
            num_pages = len(pdf_reader.pages)
            # return the amount of pages 
            return num_pages

import ctypes as ct
def dark_title_bar(window):
    """
    MORE INFO:
    https://docs.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    DWMWA_BORDER_COLOR = 5  # Window attribute for border color
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())

    # Set dark mode
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))

