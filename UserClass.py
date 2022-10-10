## User, Admin, Student Classes

## Creates a parent class for all users
class User:
    def __init__(self, newUserID, newAccountType, newUsername, newPassword, newFirstName, newLastName, newReviewID):
        self.__userID = newUserID
        self.__accountType = newAccountType
        self.__username = newUsername
        self.__password = newPassword
        self.__firstName = newFirstName
        self.__lastName = newLastName
        self.__reviewID = newReviewID

## Encapsulation of User Class (Set Methods)
    def setUserID(self, newUserID):    
        self.__userID = newUserID

    def setAccountType(self, newAccountType):    
        self.__accountType = newAccountType       

    def setUsername(self, newUsername):    
        self.__username = newUsername

    def setPassword(self, newPassword):    
        self.__password = newPassword

    def setFirstName(self, newFirstName):    
        self.__firstName = newFirstName

    def setLastName(self, newLastName):    
        self.__lastName = newLastName

    def setReview(self, newReviewID):    
        self.__reviewID = newReviewID

## Encapsulation of User Class (Get Methods)
    def getUserID(self):    
        return self.__userID

    def getAccountType(self):    
        return self.__accountType       

    def getUsername(self):    
        return self.__username

    def getPassword(self):    
        return self.__password

    def getFirstName(self):    
        return self.__firstName

    def getLastName(self):    
        return self.__lastName

    def getReviewID(self):    
        return self.__reviewID

    def getAllDetails(self):
        return [User.getUserID(self), User.getAccountType(self), User.getUsername(self), User.getPassword(self), User.getFirstName(self), User.getLastName(self), User.getReviewID(self)]

##heman = User(1, 'Admin', 'hemanseego01', 'Pass-word123', 'Heman', 'Seegolam', 1)
##sam = User(2, 'Student', 'sampinch02', 'Pass-word123', 'Sam', 'Pinchback', 1)
##matt = User(3, 'Parent', 'mattbumpus03', 'Pass-word123', 'Matt', 'Bumpus', 2)
##print(heman.getAllDetails())
##print(sam.getAllDetails())
##print(matt.getAllDetails())
