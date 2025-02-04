# Parts Inventory Management System

The **Parts Inventory Management System** is a Python-based application designed to help users manage inventory for parts. It allows users to add, remove, and update parts, as well as track sales, generate sales reports, and view sales receipts. The system uses a console menu interface for easy navigation and provides data persistence through file storage.

## Features

- **Add New Parts**  
  Add new parts with details such as part ID, name, quantity, production cost, and sale price.

- **Update Inventory**  
  Add stock to existing parts or sell parts while updating the inventory accordingly.

- **View Inventory**  
  Display all parts in a formatted table with details like quantity, production cost, and sale price.

- **Generate Sales Reports**  
  View detailed reports of sold items, including profit calculations.

- **View Sales Receipts**  
  Generate receipts for sold items with total price (including tax) and quantity purchased.

- **File Operations**  
  Save inventory data to a file and load it back for future use.

- **Console Menu Interface**  
  Navigate through the system using a user-friendly console menu powered by the `consolemenu` library.

## File Descriptions

- **final.py**  
  The main script containing:
  - The `Parts` class for representing individual parts.
  - The `PartsManager` class for managing inventory operations like adding, removing, and selling parts.
  - The `PartsManagerUI` class for handling user interactions and generating reports.
  - A console menu interface to navigate the system's features.

- **README.md**  
  Provides an overview of the project, its features, file descriptions, and usage instructions.

## How to Use

1. Clone this repository to your local machine:
git clone https://github.com/muditm006/Parts-Inventory.git
cd Parts-Inventory
2. Install the required Python libraries:
pip install console-menu prettytable
3. Run the program:
python final.py
4. Use the interactive menu to:
- Add new parts.
- Update inventory (add stock or sell parts).
- View inventory details.
- Generate sales reports or view sales receipts.
- Save or load inventory data from a file.

5. Follow on-screen instructions to complete your tasks.

## Example Menu Options

Parts Inventory
- Add New Part
- Manipulate Item =>
- View Reports =>
- File Operations =>
- Exit


Submenus provide additional options for manipulating items, viewing reports, or performing file operations.

## Libraries Used

- **PrettyTable**: For creating formatted tables to display inventory and reports.
- **consolemenu**: For building an interactive console menu interface.
- **pickle**: For saving and loading inventory data to/from files.

## Notes

- The program ensures data integrity by validating inputs (e.g., ensuring quantities are positive or sale prices are not lower than production costs unless explicitly confirmed).
- Sales reports include profit calculations based on the difference between sale price and production cost.
- Sales receipts include tax calculations (7%) on total sales.

This system is ideal for small businesses or individuals looking to manage part inventories efficiently through a simple console-based application.
