import customtkinter as ctk
from tkinter import ttk

# Set appearance and theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class PharmacyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PharmaFlow Management System")
        self.geometry("1100x700")

        # Configure grid layout (1x2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar Frame ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="PharmaFlow", font=ctk.CTkFont(size=24, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.dashboard_button = ctk.CTkButton(self.sidebar_frame, text="Dashboard", command=self.dashboard_event)
        self.dashboard_button.grid(row=1, column=0, padx=20, pady=10)

        self.inventory_button = ctk.CTkButton(self.sidebar_frame, text="Inventory", command=self.inventory_event)
        self.inventory_button.grid(row=2, column=0, padx=20, pady=10)

        self.sales_button = ctk.CTkButton(self.sidebar_frame, text="Sales", command=self.sales_event)
        self.sales_button.grid(row=3, column=0, padx=20, pady=10)

        self.logout_button = ctk.CTkButton(self.sidebar_frame, text="Logout", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.logout_button.grid(row=5, column=0, padx=20, pady=20)

        # --- Main Content Frame ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Header
        self.header_label = ctk.CTkLabel(self.main_frame, text="Welcome back, Dr. Sarah", font=ctk.CTkFont(size=28, weight="bold"))
        self.header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="w")
        
        self.sub_header = ctk.CTkLabel(self.main_frame, text="Pharmacy Overview", text_color="gray")
        self.sub_header.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="w")

        # --- Stats Cards ---
        self.sales_card = self.create_stat_card(self.main_frame, "Total Sales", "$24,580", 2, 0)
        self.medicine_card = self.create_stat_card(self.main_frame, "Medicines", "1,240", 2, 1)
        self.customer_card = self.create_stat_card(self.main_frame, "Customers", "842", 2, 2)

        # --- Inventory Table Section ---
        self.table_label = ctk.CTkLabel(self.main_frame, text="Recent Inventory", font=ctk.CTkFont(size=18, weight="bold"))
        self.table_label.grid(row=3, column=0, padx=20, pady=(30, 10), sticky="w")

        # Using standard Tkinter Treeview for the table (styled for dark mode)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", borderwidth=0)
        style.map("Treeview", background=[('selected', '#1f538d')])

        self.tree = ttk.Treeview(self.main_frame, columns=("Name", "Category", "Stock", "Price"), show='headings')
        self.tree.heading("Name", text="Medicine Name")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Stock", text="Stock Level")
        self.tree.heading("Price", text="Price")
        
        # Add mock data
        medicines = [
            ("Amoxicillin", "Antibiotics", "450", "$12.50"),
            ("Lisinopril", "Blood Pressure", "12", "$18.00"),
            ("Metformin", "Diabetes", "230", "$15.20"),
            ("Atorvastatin", "Cholesterol", "0", "$22.00")
        ]
        for med in medicines:
            self.tree.insert("", "end", values=med)

        self.tree.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky="nsew")

    def create_stat_card(self, parent, title, value, row, col):
        card = ctk.CTkFrame(parent, corner_radius=15, border_width=1, border_color="#333333")
        card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        lbl_title = ctk.CTkLabel(card, text=title, text_color="gray")
        lbl_title.pack(pady=(15, 0))
        
        lbl_value = ctk.CTkLabel(card, text=value, font=ctk.CTkFont(size=24, weight="bold"))
        lbl_value.pack(pady=(0, 15))
        return card

    def dashboard_event(self):
        print("Dashboard Clicked")

    def inventory_event(self):
        print("Inventory Clicked")

    def sales_event(self):
        print("Sales Clicked")

if __name__ == "__main__":
    app = PharmacyApp()
    app.mainloop()
