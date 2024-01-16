import tkinter as tk
from tkinter import ttk, messagebox

class BudgetCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Budget Calculator")

        self.total_label = ttk.Label(master, text="Total Amount:")
        self.total_label.grid(row=0, column=0, padx=10, pady=10)

        self.total_entry = ttk.Entry(master)
        self.total_entry.grid(row=0, column=1, padx=10, pady=10)

        self.calculate_button = ttk.Button(master, text="Calculate", command=self.calculate_budget)
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def calculate_budget(self):
        try:
            total_amount = float(self.total_entry.get())

            tour_budget = total_amount * 0.02
            pocket_money = total_amount * 0.03
            backup_money = total_amount * 0.03
            Reserve_Money = 2000
            internet_bill = 500
            parents_share = total_amount - (tour_budget + pocket_money + backup_money + internet_bill + Reserve_Money )

            result_message = f"Tour Budget (2%): {tour_budget:.2f} Taka\n" \
                             f"Pocket Money (3%): {pocket_money:.2f} Taka\n" \
                             f"Backup Money (3%): {backup_money:.2f} Taka\n" \
                             f"Internet Bill: {internet_bill:.2f} Taka\n" \
                             f"Reserve_Money: {Reserve_Money:.2f} Taka\n" \
                             f"Parents Share: {parents_share:.2f} Taka"

            messagebox.showinfo("Result", result_message)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid total amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetCalculatorApp(root)
    root.mainloop()
