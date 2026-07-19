import tkinter as tk
from tkinter import messagebox
import pickle
import os


class PayrollSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll System")

        # Window size and colour
        self.root.geometry("450x650")
        self.root.configure(bg="lightblue")

        # Frame
        self.frame = tk.Frame(self.root, bg="lightblue")
        self.frame.pack(pady=20)

        # Label style
        label_style = {
            "bg": "lightblue",
            "fg": "darkblue",
            "font": ("Arial", 12, "bold")
        }

        # Employee ID
        self.employee_id_label = tk.Label(
            self.frame, text="Employee ID:", **label_style
        )
        self.employee_id_label.pack()

        self.employee_id_entry = tk.Entry(
            self.frame,
            width=35,
            bg="white",
            fg="black",
            font=("Arial", 12)
        )
        self.employee_id_entry.pack(pady=5)

        # Name
        self.name_label = tk.Label(
            self.frame, text="Name:", **label_style
        )
        self.name_label.pack()

        self.name_entry = tk.Entry(
            self.frame,
            width=35,
            bg="white",
            fg="black",
            font=("Arial", 12)
        )
        self.name_entry.pack(pady=5)

        # Salary
        self.salary_label = tk.Label(
            self.frame, text="Salary:", **label_style
        )
        self.salary_label.pack()

        self.salary_entry = tk.Entry(
            self.frame,
            width=35,
            bg="white",
            fg="black",
            font=("Arial", 12)
        )
        self.salary_entry.pack(pady=5)

        # Leave
        self.leave_label = tk.Label(
            self.frame, text="Leave:", **label_style
        )
        self.leave_label.pack()

        self.leave_entry = tk.Entry(
            self.frame,
            width=35,
            bg="white",
            fg="black",
            font=("Arial", 12)
        )
        self.leave_entry.pack(pady=5)

        # Button style
        button_style = {
            "width": 22,
            "height": 2,
            "bg": "navy",
            "fg": "white",
            "font": ("Arial", 11, "bold")
        }

        self.register_button = tk.Button(
            self.frame,
            text="Register",
            command=self.register_employee,
            **button_style
        )
        self.register_button.pack(pady=5)

        self.login_button = tk.Button(
            self.frame,
            text="Login",
            command=self.login_employee,
            **button_style
        )
        self.login_button.pack(pady=5)

        self.calculate_salary_button = tk.Button(
            self.frame,
            text="Calculate Salary",
            command=self.calculate_salary,
            **button_style
        )
        self.calculate_salary_button.pack(pady=5)

        self.generate_pay_slip_button = tk.Button(
            self.frame,
            text="Generate Pay Slip",
            command=self.generate_pay_slip,
            **button_style
        )
        self.generate_pay_slip_button.pack(pady=5)

        self.search_employee_button = tk.Button(
            self.frame,
            text="Search Employee",
            command=self.search_employee,
            **button_style
        )
        self.search_employee_button.pack(pady=5)

        self.employee_list_button = tk.Button(
            self.frame,
            text="Employee List",
            command=self.employee_list,
            **button_style
        )
        self.employee_list_button.pack(pady=5)

        self.exit_button = tk.Button(
            self.frame,
            text="Exit",
            command=self.root.quit,
            width=22,
            height=2,
            bg="red",
            fg="white",
            font=("Arial", 11, "bold")
        )
        self.exit_button.pack(pady=5)

        # Employee data
        self.employees = {}
        self.load_data()


    def register_employee(self):
        employee_id = self.employee_id_entry.get()
        name = self.name_entry.get()
        salary = float(self.salary_entry.get())
        leave = int(self.leave_entry.get())

        if employee_id in self.employees:
            messagebox.showerror("Error", "Employee ID already exists!")
        else:
            self.employees[employee_id] = {
                'name': name,
                'salary': salary,
                'leave': leave
            }

            self.save_data()

            messagebox.showinfo(
                "Success",
                "Employee registered successfully!"
            )


    def login_employee(self):
        employee_id = self.employee_id_entry.get()

        if employee_id in self.employees:
            employee = self.employees[employee_id]

            messagebox.showinfo(
                "Login Success",
                f"Welcome {employee['name']}!"
            )

        else:
            messagebox.showerror(
                "Error",
                "Employee ID not found!"
            )


    def calculate_salary(self):
        employee_id = self.employee_id_entry.get()

        if employee_id in self.employees:
            employee = self.employees[employee_id]

            salary = employee['salary']
            leave = employee['leave']

            net_salary = salary - (leave * (salary / 30))

            messagebox.showinfo(
                "Salary Calculation",
                f"Net Salary: {net_salary}"
            )

        else:
            messagebox.showerror(
                "Error",
                "Employee ID not found!"
            )


    def generate_pay_slip(self):
        employee_id = self.employee_id_entry.get()

        if employee_id in self.employees:
            employee = self.employees[employee_id]

            salary = employee['salary']
            leave = employee['leave']

            net_salary = salary - (leave * (salary / 30))

            pay_slip = (
                f"Pay Slip\n\n"
                f"Employee ID: {employee_id}\n"
                f"Name: {employee['name']}\n"
                f"Salary: {salary}\n"
                f"Leave: {leave}\n"
                f"Net Salary: {net_salary}"
            )

            messagebox.showinfo(
                "Pay Slip",
                pay_slip
            )

        else:
            messagebox.showerror(
                "Error",
                "Employee ID not found!"
            )


    def search_employee(self):
        employee_id = self.employee_id_entry.get()

        if employee_id in self.employees:
            employee = self.employees[employee_id]

            messagebox.showinfo(
                "Employee Details",
                f"Employee ID: {employee_id}\n"
                f"Name: {employee['name']}\n"
                f"Salary: {employee['salary']}\n"
                f"Leave: {employee['leave']}"
            )

        else:
            messagebox.showerror(
                "Error",
                "Employee ID not found!"
            )


    def employee_list(self):
        employee_list = "\n".join(
            [
                f"ID: {eid}, Name: {data['name']}, "
                f"Salary: {data['salary']}, Leave: {data['leave']}"
                for eid, data in self.employees.items()
            ]
        )

        messagebox.showinfo(
            "Employee List",
            employee_list
        )


    def save_data(self):
        with open("employees.pkl", "wb") as f:
            pickle.dump(self.employees, f)


    def load_data(self):
        if os.path.exists("employees.pkl"):
            with open("employees.pkl", "rb") as f:
                self.employees = pickle.load(f)



if __name__ == "__main__":
    root = tk.Tk()
    app = PayrollSystem(root)
    root.mainloop()
