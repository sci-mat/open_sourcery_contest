from  tkinter import *
from tkinter import messagebox

def bsa(listofnumbers, target):
    a = 0
    b = len(listofnumbers) - 1

    while a <= b:
        m = (a + b) // 2
        if listofnumbers[m] == target:
            return m
        elif listofnumbers[m] < target:
            a = m + 1
        else:
            b = m - 1
    return "element is not found"

def search():
    try:
        listofnumbers = list(map(int, entrylistofnums.get().split()))
        listofnumbers.sort()  
        target = int(entry_searchnum.get())
        
        result = bsa(listofnumbers, target)
        
        if result != "element is not found":
            messagebox.showinfo("Result", f"Element found at index {result} of the list")
        else:
            messagebox.showinfo("Result", "Element is not found in the list provided by the user")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer")


window = Tk()
window.title("Binary Search Algorithm Application")
window.geometry("500x500")

listofnums = Label(window, text="Enter a listed of numbers in ascending order and seperated by space")
listofnums.pack(pady=10)

entrylistofnums = Entry(window, width=60)
entrylistofnums.pack(pady=10)

searchnum = Label(window, text="Enter the number that user wants to search")
searchnum.pack(pady=10)

entry_searchnum = Entry(window, width=60)
entry_searchnum.pack(pady=10)

search_button = Button(window, text="Search", command=search)
search_button.pack(pady=20)

window.mainloop()
