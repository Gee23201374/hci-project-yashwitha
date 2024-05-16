import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AddStudentPage(tk.Toplevel):
    def __init__(self, master, students_list):
        super().__init__(master)
        self.title("Add Student")
        self.geometry("400x300")
        
        self.students_list = students_list
        
        tk.Label(self, text="Name:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()
        
        tk.Label(self, text="Address:").pack()
        self.address_entry = tk.Entry(self)
        self.address_entry.pack()
        
        tk.Label(self, text="Age:").pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()
        
        tk.Label(self, text="Phone Number:").pack()
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack()
        
        tk.Button(self, text="Submit", command=self.submit_student).pack(pady=10)
        
    def submit_student(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        age = self.age_entry.get()
        phone_number = self.phone_entry.get()
        
        self.students_list.append({"name": name, "address": address, "age": age, "phone": phone_number})
        
        messagebox.showinfo("Student Added", f"Student {name} added successfully!")
        self.destroy()

class DisplayStudentsPage(tk.Toplevel):
    def __init__(self, master, students_list):
        super().__init__(master)
        self.title("Display Students")
        self.geometry("600x400")
        
        self.students_list = students_list
        
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("Name", "Address", "Age", "Phone Number")
        self.tree.heading("#0", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Phone Number", text="Phone Number")
        
        for i, student in enumerate(self.students_list, start=1):
            self.tree.insert("", "end", text=str(i), values=(student["name"], student["address"], student["age"], student["phone"]))
        
        self.tree.pack(expand=True, fill="both")

class AddInstructorPage(tk.Toplevel):
    def __init__(self, master, instructors_list):
        super().__init__(master)
        self.title("Add Instructor")
        self.geometry("300x250")
        
        self.instructors_list = instructors_list
        
        tk.Label(self, text="Instructor Name:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()
        
        tk.Label(self, text="Instructor ID:").pack()
        self.id_entry = tk.Entry(self)
        self.id_entry.pack()
        
        tk.Label(self, text="Experience:").pack()
        self.experience_entry = tk.Entry(self)
        self.experience_entry.pack()
        
        tk.Label(self, text="Gender:").pack()
        self.gender_entry = tk.Entry(self)
        self.gender_entry.pack()
        
        tk.Label(self, text="Applicable Driving:").pack()
        self.driving_entry = tk.Entry(self)
        self.driving_entry.pack()
        
        tk.Button(self, text="Submit", command=self.submit_instructor).pack(pady=10)
        
    def submit_instructor(self):
        name = self.name_entry.get()
        instructor_id = self.id_entry.get()
        experience = self.experience_entry.get()
        gender = self.gender_entry.get()
        driving = self.driving_entry.get()
        
        self.instructors_list.append({"name": name, "id": instructor_id, "experience": experience, "gender": gender, "driving": driving})
        
        messagebox.showinfo("Instructor Added", f"Instructor {name} added successfully!")
        self.destroy()

class DisplayInstructorsPage(tk.Toplevel):
    def __init__(self, master, instructors_list):
        super().__init__(master)
        self.title("Display Instructors")
        self.geometry("400x300")
        
        self.instructors_list = instructors_list
        
        tk.Label(self, text="List of Instructors").pack()
        
        for instructor in self.instructors_list:
            tk.Label(self, text=f"Name: {instructor['name']}, ID: {instructor['id']}, Experience: {instructor['experience']}, Gender: {instructor['gender']}, Driving: {instructor['driving']}").pack()

class DrivingSchoolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IT Pass Driving School")
        self.geometry("600x400")
        
        self.students_list = []
        self.instructors_list = []
        self.driving_types = ["Manual", "Automatic", "Motorcycle"]
        self.booked_lessons = []  # Store booked lessons
        
        self.create_dashboard()
    
    def create_dashboard(self):
        dashboard_frame = tk.Frame(self, bg="lightblue", padx=20, pady=20)
        dashboard_frame.pack(expand=True, fill='both')
        
        welcome_label = tk.Label(dashboard_frame, text="Welcome to IT Pass Driving School", font=("Helvetica", 20, "bold"), bg="lightblue")
        welcome_label.pack(pady=20)
        
        description_label = tk.Label(dashboard_frame, text="Your journey to becoming a skilled driver begins here!", font=("Helvetica", 12), bg="lightblue")
        description_label.pack()
        
        button_frame = tk.Frame(dashboard_frame, bg="lightblue")
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Add Student", command=self.open_add_student_page).pack(side="left", padx=10)
        tk.Button(button_frame, text="Add Instructor", command=self.open_add_instructor_page).pack(side="left", padx=10)
        tk.Button(button_frame, text="Book Lesson", command=self.show_book_lesson).pack(side="left", padx=10)
        tk.Button(button_frame, text="Cancel Lesson", command=self.show_cancel_lesson).pack(side="left", padx=10)
        tk.Button(button_frame, text="Display Students", command=self.display_students).pack(side="left", padx=10)
        tk.Button(button_frame, text="Display Instructors", command=self.display_instructors).pack(side="left", padx=10)
        tk.Button(button_frame, text="Exit", command=self.quit).pack(side="left", padx=10)
    
    def open_add_student_page(self):
        AddStudentPage(self, self.students_list)

    def open_add_instructor_page(self):
        AddInstructorPage(self, self.instructors_list)
    
    def show_book_lesson(self):
        book_lesson_window = tk.Toplevel(self)
        book_lesson_window.title("Book Lesson")
        book_lesson_window.geometry("300x200")
        
        tk.Label(book_lesson_window, text="Select Driving Type:").pack()
        driving_var = tk.StringVar()
        driving_dropdown = ttk.Combobox(book_lesson_window, textvariable=driving_var, values=self.driving_types)
        driving_dropdown.pack()
        driving_dropdown.current(0)
        
        tk.Label(book_lesson_window, text="Name of the Student:").pack()
        student_name_entry = tk.Entry(book_lesson_window)
        student_name_entry.pack()
        
        tk.Label(book_lesson_window, text="Student ID:").pack()
        student_id_entry = tk.Entry(book_lesson_window)
        student_id_entry.pack()
        
        tk.Label(book_lesson_window, text="Select Course Duration:").pack()
        duration_var = tk.StringVar()
        duration_dropdown = ttk.Combobox(book_lesson_window, textvariable=duration_var, values=["1 hour", "2 hours", "3 hours"])
        duration_dropdown.pack()
        duration_dropdown.current(0)
        
        def submit_lesson():
            student_name = student_name_entry.get()
            lesson_details = {
                "student_name": student_name,
                "driving_type": driving_var.get(),
                "duration": duration_var.get()
            }
            self.booked_lessons.append(lesson_details)
            messagebox.showinfo("Lesson Added", "Lesson is added successfully!")
        
        tk.Button(book_lesson_window, text="Submit", command=submit_lesson).pack(pady=10)
    
    def show_cancel_lesson(self):
        cancel_lesson_window = tk.Toplevel(self)
        cancel_lesson_window.title("Cancel Lesson")
        cancel_lesson_window.geometry("400x300")
        
        # Create a treeview to display booked lessons
        tree = ttk.Treeview(cancel_lesson_window)
        tree["columns"] = ("Student Name", "Driving Type", "Duration")
        tree.heading("#0", text="ID")
        tree.heading("Student Name", text="Student Name")
        tree.heading("Driving Type", text="Driving Type")
        tree.heading("Duration", text="Duration")
        
        # Populate the treeview with booked lessons
        for i, lesson in enumerate(self.booked_lessons, start=1):
            tree.insert("", "end", text=str(i), values=(lesson["student_name"], lesson["driving_type"], lesson["duration"]))
        
        tree.pack(expand=True, fill="both")
        
        # Function to cancel the selected lesson
        def cancel_lesson():
            selected_item = tree.selection()[0]
            lesson_index = int(tree.item(selected_item, "text")) - 1
            del self.booked_lessons[lesson_index]
            tree.delete(selected_item)
            messagebox.showinfo("Cancel Lesson", "Lesson canceled successfully!")
        
        # Button to cancel the selected lesson
        cancel_button = tk.Button(cancel_lesson_window, text="Cancel Selected Lesson", command=cancel_lesson)
        cancel_button.pack(pady=10)
    
    def display_students(self):
        DisplayStudentsPage(self, self.students_list)
    
    def display_instructors(self):
        DisplayInstructorsPage(self, self.instructors_list)

if __name__ == "__main__":
    app = DrivingSchoolApp()
    app.mainloop()
