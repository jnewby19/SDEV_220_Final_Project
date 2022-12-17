"""
------------------------------------------------------------------------------------------------------------------------------------
Program Name: Absolute Mechanic Client Directory - main.py

SDEV 220

Contributors:
    Ayden Pitstick - Editor
    Marcos Valencia - Editor
    Josh Lanier - Documentation

Last Revision: 2022-12-16

Program Purpose: To give auto mechanics and staff at Absolute Mechanic an easy to navigate client directory, where they can access 
a directory of clients, their cars, and issues, and add, edit, and delete them.

Module Purpose: To provide the 'main()' function as a script entry point for the package, called by the 'rpcontacts.py' module. It 
basically initiates the program and its main elements.

   
------------------------------------------------------------------------------------------------------------------------------------
"""

import sys

from PyQt5.QtWidgets import QApplication


from .database import createConnection
from .views import Window


def main():
    """RP Contacts main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # Create the main window if the connection succeeded
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())