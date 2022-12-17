"""
------------------------------------------------------------------------------------------------------------------------------------
Program Name: Absolute Mechanic Client Directory - database.py

SDEV 220

Contributors:
    Ayden Pitstick - Editor
    Josh Lanier - Documentation

Last Revision: 2022-12-16

Program Purpose: To give auto mechanics and staff at Absolute Mechanic an easy to navigate client directory, where they can access 
a directory of clients, their cars, and issues, and add, edit, and delete them.

Module Purpose: To create and manage the connection with the SQLite3 database that provides the records and data for the table.

------------------------------------------------------------------------------------------------------------------------------------
"""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def createConnection(databaseName):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(None, "RP Contact", f"Database Error: {connection.lastError().text()}",)
        return False
    createContactsTable()
    return True

def createContactsTable():
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            car VARCHAR(100) NOT NULL,
            issue VARCHAR(50)
          )
        """
    )

