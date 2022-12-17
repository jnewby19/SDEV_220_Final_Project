##SDEV 220 FINAL PROJECT README.md

Program Name: Absolute Mechanic Client Directory

Contributors:
    Jacob Newby
    Willie Alford
    Ayden Pitstick
    Marcos Valencia
    Josh Lanier

Last Revision: 2022-12-16

Purpose: To give auto mechanics and staff at Absolute Mechanic an easy to navigate client directory, where they can access a directory of clients, their cars, and issues, and add, edit, and delete them.

----------------------------------------------------

Directory:

rpcontact_project/
    |
    Documentation/
        |
        SDEV_220_FinalProject_ClassDiagram.png
        SDEV_220_Final_Project_Launch_updated.docx
        Test_Results.txt
    rpcontacts/
        |
        __init__.py
        database.py
        main.py
        model.py
        views.py
    contacts.sqlite
    requirements.txt
    rpcontacts.py

----------------------------------------------------

Dependencies:
-PyQt5, version 5.15.7

To install using a terminal or command line, use the command 'pip install PyQt5'.

----------------------------------------------------

1. Starting program from a file explorer:

- Open 'rpcontacts.py'. The application window should open.

Starting program from IDE:

- Open the 'rpcontacts_project' folder in the IDE. Run the 'rpcontacts.py' file.

2. Application window navigation:

- Application is contained in one main window, with popup windows for adding, deleting, and clearing the client records in the table view.

- Table view allows for real time editing of the table cells.

- Buttons on the side allow for adding, deleting, and clearing client records.

3. Editing client records:

- To edit table cells, double click a cell, edit the cell contacts, then press the 'Enter' key. Cells will automatically update the database.

4. Adding client records:

- Click the 'Add...' button on the right side of the window. An 'Add Contact' window will appear.

- Input entries in each of the 'Name', 'Car', and 'Issue' fields.

- Click 'OK' to commit the addition of the contact. Click 'Cancel' to discard the addition.

- Click 'OK' adds the entries just inputted to a record at the bottom of the table in the main window and adds it to the database.

5. Deleting client records:

- Click once on a cell in the row that you want to delete and the row will highlight.

- Click the 'Delete' button on the right side of the window. A 'Warning!' window will appear, asking 'Do you want to remove the selected contact?'.

- Click 'OK' if you want to commit the deletion. Click 'Cancel' to discard the deletion and to keep the client record.

- Clicking 'OK' deletes the record from the table and from the database.

6. Clearing the entire table:

- Click the 'Clear All' button at the bottom right corner of the window. A 'Warning!' window will appear, asking 'Do you want to remove all your contacts?'.

- Click 'OK' if you want to commit the clearing of the entire table. Click 'Cancel' to discard the clear and to keep the current status of the client records.

- Clicking 'OK' clears all records from the table and from the database.

7. Exiting:

- To exit, click the 'X' at the top right of the window.

