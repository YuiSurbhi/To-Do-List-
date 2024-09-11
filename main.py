import tkinter
from tkinter import *

# Create main window 
root = Tk()
root.title("To-Do-List")   # Set the window title 
root.geometry("400x650+400+100")   # Set the size and position of the window 
root.resizable(False,False)   # Disable the window resizing 

# Initialize an empty task list
task_list = []

# Function to add a new task 
def addTask():
    task = task_entry.get()    # Get the task from entry field 
    task_entry.delete(0,END)    # Clear the entry field after getting the input

    if task:    # If the task is not empty
        with open("tasklist.txt",'a') as taskfile:   # Open the file in append mode
            taskfile.write(f"\n{task}")   # Write the task to do the file 
        task_list.append(task)   # Add the task to the in-memory list 
        listbox.insert(END,task)   # Insert the task into the Listbox widget

# Function to delete the selected task
def deleteTask():
    global task_list    # Use the global task_list variable
    task = str(listbox.get(ANCHOR))    # Get the currently selected task
    if task in task_list:     # If the task is in the task list
        task_list.remove(task)    # Remove it from the in-memory list
        with open("tasklist.txt",'w') as taskfile:     # Open the file in write mode 
            for task in task_list:     # Write all remaining tasks to the file
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)    # Delete the selected task from the Listbox

# Function to open the file and load existing tasks
def openTaskFile():

    try:
        global task_list      # Reffer to the global task_list variable
        # Open the file in read mode
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()     # Read all tasks from the file 

        # Load task into list and listbox
        for task in tasks:
            if task != '\n':     # Ignore empty lines 
                task_list.append(task)      # Add task to the in-memory list 
                listbox.insert(END,task)     # Insert task into the Listbox

    except:
        file=open("tasklist.txt",'w')    # If file doesn't exist, create it
        file.close()

# Load the Icon for the application
Image_icon = PhotoImage(file = "images/task.png")
root.iconphoto(False,Image_icon)

# Add the Topbar image
TopImage = PhotoImage(file = "images/topbar.png")
Label(root,image = TopImage).pack()

# Add the dock image for styling
dockImage = PhotoImage(file = "images/dock.png")
Label(root,image = dockImage, bg = "#32405b").place(x = 30,y = 25)

# Add the note image for visula appeal
noteImage = PhotoImage(file = "images/task.png")
Label(root,image = noteImage, bg = "#32405b").place(x = 340,y = 25)

# Heading Label
heading = Label(root,text = "All Task",font = "arial 20 bold",fg = "white",bg = "#32405b")
heading.place(x = 130,y = 20)

# Main
frame = Frame(root,width = 400,height = 50,bg = "white")
frame.place(x= 0,y= 180)

# Entry widget for entering new tasks
task = StringVar()
task_entry = Entry(frame,width = 18,font = "arial 20",bd = 0)
task_entry.place(x = 10,y = 7)
task_entry.focus()     # Automatically focus the cursor on the entry field

# Add button to add tasks
button = Button(frame,text="ADD",font = "arial 20 bold",width = 6,bg = "#5a95ff",fg = "#fff",bd = 0,command=addTask)
button.place(x = 300,y = 0)

# frame for Listbox widget
frame1 = Frame(root,bd = 3,width = 700,height = 280,bg = "#32450b")
frame1.pack(pady = (160,0))

listbox = Listbox(frame1,font = ('arial',12),width = 40,height = 16,bg = "#32405b",fg = "white",cursor = "hand2",selectbackground = "#5a95ff")
listbox.pack(side = LEFT,fill = BOTH,padx = 2)

# Scrollbar for listbox
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

# Configure the listbox to work with scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Load existing task from the file
openTaskFile()

# Delete button to reove task
Delete_icon = PhotoImage(file="images/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)

# Start main event loop
root.mainloop()