import tkinter as tk
from tkinter import messagebox


class PalletContainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pallet Container Placement")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.pallet_listbox = tk.Listbox(self.frame, width=30, height=10)
        self.pallet_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(
            self.frame, orient=tk.VERTICAL, command=self.pallet_listbox.yview
        )
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.pallet_listbox.config(yscrollcommand=self.scrollbar.set)

        self.add_button = tk.Button(
            self.frame, text="Add Pallet", command=self.add_pallet
        )
        self.add_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.calculate_button = tk.Button(
            self.frame, text="Calculate Placement", command=self.calculate_placement
        )
        self.calculate_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.pallets = []

    def add_pallet(self):
        # Hier kun je een dialoogvenster toevoegen om de gebruiker om de afmetingen te vragen
        pallet = self.get_pallet_dimensions()
        if pallet:
            self.pallets.append(pallet)
            self.pallet_listbox.insert(tk.END, f"Pallet {len(self.pallets)}: {pallet}")

    def get_pallet_dimensions(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Enter Pallet Dimensions")

        width_entry = tk.Entry(dialog, width=10)
        width_entry.pack(padx=10, pady=10)
        height_entry = tk.Entry(dialog, width=10)
        height_entry.pack(padx=10, pady=10)

        def on_ok():
            width = width_entry.get()
            height = height_entry.get()
            if width and height:
                dialog.destroy()
                return f"{width} x {height}"
            else:
                messagebox.showwarning(
                    "Input Error", "Please enter both width and height"
                )

        ok_button = tk.Button(dialog, text="OK", command=on_ok)
        ok_button.pack(padx=10, pady=10)

        self.root.wait_window(dialog)

    def calculate_placement(self):
        if not self.pallets:
            messagebox.showwarning("No Pallets", "Please add some pallets first")
            return

        container_width = 12.192  # 40 FT container in m²
        container_height = container_width  # Assuming square container for simplicity

        # Hier kun je een heuristiek toepassen om de pallets in de container te plaatsen
        # Voor dit voorbeeld gebruiken we een eenvoudige heuristiek
        placed_pallets = []
        for pallet in self.pallets:
            if container_width >= pallet[0] and container_height >= pallet[1]:
                placed_pallets.append(pallet)
                container_width -= pallet[0]
                container_height -= pallet[1]

        messagebox.showinfo("Placement Result", f"Placed {len(placed_pallets)} pallets")


if __name__ == "__main__":
    root = tk.Tk()
    app = PalletContainerApp(root)
    root.mainloop()
