from consolemenu import *
from consolemenu.items import *
from prettytable import PrettyTable
import pickle


class Parts:
    def __init__(self, sku, name, qty, sales_price, cost_price):
        self.sku = sku
        self.name = name
        self.qty = qty
        self.qty_sold = 0
        self.sales_price = sales_price
        self.cost_price = cost_price


class PartsManager:

    def __init__(self):
        self.parts = {}

    def add_new_part(self, sku, name, qty, sales_price, cost_price):
        self.parts[sku] = Parts(sku, name, qty, sales_price, cost_price)

    def add_part(self, sku, qty):
        if sku in self.parts:
            self.parts[sku].qty += qty

    def sell_part(self, sku, qty):
        if sku in self.parts:
            self.parts[sku].qty -= qty
            self.parts[sku].qty_sold += qty

    @staticmethod
    def checker(a, b, c):
        while True:
            try:
                if b == 0:
                    value = int(input(a))
                    return value
                elif b == 1:
                    value = float(input(a))
                    if value < 0:
                        input("Production Cost must be greater than 0. Press enter to retry. ")
                    else:
                        return value
                elif b == 2:
                    value = int(input(a))
                    if value < 1:
                        input("Quantity must be greater than 0. Press enter to retry. ")
                    else:
                        return value
                elif b == 3:
                    value = float(input(a))
                    if value < 0:
                        input("Sales Price must be greater than 0. Press enter to retry. ")
                    elif value < c:
                        check = input(
                            "Sales price less than production cost! Are you sure you want to continue? (Print 'Yes' to do so, print anything else to redo.) ")
                        check = check.lower()
                        if check == "yes":
                            return value
                        else:
                            pass
                    else:
                        return value
            except ValueError:
                input("Input a number!, Press enter to retry. ")

    def save(self):
        with open("mdm_inventory.txt", "wb") as inventoryfile:
            pickle.dump(self.parts, inventoryfile)
        input("Data Saved. Press enter to return to menu. ")

    def load(self):
        try:
            with open("mdm_inventory.txt", "rb") as inventoryfile:
                self.parts = pickle.load(inventoryfile)
            input("Data retrieved, press enter to return to menu. ")
        except FileNotFoundError:
            input("File doesn't exist! Press enter to return to Menu. ")


class PartsManagerUI:
    def __init__(self):
        self.partsMan = PartsManager()
        self.receiptMan = PartsManager()

    def add_part(self):
        # This code is how the user inputs the item into the system.
        a = self.partsMan.checker("Please enter in part ID ", 0, 0)
        if a not in self.partsMan.parts:
            b = input("Please enter in the part name. ")
            c = self.partsMan.checker("Please enter in the quantity. ", 2, 0)
            d = self.partsMan.checker("Please enter in the production cost. ", 1, 0)
            e = self.partsMan.checker("Please enter in the sale price. ", 3, d)
            self.partsMan.add_new_part(a, b, c, e, d)
            input("Part Number " + str(a) + " entered/updated into system. Press Enter to return to menu.")
        else:
            input("Part already exists! Press enter to return to menu. ")

    def view(self):
        # This code creates a table that looks nice so that the user gets the data in a nice format.
        myprettytable = PrettyTable()
        myprettytable.field_names = ['Part Number', 'Name', 'Quantity', "Production Cost", "Sale Price"]
        for part in self.partsMan.parts:
            p = self.partsMan.parts[part]
            if part in self.receiptMan.parts:
                q = self.receiptMan.parts[part]
                myprettytable.add_row([p.sku, p.name, q.qty, '${:,.2f}'.format(int(p.cost_price)), '${:,.2f}'.format(int(p.sales_price))])
            else:
                myprettytable.add_row([p.sku, p.name, p.qty, '${:,.2f}'.format(int(p.cost_price)), '${:,.2f}'.format(int(p.sales_price))])
        print(myprettytable)
        input("Continue? ")

    def sell(self):
        PartsManagerUI.view(self)
        while True:
            try:
                a = input("Please enter in part ID. ")
                if int(a) not in self.partsMan.parts:
                    input("Part Doesn't exist!")
                else:
                    break
            except ValueError:
                print("Please enter in number!")
        b = self.partsMan.checker("How many parts are you buying? ", 2, 0)
        c = self.partsMan.parts[int(a)]
        if c.qty-b < 0:
            input("Cannot sell that many parts! There are only " + str(c.qty) + " part(s) available. Press enter to return to menu.")
        else:
            self.receiptMan.parts[int(a)] = Parts(int(a), c.name, c.qty, c.sales_price, c.cost_price)
            self.receiptMan.sell_part(int(a), b)
            d = self.receiptMan.parts[int(a)]
            self.partsMan.parts[int(a)] = Parts(int(a), c.name, d.qty, c.sales_price, c.cost_price)

    def add(self):
        PartsManagerUI.view(self)
        while True:
            try:
                a = input("Please enter in part ID. ")
                if int(a) not in self.partsMan.parts:
                    input("Part Doesn't exist!")
                else:
                    break
            except ValueError:
                print("Please enter in number!")
        b = self.partsMan.checker("How many parts are you adding? ", 2, 0)
        self.partsMan.add_part(int(a), b)

    def sales_report(self):
        print("Sales Report")
        myprettytable = PrettyTable()
        myprettytable.field_names = ['Part Number', "Name", 'Production Cost', "Sales Price", 'Quantity Sold', "Profit Made"]
        for part in self.receiptMan.parts:
            p = self.receiptMan.parts[part]
            profit = p.qty_sold*(p.sales_price-p.cost_price)
            myprettytable.add_row(
                [p.sku, p.name, '${:,.2f}'.format(int(p.cost_price)), '${:,.2f}'.format(int(p.sales_price)), p.qty_sold, '${:,.2f}'.format(int(profit))])
        print(myprettytable)
        input("Continue? ")

    def sales_receipt(self):
        myprettytable = PrettyTable()
        myprettytable.field_names = ['Part Number', "Name",  "Total Price", 'Quantity Bought']
        for part in self.receiptMan.parts:
            p = self.receiptMan.parts[part]
            cost = '${:,.2f}'.format(.07*(p.sales_price*p.qty_sold)+p.sales_price*p.qty_sold)
            myprettytable.add_row([p.sku, p.name, cost, p.qty_sold])
        print(myprettytable)
        input("Continue? ")
        input("Press enter to return to menu.")

    def save(self):
        self.partsMan.save()

    def load(self):
        self.partsMan.load()


pmu = PartsManagerUI()

# Create the menu
menu = ConsoleMenu("Parts Inventory")


New_Part = FunctionItem("Add New Part", pmu.add_part)
Viewing = FunctionItem("View Parts", pmu.view)
Sell = FunctionItem("Sell Part", pmu.sell)
Add = FunctionItem("Add Part", pmu.add)
Save = FunctionItem("Save to File", pmu.save)
Load = FunctionItem("Load from File", pmu.load)
Sales = FunctionItem("View Sales Report", pmu.sales_report)
Receipt = FunctionItem("View Sales Receipt", pmu.sales_receipt)

# A SelectionMenu constructs a menu from a list of strings
selection_menu = (SelectionMenu("", "Manipulate Part", "", exit_option_text="Return to Main Menu"))
selection_menu.append_item(Add)
selection_menu.append_item(Sell)
file_selection_menu = SelectionMenu("", "File Operations", "", exit_option_text="Return to Main Menu")
file_selection_menu.append_item(Load)
file_selection_menu.append_item(Save)
report_selection_menu = SelectionMenu("", "View Information", "", exit_option_text="Return to Main Menu")
report_selection_menu.append_item(Sales)
report_selection_menu.append_item(Viewing)
report_selection_menu.append_item(Receipt)
# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Manipulate Item =>", selection_menu, menu)
file_selection_item = SubmenuItem("File Operations =>", file_selection_menu, menu)
report_item = SubmenuItem("View Reports =>", report_selection_menu, menu)

menu.append_item(file_selection_item)
menu.append_item(New_Part)
menu.append_item(submenu_item)
menu.append_item(report_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
