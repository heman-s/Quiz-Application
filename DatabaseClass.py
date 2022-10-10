## DATABASE CLASS

##from UserClass import * 
import sqlite3
import shutil

## Creates a parent class for all database functions
class DatabaseFunction:
    ## Assigns attributes for database functions
    def __init__(self, newType):
        self.__type = newType

    ## Encapsulation of DatabaseFunction Class (Set Methods)
    def setType(self, newType):    
        self.__type = newType

    ## Encapsulation of DatabaseFunction Class (Get Methods)
    def getType(self):    
        return self.__type

    ## Open Connection Function
    def openConnection(self, databaseFile):
        ## Initiates the database with the name stored in databaseFile along with its cursor
        conn = sqlite3.connect(databaseFile)
        c = conn.cursor()
        return conn, c

    ## Add To Database Function
    def addToDatabase(self, conn, c, record, table):
        ## If to be added to UserDetails table or Question table
        if len(record) == 8:
            # Establish SQL statement
            sqlAdd = ("INSERT INTO " + table + " VALUES (?,?,?,?,?,?,?,?)")
        ## If to be added to UserReview table
        elif len(record) == 2:
            sqlAdd = ("INSERT INTO " + table + " VALUES (?,?)")
        ## If to be added to Quiz table
        elif len(record) == 4:
            sqlAdd = ("INSERT INTO " + table + " VALUES (?,?,?,?)")
        ## If to be added to Question table
        if len(record) == 12:
            # Establish SQL statement
            sqlAdd = ("INSERT INTO " + table + " VALUES (?,?,?,?,?,?,?,?,?,?,?,?)")
        ## If to be added to Progress table
        elif len(record) == 6:
            sqlAdd = ("INSERT INTO " + table + " VALUES (?,?,?,?,?,?)")

        self.saveTransaction(sqlAdd, record, conn, c)
        self.atomicTransaction(sqlAdd, record, conn, c)

    ## View From Database Function
    def viewFromDatabase(self, c, allFields, allRecords, field, recordPrimaryKey, recordPrimaryKeyValue, table):
        ## Retrieve and display all items from a table
        if allFields == True and allRecords == True:
            sqlView = ("SELECT * FROM " + table)
        ## Retrieve and display all items from a record
        elif allFields == True and allRecords == False:
            sqlView = ("SELECT * FROM " + table + " WHERE " + recordPrimaryKey + " = " + str(recordPrimaryKeyValue))
        ## Retrieve and display all items from a field
        elif allFields == False and allRecords == True:
            sqlView = ("SELECT " + field + " FROM " + table)
        ## Retrieve and display an item from a field from a specific record
        elif allFields == False and allRecords == False:
            sqlView = ("SELECT " + field + " FROM " + table + " WHERE " + recordPrimaryKey + " = " + str(recordPrimaryKeyValue))
        c.execute(sqlView)
        return c.fetchall()

    ## Update In Database Function
    def updateInDatabase(self, conn, c, field, updatedData, recordPrimaryKey, recordPrimaryKeyValue, table):
        sqlUpdate = ("UPDATE " + table + " SET " + field + " = '" + updatedData + "' WHERE " + recordPrimaryKey + " = " + str(recordPrimaryKeyValue))
        record = []
        self.saveTransaction(sqlUpdate, record, conn, c)
        self.atomicTransaction(sqlUpdate, record, conn, c)
            
    ## Delete From Database Function
    def deleteFromDatabase(self, conn, c, recordPrimaryKey, recordPrimaryKeyValue, table):
        sqlDelete = ("DELETE from " + table + " WHERE " + recordPrimaryKey + " = " + str(recordPrimaryKeyValue))
        record = []
        self.saveTransaction(sqlDelete, record, conn, c)
        self.atomicTransction(sqlDelete, record, conn, c)

    ## Create Class Object from Database Record
    def createObjectOfClassFromDatabase(self, c, allFields, allRecords, field, recordPrimaryKey, recordPrimaryKeyValue, table):
        record = self.viewFromDatabase(c, allFields, allRecords, field, recordPrimaryKey, recordPrimaryKeyValue, table)
        userOne = User(*record[0])

    ## Transaction Atomicity
    def atomicTransaction(self, sqlCommand, record, conn, c):
        try:
            ## For updating and deleting
            if record == []:
                # Execute SQL command
                c.execute(sqlCommand)
            ## For adding
            else:
                c.execute(sqlCommand, record)
            # Commit changes to database
            conn.commit()
            with open('sqlCommands.txt', 'w') as file:
                file.write('')
            self.createBackupDBFile(databaseFile)
        except:
            # Rollback in case of error (reverts database to earlier state)
            conn.rollback()

    ## Transaction Durability
    def saveTransaction(self, sqlCommand, record, conn, c):
        # Save SQL command to external text file
        with open('sqlCommands.txt', 'w') as file:
                file.write(sqlCommand + '\n')
                for each in record:
                        file.write(str(each) + '\n')

    ## Check whether any pending transactions (and execute)
    def readTransaction(self):
        # Read SQL command from external text file (if any)
        with open('sqlCommands.txt', 'r') as file:
            sqlCommand = file.readline()
            sqlCommand = sqlCommand.rstrip('\n')
            record = [line.rstrip() for line in file]

        # If file isn't blank, open backup database file and execute instruction
        if sqlCommand != '':
            databaseFile = 'AccountInfo2.db'
            conn, c = self.openConnection(databaseFile)
            self.atomicTransaction(sqlCommand, record, conn, c)
            self.createBackupDBFile(databaseFile)
        # If file is blank, open original database file
        else:
            databaseFile = 'AccountInfo.db'
            conn, c = self.openConnection(databaseFile)

        return conn, c

    ## Create Backup Database File
    def createBackupDBFile(self, databaseFile):
        if databaseFile == 'AccountInfo.db':
            backupFile = 'AccountInfo2.db'
        else:
            backupFile = 'AccountInfo.db'
        shutil.copy2(databaseFile, backupFile)

    ## Perform an inner join on two tables (combine two tables)
    def innerJoin(self, c, tableFields, table1, table2, table1MatchingField, table2MatchingField):
        table = c.execute("SELECT " + tableFields + " FROM " + table1 + " INNER JOIN " + table2 + " ON " + table1MatchingField + " = " + table2MatchingField)
        newTable = table.fetchall()
        return newTable

    ## Close Connection Function
    def closeConnection(self):
        conn.commit()
        conn.close()  

## Creates a new instance of the DatabaseFunction class for the different functions
openingConnection = DatabaseFunction('Open')
addingToDatabase = DatabaseFunction('Add')
updatingDatabase = DatabaseFunction('Update')
deletingFromDatabase = DatabaseFunction('Delete')
saveTransactionToFile = DatabaseFunction('Save')
readTransactionFromFile = DatabaseFunction('Read')
viewingFromDatabase = DatabaseFunction('View')
createBackupFile = DatabaseFunction('Backup')
innerJoinTables = DatabaseFunction('InnerJoin')
closingConnection = DatabaseFunction('Close')

conn, c = readTransactionFromFile.readTransaction()

##allFields = 
##allRecords = 
##field = 
##recordPrimaryKey = 
##recordPrimaryKeyValue = 
##table =

##addingToDatabase.addToDatabase(conn, c, record, table)
##print(viewingFromDatabase.viewFromDatabase(c, allFields, allRecords, field, recordPrimaryKey, recordPrimaryKeyValue, table))
##viewingFromDatabase.createObjectOfClassFromDatabase(c, allFields, allRecords, field, recordPrimaryKey, recordPrimaryKeyValue, table)
##updatingDatabase.updateInDatabase(conn, c, field, updatedData, recordPrimaryKey, recordPrimaryKeyValue, table)
##deletingFromDatabase.deleteFromDatabase(conn, c, recordPrimaryKey, recordPrimaryKeyValue, table)    

#closingConnection.closeConnection()
