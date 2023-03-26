# this imports everything from the tkinter module
from tkinter import *
# importing the ttk module from tkinter that's for styling widgets
from tkinter import ttk
# importing message boxes like showinfo, showerror, askyesno from tkinter.messagebox
from tkinter.messagebox import askyesno
# this imports operating system commands
import os


# the function to close the window
def close_window():
    # this will ask the user whether to close or not
    # if the value is yes/True the window will close
    if askyesno(title='Close Pcb Database', message='Are you sure you want to close the Database Application?'):
        # this destroys the window
        window.destroy()


# creating the window using the Tk() class
window = Tk()
# creates title for the window
window.title('PCB DATABASE STORAGE')
# adding the window's icon
window.iconbitmap(window, 'database.ico')
# dimensions and position of the window
window.geometry('800x600+400+100')
# makes the window non-resizable
window.resizable(height=FALSE, width=FALSE)
# this is for closing the window via the close_window() function
window.protocol('WM_DELETE_WINDOW', close_window)


"""Styles for the widgets, labels, entries, and buttons"""

# style for the labels
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('Dotum', 10))

# style for the entries
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))

# style for the buttons
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font=('DotumChe', 10))

# creating the Notebook widget
tab_control = ttk.Notebook(window)

# creating a tab with the ttk.Frame()
detect_tab = ttk.Frame(tab_control)

# adding the two tabs to the Notebook
tab_control.add(detect_tab, text='BUGFIX')
# this makes the Notebook fill the entire main window so that its visible
tab_control.pack(expand=1, fill="both")

# creates the canvas for containing all the widgets in the tab
gen_canvas = Canvas(detect_tab, width=750, height=550)
# packing the canvas to the second tab
gen_canvas.pack()

# creates the canvas for containing all the widgets in the tab
gen_canvas1 = Canvas(detect_tab, width=750, height=550)
# packing the canvas to the second tab
gen_canvas1.pack(fill=BOTH, expand=1)


"""Widgets for the BugFix tab"""

# creating a source label
source_qrcode = ttk.Label(window, text='Scan Source QRcode:', style='TLabel')
# creating a source entry
source_entry = ttk.Entry(window, width=45, style='TEntry')

# adding the label to the canvas
gen_canvas.create_window(110, 30, window=source_qrcode)
# adding the entry to the canvas
gen_canvas.create_window(320, 30, window=source_entry)

# creating a pcb label
pcb_qrcode = ttk.Label(window, text='Scan QRcode:', style='TLabel')
# creating a pcb entry
pcb_entry = ttk.Entry(width=45, style='TEntry')

# adding the label to the canvas
gen_canvas.create_window(88, 60, window=pcb_qrcode)
# adding the entry to the canvas
gen_canvas.create_window(280, 60, window=pcb_entry)

# creating a scan pcb label
pcb_box = ttk.Label(window, text='Scanned PCB`s:', style='TLabel')
# creating a scan pcb entry
pcb_entry = ttk.Entry(window, width=35)

# adding the scan pcb label to the canvas
gen_canvas.create_window(600, 60, window=pcb_box)
gen_canvas.create_window(620, 210, height= 280, window=pcb_entry)

# adding the scrollbar to the canvas
#my_scrollbar = ttk.Scrollbar(pcb_entry, orient=VERTICAL, command=gen_canvas1.yview) 
#my_scrollbar.pack(side=RIGHT, fill=Y)
#gen_canvas1.configure(yscrollcommand=my_scrollbar.set)
#gen_canvas1.bind('<Configure>', lambda e:gen_canvas.configure(scrollregion=gen_canvas1.bbox("all")))
#sec_frame = Frame(gen_canvas1)
#gen_canvas1.create_window((500,60), window=sec_frame, anchor="nw")

# creating a bug label
bug_number = ttk.Label(window, text='Bugs To be Fixed:', style='TLabel')
# creating a bug entry
bug_entry = ttk.Entry(window, width=20)

# adding the bug label to the canvas
gen_canvas.create_window(100, 120, window=bug_number)
gen_canvas.create_window(110, 240, height= 220, window=bug_entry)

# creating a source bug label
sbug_number = ttk.Label(window, text='Source Bugs Description:', style='TLabel')
# creating a source bug entry
sbug_entry = ttk.Entry(window, width=40)

# adding the source bug label to the canvas
gen_canvas.create_window(350, 120, window=sbug_number)
gen_canvas.create_window(350, 240, height= 220, window=sbug_entry)

# creating a Additional Bug label
source_qrcode = ttk.Label(window, text='Enter Additonal Bug Details:', style='TLabel')
# creating a Additional Bug entry
source_entry = ttk.Entry(window, width=45, style='TEntry')

# adding the Additional Bug label to the canvas
gen_canvas.create_window(130, 400, window=source_qrcode)
# adding the Additional Bug entry to the canvas
gen_canvas.create_window(360, 400, window=source_entry)

# creating the reset button in a disabled mode
reset_button = ttk.Button(window, text='Reset', style='TButton', state=DISABLED)
# creating the generate button
save_button = ttk.Button(window, text='Save', style='TButton', state=DISABLED)

# adding the reset button to the canvas
gen_canvas.create_window(250, 500, window=reset_button)
# adding the generate button to the canvas
gen_canvas.create_window(500, 500, window=save_button)


# run the main window infinitely
window.mainloop()
