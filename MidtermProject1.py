
from tkinter import *
from tkinter import messagebox

# Function: returns a letter grade based on the average
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Function: runs when Calculate Grade button is clicked
def calculate_grade():
    entries = [entry1, entry2, entry3, entry4, entry5]
    scores = []

    for entry in entries:
        value = entry.get().strip()
        if value != "":
            try:
                score = float(value)
                scores.append(score)
            except ValueError:
                messagebox.showerror("Error", "Please enter numbers only.")
                return

    # Stop if no scores were entered
    if len(scores) == 0:
        messagebox.showwarning("Warning", "Please enter at least one score.")
        return

    total = 0
    i = 0
    while i < len(scores):
        total = total + scores[i]
        i = i + 1

    # Calculate the average and get the letter grade
    average = total / len(scores)
    letter = get_letter_grade(average)

    # Build result string
    result = "Scores entered:  " + str(len(scores)) + "\n"
    result = result + "Total points:    " + str(round(total, 1)) + "\n"
    result = result + "Average score:   " + str(round(average, 2)) + "\n"
    result = result + "Letter grade:    " + letter

    # Clear the output box then insert the new result
    output_box.config(state=NORMAL)
    output_box.delete("1.0", END)
    output_box.insert(END, result)
    output_box.config(state=DISABLED)

# Function: clears all entry boxes and the output box
def clear_all():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    output_box.config(state=NORMAL)
    output_box.delete("1.0", END)
    output_box.config(state=DISABLED)

# Window setup
root = Tk()
root.title("Student Grade Tracker")
root.geometry("380x460")
root.resizable(0, 0)
root.configure(bg="light blue")

# Title
Label(root, text="Student Letter Grade Tracker",
      font=("Arial", 14, "bold"), bg="light blue").pack(pady=10)

# Entry boxes for scores
frame = Frame(root, bg="light blue")
frame.pack(pady=5)

Label(frame, text="Test Score 1:", bg="light blue", width=13, anchor="e").grid(row=0, column=0, pady=4)
entry1 = Entry(frame, width=10)
entry1.grid(row=0, column=1, pady=4)

Label(frame, text="Test Score 2:", bg="light blue", width=13, anchor="e").grid(row=1, column=0, pady=4)
entry2 = Entry(frame, width=10)
entry2.grid(row=1, column=1, pady=4)

Label(frame, text="Test Score 3:", bg="light blue", width=13, anchor="e").grid(row=2, column=0, pady=4)
entry3 = Entry(frame, width=10)
entry3.grid(row=2, column=1, pady=4)

Label(frame, text="Test Score 4:", bg="light blue", width=13, anchor="e").grid(row=3, column=0, pady=4)
entry4 = Entry(frame, width=10)
entry4.grid(row=3, column=1, pady=4)

Label(frame, text="Test Score 5:", bg="light blue", width=13, anchor="e").grid(row=4, column=0, pady=4)
entry5 = Entry(frame, width=10)
entry5.grid(row=4, column=1, pady=4)

Label(root, text="(Leave boxes empty to skip them)",
      font=("Arial", 9, "italic"), bg="light blue").pack()

# Buttons: Calculate and Clear
btn_frame = Frame(root, bg="light blue")
btn_frame.pack(pady=12)

Button(btn_frame, text="Calculate Grade", command=calculate_grade,
       bg="light green", font=("Arial", 11), width=14).grid(row=0, column=0, padx=8)

Button(btn_frame, text="Clear All", command=clear_all,
       bg="tomato", font=("Arial", 11), width=10).grid(row=0, column=1, padx=8)

output_box = Text(root, font=("Courier", 11), width=32, height=5,
                  relief="sunken", padx=8, pady=8, state=DISABLED)
output_box.pack(pady=8)

#Grade scale reference
Label(root, text="A=90-100   B=80-89   C=70-79   D=60-69   F=below 60",
      font=("Arial", 9), bg="light blue").pack()

#Start  program
mainloop()