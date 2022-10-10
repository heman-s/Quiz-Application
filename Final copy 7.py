from DatabaseClass import *
import tkinter as tk
from tkinter import font
from tkinter import ttk
import re
import hashlib
from PIL import Image, ImageTk
import time
from datetime import datetime
import random
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import operator
import math

## Creates a parent class for all interfaces
class Interface:
    ## Assigns attributes for all interfaces (height and width)
    def __init__(self, newScreenWidth, newScreenHeight):
        self.__screenWidth = newScreenWidth
        self.__screenHeight = newScreenHeight

    ## Encapsulation of Interface Class (Set Methods)
    def setScreenWidth(self, newScreenWidth):    
        self.__screenWidth = newScreenWidth

    def setScreenHeight(self, newScreenHeight):    
        self.__screenHeight = newScreenHeight

    ## Encapsulation of Interface Class (Get Methods)
    def getScreenWidth(self):    
        return self.__screenWidth

    def getScreenHeight(self):    
        return self.__screenHeight

    def adminMainMenuPage(self, username, titleFont, buttonFont, defaultFont):
        mainMenuAdmin = tk.Tk()
        mainMenuAdmin.title("Main Menu")

        ## Retrieves the assigned width and height for the main menu page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()

        mainMenuAdmin.geometry(str(mainScreenWidth)+'x'+str(mainScreenHeight))
        mainMenuAdmin.resizable(False, False)

        canvas = tk.Canvas(mainMenuAdmin, height = mainScreenHeight, width = mainScreenWidth, bg = '#80c1ff', highlightthickness=0, relief='ridge')   
        canvas.pack(fill = 'both', expand = True) ## Use to allow user to choose dimensions later --> height//2 - (imageSize//2)

        firstName = viewingFromDatabase.viewFromDatabase(c, False, False, 'firstName', 'username', "'"+username+"'", 'UserDetails')        
        welcomeLabel = tk.Label(canvas, text = "Welcome "+firstName[0][0], bg = 'gray', font = titleFont)
        welcomeLabel.place(relx = 0, rely = 0, relheight = 0.15, relwidth = 1)

        menuOptionImage = Image.open('MenuOption.png')
        menuOptionImage = menuOptionImage.resize((202,282))

        faintMenuOptionImage = Image.open('FaintMenuOption.png')
        faintMenuOptionImage = faintMenuOptionImage.resize((202,282))

        faintMenuOptionImage2 = Image.open('FaintMenuOption2.png')
        faintMenuOptionImage2 = faintMenuOptionImage2.resize((202,282))

        rightArrowImage = Image.open('RightArrow.png')
        rightArrowImage = rightArrowImage.resize((54,93))

        leftArrowImage = Image.open('LeftArrow.png')
        leftArrowImage = leftArrowImage.resize((54,93))

        settingsImage = Image.open('Settings.png')

        selectButtonImage = Image.open('SelectButton.png')
        selectButtonImage = selectButtonImage.resize((135,55))

        tkMenuOptionImage = ImageTk.PhotoImage(menuOptionImage)
        tkFaintMenuOptionImage = ImageTk.PhotoImage(faintMenuOptionImage)
        tkFaintMenuOptionImage2 = ImageTk.PhotoImage(faintMenuOptionImage2)
        tkRightArrowImage = ImageTk.PhotoImage(rightArrowImage)
        tkLeftArrowImage = ImageTk.PhotoImage(leftArrowImage)
        tkSettingsImage = ImageTk.PhotoImage(settingsImage)
        tkSelectButtonImage = ImageTk.PhotoImage(selectButtonImage)

        fainterMenuOption1 = canvas.create_image(95,200, image = tkFaintMenuOptionImage2, anchor = 'nw')
        faintMenuOption1 = canvas.create_image(247,250, image = tkFaintMenuOptionImage, anchor = 'nw')
        menuOption = canvas.create_image(399,300, image = tkMenuOptionImage, anchor = 'nw')
        faintMenuOption2 = canvas.create_image(551,250, image = tkFaintMenuOptionImage, anchor = 'nw')
        fainterMenuOption2 = canvas.create_image(703,200, image = tkFaintMenuOptionImage2, anchor = 'nw')
        rightArrow = canvas.create_image(850,350, image = tkRightArrowImage, anchor = 'nw')
        leftArrow = canvas.create_image(96,350, image = tkLeftArrowImage, anchor = 'nw')
        settings = canvas.create_image(935,635, image = tkSettingsImage, anchor = 'nw')
        selectButton = canvas.create_image(435,550, image = tkSelectButtonImage, anchor = 'nw')

        optionLabel = tk.Label(canvas, text = "Play Quiz", bg = '#80c1ff', font = titleFont)
        optionLabel.place(relx = 0.4, rely = 0.32, relheight = 0.06, relwidth = 0.2)

        canvas.tag_bind(rightArrow, "<Button-1>", lambda x: self.rightArrowPressed(mainMenuAdmin, canvas, optionLabel, fainterMenuOption1, faintMenuOption1, menuOption, faintMenuOption2, fainterMenuOption2, tkMenuOptionImage, tkFaintMenuOptionImage))
        canvas.tag_bind(leftArrow, "<Button-1>", lambda x: self.leftArrowPressed(mainMenuAdmin, canvas, optionLabel, fainterMenuOption1, faintMenuOption1, menuOption, faintMenuOption2, fainterMenuOption2, tkMenuOptionImage, tkFaintMenuOptionImage))
        canvas.tag_bind(selectButton, "<Button-1>", lambda x: self.selectButtonPressed(mainMenuAdmin, username, optionLabel))
        canvas.tag_bind(settings, "<Button-1>", lambda x: self.settingsMenu(username, Login.titleFont, Login.buttonFont, Login.defaultFont))
                                                                          
        mainMenuAdmin.mainloop()

    def studentMainMenuPage(self, username, titleFont, buttonFont, defaultFont):
        mainMenuStudent = tk.Tk()
        mainMenuStudent.title("Main Menu")

        ## Retrieves the assigned width and height for the main menu page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()

        ## Sets the dimensions of the page and sets it to non-resizable
        mainMenuStudent.geometry(str(mainScreenWidth)+'x'+str(mainScreenHeight))
        mainMenuStudent.resizable(False, False)

        ## Creates a canvas for all the menu options
        canvas = tk.Canvas(mainMenuStudent, height = mainScreenHeight, width = mainScreenWidth, highlightthickness=0, relief='ridge')   
        canvas.pack(fill = 'both', expand = True)

        ## Retrieve first name from database using username
        firstName = viewingFromDatabase.viewFromDatabase(c, False, False, 'firstName', 'username', "'"+username+"'", 'UserDetails')
        ## Create welcome label using first name
        welcomeLabel = tk.Label(canvas, text = "Welcome "+firstName[0][0], bg = 'gray', font = titleFont)
        welcomeLabel.place(relx = 0, rely = 0, relheight = 0.15, relwidth = 1)

        ## Import menu option and settings images and resize them
        menuOptionOneImage = Image.open('StudentMenuOptionOne.png')
        menuOptionOneImage = menuOptionOneImage.resize((1007,265))

        menuOptionTwoImage = Image.open('StudentMenuOptionTwo.png')
        menuOptionTwoImage = menuOptionTwoImage.resize((1007,315))

        menuOptionThreeImage = Image.open('StudentMenuOptionThree.png')
        menuOptionThreeImage = menuOptionThreeImage.resize((1007,190))

        settingsImage = Image.open('Settings.png')

        ## Convert them to tkinter images
        tkMenuOptionOneImage = ImageTk.PhotoImage(menuOptionOneImage)
        tkMenuOptionTwoImage = ImageTk.PhotoImage(menuOptionTwoImage)
        tkMenuOptionThreeImage = ImageTk.PhotoImage(menuOptionThreeImage)
        tkSettingsImage = ImageTk.PhotoImage(settingsImage)

        ## Add the images to the canvas
        menuOptionOne = canvas.create_image(-3,99, image = tkMenuOptionOneImage, anchor = 'nw')
        menuOptionTwo = canvas.create_image(-3,270, image = tkMenuOptionTwoImage, anchor = 'nw')
        menuOptionThree = canvas.create_image(-3,514, image = tkMenuOptionThreeImage, anchor = 'nw')
        settings = canvas.create_image(935,635, image = tkSettingsImage, anchor = 'nw')

        ## Create labels for the menu options
        optionOneLabel = tk.Label(canvas, text = "Play Quiz", bg = 'gray', font = titleFont)
        optionOneLabel.place(relx = 0.2, rely = 0.3, relheight = 0.06, relwidth = 0.12)

        optionTwoLabel = tk.Label(canvas, text = "View Progress", bg = 'gray', font = titleFont)
        optionTwoLabel.place(relx = 0.7, rely = 0.6, relheight = 0.06, relwidth = 0.17)

        optionThreeLabel = tk.Label(canvas, text = "Log Off", bg = 'gray', font = titleFont)
        optionThreeLabel.place(relx = 0.07, rely = 0.85, relheight = 0.06, relwidth = 0.1)

        ## Bind the images and labels to destroy the main meny page and go to the relevant function
        canvas.tag_bind(menuOptionOne, "<Button-1>", lambda x: (mainMenuStudent.destroy(), self.playQuiz(username, Login.titleFont, Login.defaultFont, Login.buttonFont)))
        optionOneLabel.bind("<Button-1>", lambda x: (mainMenuStudent.destroy(), self.playQuiz(username, Login.titleFont, Login.defaultFont, Login.buttonFont)))
        
        canvas.tag_bind(menuOptionTwo, "<Button-1>", lambda x: (mainMenuStudent.destroy(), self.viewClasses(username, Login.titleFont, Login.defaultFont, Login.buttonFont)))
        optionTwoLabel.bind("<Button-1>", lambda x: (mainMenuStudent.destroy(), self.viewClasses(username, Login.titleFont, Login.defaultFont, Login.buttonFont)))

        canvas.tag_bind(menuOptionThree, "<Button-1>", lambda x: (mainMenuStudent.destroy(), self.logOff()))
        optionThreeLabel.bind("<Button-1>", lambda x: (mainMenuStudent.destroy(), self.logOff()))
                            
        canvas.tag_bind(settings, "<Button-1>", lambda x: self.settingsMenu(username, Login.titleFont, Login.buttonFont, Login.defaultFont))

        mainMenuStudent.mainloop()

    def parentMainMenuPage(self, username, titleFont, buttonFont, defaultFont):
        mainMenuParent = tk.Tk()
        mainMenuParent.title("Main Menu")

        ## Retrieves the assigned width and height for the main menu page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()

        ## Sets the dimensions of the page and sets it to non-resizable
        mainMenuParent.geometry(str(mainScreenWidth)+'x'+str(mainScreenHeight))
        mainMenuParent.resizable(False, False)

        ## Creates a canvas for all the menu options
        canvas = tk.Canvas(mainMenuParent, height = mainScreenHeight, width = mainScreenWidth, highlightthickness=0, relief='ridge')   
        canvas.pack(fill = 'both', expand = True)

        ## Retrieve first name from database using username
        firstName = viewingFromDatabase.viewFromDatabase(c, False, False, 'firstName', 'username', "'"+username+"'", 'UserDetails')
        ## Create welcome label using first name
        welcomeLabel = tk.Label(canvas, text = "Welcome "+firstName[0][0], bg = 'gray', font = titleFont)
        welcomeLabel.place(relx = 0, rely = 0, relheight = 0.15, relwidth = 1)

        ## Import menu option and settings images and resize them
        menuOptionOneImage = Image.open('ParentMenuOptionOne.png')
        menuOptionOneImage = menuOptionOneImage.resize((1009,325))

        menuOptionTwoImage = Image.open('ParentMenuOptionTwo.png')
        menuOptionTwoImage = menuOptionTwoImage.resize((1009,355))

        settingsImage = Image.open('Settings.png')

        ## Convert them to tkinter images
        tkMenuOptionOneImage = ImageTk.PhotoImage(menuOptionOneImage)
        tkMenuOptionTwoImage = ImageTk.PhotoImage(menuOptionTwoImage)
        tkSettingsImage = ImageTk.PhotoImage(settingsImage)

        ## Add the images to the canvas
        menuOptionOne = canvas.create_image(-3,97, image = tkMenuOptionOneImage, anchor = 'nw')
        menuOptionTwo = canvas.create_image(-5,352, image = tkMenuOptionTwoImage, anchor = 'nw')
        settings = canvas.create_image(935,635, image = tkSettingsImage, anchor = 'nw')

        ## Create labels for the menu options
        optionOneLabel = tk.Label(canvas, text = "View Progress", bg = 'gray', font = titleFont)
        optionOneLabel.place(relx = 0.7, rely = 0.3, relheight = 0.06, relwidth = 0.17)

        optionTwoLabel = tk.Label(canvas, text = "Log Off", bg = 'gray', font = titleFont)
        optionTwoLabel.place(relx = 0.1, rely = 0.75, relheight = 0.06, relwidth = 0.1)

        ## Bind the images and labels to destroy the main meny page and go to the relevant function
        canvas.tag_bind(menuOptionOne, "<Button-1>", lambda x: (mainMenuParent.destroy(), self.viewClasses(username, Login.titleFont, Login.defaultFont, Login.buttonFont)))
        optionOneLabel.bind("<Button-1>", lambda x: (mainMenuParent.destroy(), self.viewClasses(username, Login.titleFont, Login.defaultFont, Login.buttonFont)))

        canvas.tag_bind(menuOptionTwo, "<Button-1>", lambda x: (mainMenuParent.destroy(), self.logOff()))
        optionTwoLabel.bind("<Button-1>", lambda x: (mainMenuParent.destroy(), self.logOff()))
                            
        canvas.tag_bind(settings, "<Button-1>", lambda x: self.settingsMenu(username, Login.titleFont, Login.buttonFont, Login.defaultFont))

        mainMenuParent.mainloop()

    ########################## BUTTONS FOR ADMIN MAIN MENU PAGE ##########################
    
    def leftArrowPressed(self, mainMenuAdmin, canvas, optionLabel, one, two, three, four, five, tkMenuOptionImage, tkFaintMenuOptionImage):
        leftList = []
        rightList = []
        menuOptionsList = [one, two, three, four, five]
        
        for each in menuOptionsList:
            if ((canvas.coords(each))[0]) < 399:
                leftList.append(each)
            elif ((canvas.coords(each))[0]) > 550:
                rightList.append(each)

        if len(leftList) != 0:
            for i in range(1,39):
                if len(leftList) == 2:
                    canvas.move(one, 4, 1)
                    canvas.move(two, 4, 1)
                    canvas.move(three, 4, -1)
                    canvas.move(four, 4, -1)
                    canvas.move(five, 4, -1)
                elif len(leftList) == 1:
                    ##43215
                    canvas.move(four, 4, 1)
                    canvas.move(three, 4, -1)
                    canvas.move(two, 4, -1)
                    canvas.move(one, 4, -1)
                    canvas.move(five, 4, -1)
                elif len(leftList) == 3:
                    ## 15432
                    canvas.move(one, 4, 1)
                    canvas.move(five, 4, 1)
                    canvas.move(four, 4, 1)
                    canvas.move(three, 4, -1)
                    canvas.move(two, 4, -1)
                elif len(leftList) == 4:
                    ## 45123
                    canvas.move(four, 4, 1)
                    canvas.move(five, 4, 1)
                    canvas.move(one, 4, 1)
                    canvas.move(two, 4, 1)
                    canvas.move(three, 4, -1)
                mainMenuAdmin.update()
            if len(leftList) == 2:
                optionLabel.config(text = 'View Quizzes')
            elif len(leftList) == 1:
                optionLabel.config(text = 'Create Quiz')
            elif len(leftList) == 3:
                optionLabel.config(text = 'Play Quiz')
            elif len(leftList) == 4:
                optionLabel.config(text = 'View Classes')
            for j in range(1,13):
                if len(leftList) == 2:
                    canvas.move(one, 0, 1)
                    canvas.move(two, 0, 1)
                    canvas.move(three, 0, -1)
                    canvas.move(four, 0, -1)
                    canvas.move(five, 0, -1)
                elif len(leftList) == 1:
                    canvas.move(four, 0, 1)
                    canvas.move(three, 0, -1)
                    canvas.move(two, 0, -1)
                    canvas.move(one, 0, -1)
                    canvas.move(five, 0, -1)
                elif len(leftList) == 3:
                    canvas.move(one, 0, 1)
                    canvas.move(five, 0, 1)
                    canvas.move(four, 0, 1)
                    canvas.move(three, 0, -1)
                    canvas.move(two, 0, -1)
                elif len(leftList) == 4:
                    canvas.move(four, 0, 1)
                    canvas.move(five, 0, 1)
                    canvas.move(one, 0, 1)
                    canvas.move(two, 0, 1)
                    canvas.move(three, 0, -1)
                mainMenuAdmin.update()
                
            if len(leftList) == 2:
                ## From 12345 to 43215
                canvas.move(three, -152, 50) ## Swap with two
                canvas.move(two, 152, -50) ## Swap with three
                canvas.move(four, -456, 50) ## Swap with one
                canvas.move(one, 456, -50) ## Swap with four
            elif len(leftList) == 1:
                ## From 43215 to 34512
                canvas.move(three, -152, 50) ## Swap with four (to position 1)
                canvas.move(four, 152, -50) ## Swap with three (to position 2)
                canvas.move(five, -304, 100) ## Swap with two (to out of frame)
                canvas.move(two, 304, -100) ## Swap with five (to position 3)
            elif len(leftList) == 3:
                ## Back to 12345 from 15432 
                canvas.move(three, -152, 50) ## Swap with four
                canvas.move(four, 152, -50) ## Swap with three
                canvas.move(five, 456, -50) ## Swap with two
                canvas.move(two, -456, 50) ## Swap with five
            elif len(leftList) == 4:
                ## Back to 15432 from 45123
                canvas.move(one, -304, -100) ## Swap with four
                canvas.move(four, 304, 100) ## Swap with one
                canvas.move(three, -152, 50) ## Swap with two
                canvas.move(two, 152, -50) ## Swap with three

    def rightArrowPressed(self, mainMenuAdmin, canvas, optionLabel, one, two, three, four, five, tkMenuOptionImage, tkFaintMenuOptionImage):
        leftList = []
        rightList = []
        menuOptionsList = [one, two, three, four, five]
        
        for each in menuOptionsList:
            if ((canvas.coords(each))[0]) < 399:
                leftList.append(each)
            elif ((canvas.coords(each))[0]) > 550:
                rightList.append(each)

        if len(rightList) != 0:
            for i in range(1,39):
                if len(rightList) == 2:
                    canvas.move(one, -4, -1)
                    canvas.move(two, -4, -1)
                    canvas.move(three, -4, -1)
                    canvas.move(four, -4, 1)
                    canvas.move(five, -4, 1)
                elif len(rightList) == 1:
                    ## 15432
                    canvas.move(one, -4, -1)
                    canvas.move(five, -4, -1)
                    canvas.move(four, -4, -1)
                    canvas.move(three, -4, -1)
                    canvas.move(two, -4, 1)
                elif len(rightList) == 3:
                    ## 43215
                    canvas.move(four, -4, -1)
                    canvas.move(three, -4, -1)
                    canvas.move(two, -4, 1)
                    canvas.move(one, -4, 1)
                    canvas.move(five, -4, 1)
                elif len(rightList) == 4:
                    ## 34512
                    canvas.move(three, -4, -1)
                    canvas.move(four, -4, 1)
                    canvas.move(five, -4, 1)
                    canvas.move(one, -4, 1)
                    canvas.move(two, -4, 1)
                mainMenuAdmin.update()
            if len(rightList) == 2:
                optionLabel.config(text = 'View Classes')
            elif len(rightList) == 1:
                optionLabel.config(text = 'Log off')
            elif len(rightList) == 3:
                optionLabel.config(text = 'Play Quiz')
            elif len(rightList) == 4:
                optionLabel.config(text = 'View Quizzes')
            for j in range(1,13):
                if len(rightList) == 2:
                    canvas.move(one, 0, -1)
                    canvas.move(two, 0, -1)
                    canvas.move(three, 0, -1)
                    canvas.move(four, 0, 1)
                    canvas.move(five, 0, 1)
                elif len(rightList) == 1:
                    canvas.move(one, 0, -1)
                    canvas.move(five, 0, -1)
                    canvas.move(four, 0, -1)
                    canvas.move(three, 0, -1)
                    canvas.move(two, 0, 1)
                elif len(rightList) == 3:
                    canvas.move(four, 0, -1)
                    canvas.move(three, 0, -1)
                    canvas.move(two, 0, 1)
                    canvas.move(one, 0, 1)
                    canvas.move(five, 0, 1)
                elif len(rightList) == 4:
                    canvas.move(three, 0, -1)
                    canvas.move(four, 0, 1)
                    canvas.move(five, 0, 1)
                    canvas.move(one, 0, 1)
                    canvas.move(two, 0, 1)
                mainMenuAdmin.update()

            if len(rightList) == 2:
                ## From 12345 to 15432
                canvas.move(three, 152, 50) ## Swap with four
                canvas.move(four, -152, -50) ## Swap with three
                canvas.move(five, -456, -50) ## Swap with two
                canvas.move(two, 456, 50) ## Swap with five
                ## From 15432 to 45123
            elif len(rightList) == 1:
                canvas.move(three, 152, 50) ## Swap with two (to position 5)
                canvas.move(two, -152, -50) ## Swap with three (to position 4)
                canvas.move(four, -304, -100) ## Swap with one (to out of frame)
                canvas.move(one, 304, 100) ## Swap with four (to position 3)
            elif len(rightList) == 3:
                ## Back to 12345 from 43215
                canvas.move(three, 152, 50) ## Swap with two
                canvas.move(two, -152, -50) ## Swap with three
                canvas.move(four, 456, 50) ## Swap with one
                canvas.move(one, -456, -50) ## Swap with four
            elif len(rightList) == 4:
                ## Back to 43215 from 34512
                canvas.move(three, 152, 50) ## Swap with four
                canvas.move(four, -152, -50) ## Swap with three
                canvas.move(two, -304, 100) ## Swap with five
                canvas.move(five, 304, -100) ## Swap with two

    def selectButtonPressed(self, previousPage, username, menuOption):
        if menuOption.cget('text') == 'Play Quiz':
            ## Destroy previous page
            previousPage.destroy()
            ## Initiate playQuiz function
            self.playQuiz(username, Login.titleFont, Login.defaultFont, Login.buttonFont)
        elif menuOption.cget('text') == 'View Quizzes':
            ## Destroy previous page
            previousPage.destroy()
            ## Initiate viewQuizzes function
            self.viewQuizzes(username, Login.titleFont, Login.defaultFont, Login.buttonFont)
        elif menuOption.cget('text') == 'Create Quiz':
            ## Destroy previous page
            previousPage.destroy()
            ## Initiate createQuiz function
            self.createQuiz(username, Login.titleFont, Login.defaultFont, Login.buttonFont)
        elif menuOption.cget('text') == 'View Classes':
            ## Destroy previous page
            previousPage.destroy()
            ## Initiate viewClasses function
            self.viewClasses(username, Login.titleFont, Login.defaultFont, Login.buttonFont)
        elif menuOption.cget('text') == 'Log off':
            ## Destroy previous page
            previousPage.destroy()
            ## Initiate logOff function
            self.logOff()

    def settingsMenu(self, username, titleFont, buttonFont, defaultFont):
        settingsPage = tk.Tk()
        settingsPage.title("Settings")

        ## Retrieves the assigned width and height for the settings page
        mainScreenWidth = settings.getScreenWidth()
        mainScreenHeight = settings.getScreenHeight()

        settingsPage.resizable(False, False)
        
        canvas = tk.Canvas(settingsPage, height = mainScreenHeight, width = mainScreenWidth)   
        canvas.pack()

        mainframe = tk.Frame(settingsPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)
        
        welcomeLabel = tk.Label(mainframe, text = "Settings", bg = 'gray', font = titleFont)
        welcomeLabel.place(relx = 0, rely = 0, relheight = 0.15, relwidth = 1)

        userType = viewingFromDatabase.viewFromDatabase(c, False, False, 'accountType', 'username', "'"+username+"'", 'UserDetails')
        if userType[0][0] == 'Admin':
            reviewUsersFrame = tk.Frame(mainframe, bg = 'gray')
            reviewUsersFrame.place(relx = 0.3, rely = 0.25, relheight = 0.15, relwidth = 0.4)

            reviewUsersButton = tk.Button(reviewUsersFrame, text = "Review Users", bg = '#E5E7E9', font = buttonFont, command = lambda: self.reviewUsers(settingsPage, Login.titleFont, Login.buttonFont, Login.defaultFont))
            reviewUsersButton.place(relx = 0.03, rely = 0.1, relheight = 0.8, relwidth = 0.94)

            cmdPosition = 0.45
            maPosition = 0.65

        else:
            cmdPosition = 0.25
            maPosition = 0.45

        changeMenuDimensionsFrame = tk.Frame(mainframe, bg = 'gray')
        changeMenuDimensionsFrame.place(relx = 0.3, rely = cmdPosition, relheight = 0.15, relwidth = 0.4)

        changeMenuDimensionsButton = tk.Button(changeMenuDimensionsFrame, text = "Change Main Menu Dimensions", bg = '#E5E7E9', font = buttonFont, command = self.changeMenuDimensions)
        changeMenuDimensionsButton.place(relx = 0.03, rely = 0.1, relheight = 0.8, relwidth = 0.94)

        myAccountFrame = tk.Frame(mainframe, bg = 'gray')
        myAccountFrame.place(relx = 0.3, rely = maPosition, relheight = 0.15, relwidth = 0.4)

        myAccountButton = tk.Button(myAccountFrame, text = "My Account", bg = '#E5E7E9', font = buttonFont, command = self.myAccount)
        myAccountButton.place(relx = 0.03, rely = 0.1, relheight = 0.8, relwidth = 0.94)

    ######################################## END OF ###########################################

    ########################## BUTTONS FOR SETTINGS PAGE ##########################
        
    def reviewUsers(self, page, titleFont, buttonFont, defaultFont):
        page.destroy()
        reviewUsersPage = tk.Tk()
        reviewUsersPage.title("Review Users")

        ## Retrieves the assigned width and height for the settings page
        mainScreenWidth = reviewUser.getScreenWidth()
        mainScreenHeight = reviewUser.getScreenHeight()
        
        canvas = tk.Canvas(reviewUsersPage, height = mainScreenHeight, width = mainScreenWidth)   
        canvas.pack()

        mainframe = tk.Frame(reviewUsersPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        selectUserLabel = tk.Label(mainframe, text = "Please select a user to review:", bg = 'gray', font = defaultFont)
        selectUserLabel.place(relx = 0.05, rely = 0.08, relheight = 0.08, relwidth = 0.3)

        tableFrame = tk.Frame(mainframe, bg = '#80c1ff')
        tableFrame.place(relx = 0.05, rely = 0.2, relheight = 0.5, relwidth = 0.9)

        returnButton = tk.Button(mainframe, text = "Return", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = reviewUsersPage.destroy)
        returnButton.place(relx = 0.77, rely = 0.87, relheight = 0.1, relwidth = 0.2)
   
        ## Fetch the relevant data from the database by performing an inner join between the UserDetails and UserReview tables
        newTable = innerJoinTables.innerJoin(c, 'UserDetails.accountType, UserDetails.username, UserDetails.firstName, UserDetails.lastName, UserDetails.reviewID, UserReview.reviewType', 'UserDetails', 'UserReview', 'UserDetails.reviewID', 'UserReview.reviewID')
        data = []
        for each in newTable:
            if each[4] > 1:
                data.append(each)
        ## If data list is not empty...
        if len(data) > 0:
            ## Create table with data from new table
            cells = self.createTable(data, tableFrame, Login.defaultFont)
        ## If empty...
        else:
            ## Change label text
            selectUserLabel.config(text = 'There are no users under review.')

        ## Retrieve children from tableFrame and assign to list
        wlist = tableFrame.winfo_children()
        ## For each child (i.e. each cell in table)
        for each in range(len(wlist)):
            ## Find row number by integer division on current iteration by 6 (number of columns)
            ## Find username associated to selected row in cells dictionary
            username = cells[(each // 6, 1)]
            ## Bind button event which initiates reviewUser function with username as parameter
            wlist[each].bind("<Button-1>", lambda x, username = username: self.reviewUser(username, reviewUsersPage, Login.titleFont, Login.buttonFont, Login.defaultFont))

    def createTable(self, data, frame, defaultFont):
        # Find total number of rows and columns in data list 
        totalRows = len(data) 
        totalColumns = len(data[0])
        ## Create dictionary for each cell and its corresponding text
        cells = {}

        ## For each row...
        for i in range(totalRows):
            ## For each column...
            for j in range(totalColumns):
                ## Create label with relevant text and place it in a grid format
                field = tk.Label(frame, width = 15, font = defaultFont, borderwidth = 1, relief = "solid")
                field.grid(row = i, column = j)
                field.config(text = data[i][j])
                ## Add cell with text to dictionary
                cells[(i,j)] = field.cget('text')

        return cells
                       
    def reviewUser(self, username, page, titleFont, buttonFont, defaultFont):
        ## Destroy previous page
        page.destroy()
        reviewUserPage = tk.Tk()
        reviewUserPage.title("Review User")

        ## Retrieves the assigned width and height for the settings page
        mainScreenWidth = reviewUser.getScreenWidth()
        mainScreenHeight = reviewUser.getScreenHeight()

        ## Create and place canvas
        canvas = tk.Canvas(reviewUserPage, height = mainScreenHeight, width = mainScreenWidth)   
        canvas.pack()

        ## Create and place mainframe
        mainframe = tk.Frame(reviewUserPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        selectUserLabel = tk.Label(mainframe, text = "Please select a user to review:", bg = 'gray', font = defaultFont)
        selectUserLabel.place(relx = 0.05, rely = 0.08, relheight = 0.08, relwidth = 0.3)

        reviewUserPage.mainloop()
                
    def changeMenuDimensions(self):
        print('Change Menu Dimensions')

    def myAccount(self):
        print('My Account')

    ######################################## END OF ###########################################

    ########################## FUNCTIONS FOR MAIN MENU PAGES ##########################

    def playQuiz(self, username, titleFont, defaultFont, buttonFont):
        ## Retrieves the assigned height, width and fonts for the main create question page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()
        
        playQuizPage = tk.Tk()
        playQuizPage.title("Play Quiz")

        canvas = tk.Canvas(playQuizPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        background = tk.Frame(playQuizPage, bg = 'black')
        background.place(rely = 0.1, relheight = 0.9, relwidth = 1)

        ## Create a frame for listbox of all quizzes on the left
        quizFrame = tk.Frame(playQuizPage, bg = '#73ade5')
        quizFrame.place(rely = 0.1, relheight = 0.9, relwidth = 0.4)

        ## Create a frame for details of all quizzes on the right and option to play
        mainframe = tk.Frame(playQuizPage, bg = '#80c1ff')
        mainframe.place(relx = 0.405, rely = 0.1, relheight = 0.9, relwidth = 0.595)

        welcomeLabel = tk.Label(canvas, text = "Play Quiz", bg = 'gray', font = titleFont)
        welcomeLabel.place(relheight = 0.1, relwidth = 1)

        returnButton = tk.Button(canvas, text = "Go\nBack", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.returnToMainMenu(playQuizPage, username))
        returnButton.place(relheight = 0.1, relwidth = 0.1)
        
        ## Create listbox for all quizzes
        quizListbox = tk.Listbox(quizFrame, font = defaultFont, exportselection = False)
        listboxHeight = 0
        buttonPos = 0.1
        quizzes = viewingFromDatabase.viewFromDatabase(c, True, True, None, None, None, 'Quiz')
        for i in range(len(quizzes)):
            quizListbox.insert('end', quizzes[i][1] + ' ' + quizzes[i][2])
            if buttonPos < 0.8:
                listboxHeight += 0.1
                buttonPos += 0.1
        quizListbox.place(relx = 0.1, rely = 0.05, relheight = listboxHeight, relwidth = 0.8)
        ## Bind list box to displayQuizDetails function when a quiz is selected
        quizListbox.bind('<<ListboxSelect>>', lambda x: self.displayQuizDetails(username, playQuizPage, quizListbox, quizListbox.get(quizListbox.curselection()), mainframe, playButton, quizSubjectFrame, quizSubjectLabel, quizLevelFrame, quizLevelLabel, noOfQuestionsFrame, noOfQuestionsLabel, noOfQuestionsEntry, Login.titleFont, Login.defaultFont, Login.buttonFont))

        ## Create frame and label for a quiz's subject
        quizSubjectFrame = tk.Frame(mainframe)
        quizSubjectLabel = tk.Label(quizSubjectFrame, text = 'Please select a quiz to play', bg = 'gray')
        quizSubjectFrame.place(relx = 0.15, rely = 0.12, relheight = 0.15, relwidth = 0.7)
        quizSubjectLabel.place(relheight = 1, relwidth = 1)

        ## Create frame and label for a quiz's level
        quizLevelFrame = tk.Frame(mainframe)
        quizLevelLabel = tk.Label(quizLevelFrame)

        ## Create frame and label for the number of questions in a quiz
        noOfQuestionsFrame = tk.Frame(mainframe)
        noOfQuestionsLabel = tk.Label(noOfQuestionsFrame)
        noOfQuestionsEntry = tk.Entry(noOfQuestionsFrame, validate = 'key', validatecommand = (noOfQuestionsFrame.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))

        playButton = tk.Button(mainframe, text = "Play", highlightbackground = '#424949', fg = 'blue', font = defaultFont)
        
        playQuizPage.mainloop()

    def displayQuizDetails(self, username, playQuizPage, quizListbox, selectedQuiz, mainframe, playButton, quizSubjectFrame, quizSubjectLabel, quizLevelFrame, quizLevelLabel, noOfQuestionsFrame, noOfQuestionsLabel, noOfQuestionsEntry, titleFont, defaultFont, buttonFont):
        ## Hide noOfQuestionsEntry in case of changing quizzes
        noOfQuestionsEntry.place(relheight = 0, relwidth = 0)
        
        ## Retrieve all details from database for selected quiz
        index = quizListbox.get(0, "end").index(selectedQuiz)
        quizDetails = viewingFromDatabase.viewFromDatabase(c, True, True, None, None, None, "Quiz LIMIT " + str(index) + ", 1")
        
        quizSubjectFrame.place(relx = 0.3, rely = 0.12, relheight = 0.15, relwidth = 0.4)
        quizSubjectLabel.config(text = quizDetails[0][1], bg = 'gray', font = titleFont)
        quizSubjectLabel.place(relheight = 1, relwidth = 1)

        quizLevelFrame.place(relx = 0.3, rely = 0.32, relheight = 0.15, relwidth = 0.4)
        quizLevelLabel.config(text = quizDetails[0][2], bg = 'gray', font = titleFont)
        quizLevelLabel.place(relheight = 1, relwidth = 1)

        ## If random quiz with no set questions
        if quizDetails[0][3] == 0:
            noOfQuestionsFrame.place(relx = 0.2, rely = 0.52, relheight = 0.15, relwidth = 0.6)
            noOfQuestionsLabel.config(text = 'Questions:', bg = 'gray', font = titleFont)
            noOfQuestionsLabel.place(relheight = 1, relwidth = 0.7)
            noOfQuestionsEntry.place(relx = 0.8, relheight = 1, relwidth = 0.3)
        ## If quiz with set questions
        else:
            noOfQuestionsFrame.place(relx = 0.3, rely = 0.52, relheight = 0.15, relwidth = 0.4)
            noOfQuestionsLabel.config(text = str(quizDetails[0][3]) + ' Questions', bg = 'gray', font = titleFont)
            noOfQuestionsLabel.place(relheight = 1, relwidth = 1)

        playButton.config(command = lambda: self.playSelectedQuiz(playQuizPage, quizDetails, username, noOfQuestionsEntry.get()))
        playButton.place(relx = 0.4, rely = 0.8, relheight = 0.1, relwidth = 0.2)

    def playSelectedQuiz(self, previousPage, quizDetails, username, noOfQuestionsEntry):
        ## Destroy previous page
        previousPage.destroy()

        ## If random quiz with no set questions
        if quizDetails[0][3] == 0:
            questions = []
            ## If quiz ID of selected quiz is 21
            if quizDetails[0][0] == 21:
                ## For each in range chosen number of questions
                for each in range(int(noOfQuestionsEntry)):
                    ## Create two random variables between 1 and 12, and a variable with a random question type
                    numberOne = random.randint(1,12)
                    numberTwo = random.randint(1,12)
                    questionType = random.choice(['Multiple Choice','Answer Input'])
                    if questionType == 'Multiple Choice':
                        ## Add as a question to questions list
                        questions.append((None, 21, questionType, str(numberOne) + ' x ' + str(numberTwo), 4, str(numberOne * numberTwo), str(random.randint(1, numberOne * numberTwo * 2)), str(random.randint(1, numberOne * numberTwo * 2)), str(random.randint(1, numberOne * numberTwo * 2)), 30, None, random.randint(1,3)))
                    elif questionType == 'Answer Input':
                        questions.append((None, 21, questionType, str(numberOne) + ' x ' + str(numberTwo), 1, str(numberOne * numberTwo), None, None, None, 5, None, random.randint(1,3)))
        ## If quiz with set questions
        else:
            ## Retrieve all questions from database for selected quiz
            questions = viewingFromDatabase.viewFromDatabase(c, True, False, None, 'quizID', str(quizDetails[0][0]), 'Question')
            ## If quiz ID of selected quiz is 22
            if quizDetails[0][0] == 22:
                ## Create list for all 'k' values
                kValuesList = []
                ## Create counter for each question
                question = 0
                ## For each question
                for each in range(len(questions)):
                    ## Append empty list to kValuesList
                    kValuesList.append([])
                    ## Convert tuple to list so can be edited
                    questions[each] = list(questions[each])
                    ## Replace all 'k' values with random integers within given range from database
                    counter = 1
                    for each2 in range(0,3):
                        if questions[each][each2 + 6] != None:
                            randomRange = (questions[each][each2 + 6]).split()
                            randomValue = str(random.randint(int(randomRange[0]), int(randomRange[2])))
                            questions[each][3] = questions[each][3].replace('k_'+str(counter), randomValue)
                            kValuesList[question].append(randomValue)
                            counter += 1
                    
                    ## For number of random k values
                    for each3 in range(len(kValuesList[question])):
                        ## If one value
                        if len(kValuesList[question]) > 0:
                            ## Replace a with random value
                            questions[each][5] = questions[each][5].replace('a', kValuesList[question][0])
                        ## If two values
                        if len(kValuesList[question]) > 1:
                            ## Replace b with random value
                            questions[each][5] = questions[each][5].replace('b', kValuesList[question][1])
                        ## If three values
                        if len(kValuesList[question]) > 2:
                            ## Replace c with random value
                            questions[each][5] = questions[each][5].replace('c', kValuesList[question][2])

                    ## Split equation string and change integer data type for each number
                    questions[each][5] = questions[each][5].split()
                    equationList = []
                    for each4 in questions[each][5]:
                        if each4.isdigit() == True:
                            each4 = int(each4)
                        equationList.append(each4)

                    ## Place all contents of any brackets in new list
                    bracketList = []
                    bracketIndexList = []
                    for each5 in range(len(equationList)):
                        if equationList[each5] == '(':
                            counter = 1
                            while equationList[each5+counter] != ')':
                                bracketList.append(equationList[each5+counter])
                                bracketIndexList.append(each5+counter)
                                counter+=1

                    ## Reverse list to avoid index issues
                    bracketIndexList.reverse()
                    ## If not empty
                    if len(bracketIndexList) > 0:
                        ## For every index including and within brackets
                        for each6 in bracketIndexList:
                            ## Remove value in list in reverse index order
                            equationList.pop(each6)

                    ## Create dictionary for string operator values
                    operators = {
                                '+' : operator.add,
                                '-' : operator.sub,
                                '*' : operator.mul,
                                '/' : operator.truediv,
                                'π' : math.pi,
                                '√' : math.sqrt,
                                'sin\u2061' : math.sin}

                    ## If bracketList not empty, calculate contents
                    if len(bracketList) > 0:
                        counter = 0
                        ## Work out any multiplication or division first
                        while '*' in bracketList or '/' in bracketList:
                            if bracketList[counter] == '*' or bracketList[counter] == '/':
                                ## Calculate operator
                                self.calculateEquation(operators, bracketList, counter)
                                ## Reset counter since index changed
                                counter = 0
                            counter += 1
                        counter = 0
                        ## Work out any other operator
                        while len(bracketList) != 1:
                            if bracketList[counter] in operators:
                                ## Calculate operator
                                self.calculateEquation(operators, bracketList, counter)
                                ## Reset counter since index changed
                                counter = 0
                            counter += 1

                        ## Remove brackets from equationList
                        for each7 in range(len(equationList)-1):
                            if equationList[each7] == '(':
                                ## Remove ')' value from list
                                equationList.pop(each7+1)
                                ## Replace '(' value with result in bracket list
                                equationList[each7] = bracketList[0]
                            
                    for each8 in range(len(equationList)-1):
                        ## Change sin string value to operator
                        if equationList[each8] == 'sin\u2061':
                            ## Calculate sin values and replace in list
                            equationList[each8] = (operators['sin\u2061'])(equationList[each8+1]*math.pi/180)
                            equationList.pop(each8+1)
                            
                        ## Change pi string value to operator
                        elif equationList[each8] == 'π':
                            equationList[each8] = operators['π']
                            
                        ## Change root string value to operator
                        elif equationList[each8] == '√':
                            ## Calculate root values and replace in list
                            equationList[each8] = (operators['√'])(equationList[each8+1])
                            equationList.pop(each8+1)
                                
                    ## Calculate and change answers using equation in answerOne field:
                    counter = 0
                    ## Work out any multiplication or division first within equationList
                    while '*' in equationList or '/' in equationList:
                        if equationList[counter] == '*' or equationList[counter] == '/':
                            ## Calculate operator
                            self.calculateEquation(operators, equationList, counter)
                            ## Reset counter since index changed
                            counter = 0
                        counter += 1
                    counter = 0
                    ## Work out any other operator within equationList
                    while len(equationList) != 1:
                        if equationList[counter] in operators:
                            ## Calculate operator
                            self.calculateEquation(operators, equationList, counter)
                            ## Reset counter since index changed
                            counter = 0
                        counter += 1

                    ## If question 3
                    if question == 2:
                        ## Determine number of roots from discriminant and assign answer
                        if equationList[0] < 0:
                            questions[each][5] = '0'
                        elif equationList[0] == 0:
                            questions[each][5] = '1'
                        elif equationList[0] > 0:
                            questions[each][5] = '2'
                        ## Empty all other answer options
                        questions[each][6] = None
                        questions[each][7] = None
                        questions[each][8] = None
                    else:
                        ## Assign answers for the question
                        questions[each][5] = (round(equationList[0]))
                        questions[each][6] = str(random.randint(questions[each][5]//2, questions[each][5]*2))
                        questions[each][7] = str(random.randint(questions[each][5]//2, questions[each][5]*2))
                        questions[each][8] = str(random.randint(questions[each][5]//2, questions[each][5]*2))
                        questions[each][5] = str(questions[each][5])
                    question += 1

        ## Retrieves the assigned height, width and fonts for the play selected quiz page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()
        
        playSelectedQuizPage = tk.Tk()
        playSelectedQuizPage.title("Play Quiz")

        canvas = tk.Canvas(playSelectedQuizPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(playSelectedQuizPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)
        
        backgroundImageLabel = tk.Label(mainframe)
        questionFrame = tk.Frame(mainframe)
        questionLabel = tk.Label(questionFrame)
        answerOneFrame = tk.Frame(mainframe)
        answerOneEntry = tk.Entry(answerOneFrame)
        answerOneLabel = tk.Label(answerOneFrame)
        answerTwoFrame = tk.Frame(mainframe)
        answerTwoLabel = tk.Label(answerTwoFrame)
        answerThreeFrame = tk.Frame(mainframe)
        answerThreeLabel = tk.Label(answerThreeFrame)
        answerFourFrame = tk.Frame(mainframe)
        answerFourLabel = tk.Label(answerFourFrame)
        timeLimitFrame = tk.Frame(mainframe)
        timeLimitLabel = tk.Label(timeLimitFrame)

        ## Establish userID for given username
        userID = viewingFromDatabase.viewFromDatabase(c, False, False, 'userID', 'username', "'"+username+"'", 'UserDetails')
        userID = userID[0][0]

        points = 0
        multiplier = 1
        correct = False
        
        ## For each question in quiz
        for i in range(len(questions)):
            ## Show playSelectedQuizPage
            playSelectedQuizPage.deiconify()
            ## Retrieve time limit from questions list
            timeLimit = questions[i][9]
            ## Establish current time
            currentTime = datetime.now()
            formattedDate = currentTime.strftime('%Y-%m-%d %H:%M:%S')
            ## Create record to be added to database
            record = [None, userID, quizDetails[0][0], questions[i][0], None, formattedDate]
            ## Add incomplete record to Progress table in database for the question
            addingToDatabase.addToDatabase(conn, c, record, 'Progress')
            ## Determine streak and multiplier
            if correct == True:
                multiplier += 0.1
            else:
                multiplier = 1
            ## Go to display question function with relevant parameters
            answerInput, correctAnswer, correct = self.displayQuestion('Play Quiz', answerOneEntry, playSelectedQuizPage, None, questions, questionLabel, i, questionFrame, answerOneFrame, answerOneLabel, answerTwoFrame, answerTwoLabel, answerThreeFrame, answerThreeLabel, answerFourFrame, answerFourLabel, backgroundImageLabel, timeLimitFrame, timeLimitLabel, mainframe, Login.titleFont, Login.defaultFont, Login.buttonFont)
            ## Hide playSelectedQuizPage
            playSelectedQuizPage.withdraw()
            ## Initiate finishQuestion and assign returned value to points variable
            points = self.finishQuestion(answerInput, correctAnswer, correct, multiplier, points, i, len(questions), Login.titleFont, Login.buttonFont, Login.defaultFont)
        self.finishQuiz(username, len(questions), playSelectedQuizPage, Login.titleFont, Login.buttonFont, Login.defaultFont)
        
        playSelectedQuizPage.mainloop()

    def calculateEquation(self, operators, equationlist, counter):
        ## Use operator on following value and preceding value and replace following value
        equationlist[counter+1] = (operators[equationlist[counter]](equationlist[counter-1],equationlist[counter+1]))
        ## Remove preceding values
        equationlist.pop(counter-1)
        equationlist.pop(counter-1)        

    def finishQuestion(self, answerInput, correctAnswer, correct, multiplier, points, i, noOfQuestions, titleFont, buttonFont, defaultFont):
        ## Retrieves the assigned height, width and fonts for the finish question page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()

        ## Create page and title
        finishQuestionPage = tk.Tk()
        finishQuestionPage.title("Play Quiz")

        ## Create canvas for page dimensions
        canvas = tk.Canvas(finishQuestionPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        ## If answered correctly, assign green background and text to 'Correct!'
        if correct == True:
            bgColour = '#9FE2BF'
            correctText = 'Correct!'
            points += (1000*multiplier)
        ## else, assign red background and text to 'Incorrect!'
        else:
            bgColour = '#F08080'
            correctText = 'Incorrect!'
        ## Create main frame with correct background colour
        mainframe = tk.Frame(finishQuestionPage, bg = bgColour)
        mainframe.place(relheight = 1, relwidth = 1)

        ## Create label to show if correct or incorrect
        correctLabel = tk.Label(mainframe, text = correctText, bg = 'gray', font = titleFont)
        correctLabel.place(relheight = 0.15, relwidth = 1)

        ## If answered incorrectly...
        if correct == False:
            ## Create label to show user's input
            answerInputLabel = tk.Label(mainframe, text = 'You entered ' + answerInput, bg = 'gray', font = titleFont)
            answerInputLabel.place(relx = 0.3, rely = 0.25, relheight = 0.12, relwidth = 0.4)

            ## Create label to show correct answer
            correctAnswerLabel = tk.Label(mainframe, text = 'The correct answer is ' + correctAnswer, bg = 'gray', font = titleFont)
            correctAnswerLabel.place(relx = 0.3, rely = 0.42, relheight = 0.12, relwidth = 0.4)

        ## Create label to show how many points the user is on
        pointsLabel = tk.Label(mainframe, text = 'Points: ' + str(points), bg = 'gray', font = titleFont)
        pointsLabel.place(relx = 0.3, rely = 0.59, relheight = 0.12, relwidth = 0.4)

        ## Set time limit to 10 seconds
        timeLimit = 10
        ## Create label to show how long until the next question begins
        nextQuestionLabel = tk.Button(mainframe, text = 'Next Question in: ' + str(timeLimit), highlightbackground = '#424949', font = defaultFont)
        nextQuestionLabel.place(relx = 0.4, rely = 0.77, relheight = 0.12, relwidth = 0.2)

        ## Assign label text for when not the last question
        labelText = 'Next Question in: '
        ## If last iteration...
        if i == noOfQuestions-1:
            ## Assign label text for when the last question
            labelText = 'Finish in: '
        ## While time limit is greater than 0 (i.e. there is time remaining)
        while timeLimit > 0:
            timeLimit -= 1
            time.sleep(1)
            nextQuestionLabel.config(text = labelText + str(timeLimit))
            finishQuestionPage.update()

        ## Destroy page at the end of countdown
        finishQuestionPage.destroy()
        
        return points
        finishQuestionPage.mainloop()

    def finishQuiz(self, username, noOfQuestions, playSelectedQuizPage, titleFont, buttonFont, defaultFont):
        ## Retrieve 'correct' field from progress records from database for the quiz played
        progress = viewingFromDatabase.viewFromDatabase(c, False, True, 'correct', None, None, 'Progress ORDER BY progressID DESC LIMIT ' + str(noOfQuestions))
        correctAnswers = 0
        ## For each correct answer...add one to counter
        for each in progress:
            if each[0] == 'True':
                correctAnswers += 1
        
        ## Retrieves the assigned height, width and fonts for the finish quiz page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()

        ## Create page and title
        finishQuizPage = tk.Tk()
        finishQuizPage.title("Play Quiz")

        ## Create canvas for page dimensions
        canvas = tk.Canvas(finishQuizPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        ## Create main frame 
        mainframe = tk.Frame(finishQuizPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        ## Create label displaying 'Results'
        resultsLabel = tk.Label(mainframe, text = 'Results', bg = 'gray', font = titleFont)
        resultsLabel.place(relheight = 0.15, relwidth = 1)

        ## Create label to show user's result
        userResultsLabel = tk.Label(mainframe, text = 'You got ' + str(correctAnswers) + ' / ' + str(noOfQuestions), bg = 'gray', font = titleFont)
        userResultsLabel.place(relx = 0.3, rely = 0.3, relheight = 0.12, relwidth = 0.4)

        ## Create button to return to main menu
        returnButton = tk.Button(mainframe, text = 'Return to Main Menu', highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: (playSelectedQuizPage.destroy(), self.returnToMainMenu(finishQuizPage, username)))
        returnButton.place(relx = 0.375, rely = 0.7, relheight = 0.1, relwidth = 0.25)

        finishQuizPage.mainloop()

    def viewQuizzes(self, username, titleFont, defaultFont, buttonFont):
        ## Retrieves the assigned height, width and fonts for the main create question page
        mainScreenWidth = viewQuiz.getScreenWidth()
        mainScreenHeight = viewQuiz.getScreenHeight()
        
        viewQuizzesPage = tk.Tk()
        viewQuizzesPage.title("View Quizzes")

        canvas = tk.Canvas(viewQuizzesPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(viewQuizzesPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        welcomeLabel = tk.Label(mainframe, text = "View Quizzes", bg = 'gray', font = titleFont)
        welcomeLabel.place(relheight = 0.1, relwidth = 1)

        returnButton = tk.Button(mainframe, text = "Go\nBack", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.returnToMainMenu(viewQuizzesPage, username))
        returnButton.place(relheight = 0.1, relwidth = 0.1)

        background = tk.Frame(viewQuizzesPage, bg = 'black')
        background.place(rely = 0.1, relheight = 0.9, relwidth = 1)

        quizFrame = tk.Frame(viewQuizzesPage, bg = '#73ade5')
        quizFrame.place(rely = 0.1, relheight = 0.9, relwidth = 0.2)

        ## Create listbox for all quizzes
        quizListbox = tk.Listbox(quizFrame, font = defaultFont, exportselection = False)
        listboxHeight = 0
        buttonPos = 0.1
        quizzes = viewingFromDatabase.viewFromDatabase(c, True, True, None, None, None, 'Quiz')
        for i in range(len(quizzes)):
            quizListbox.insert('end', 'Quiz ' + str(i+1))
            if buttonPos < 0.8:
                listboxHeight += 0.1
                buttonPos += 0.1
        quizListbox.place(relx = 0.1, rely = 0.05, relheight = listboxHeight, relwidth = 0.8)
        quizListbox.bind('<<ListboxSelect>>', lambda x: self.displayQuestions(quizListbox, questionListbox, questionLabel, quizListbox.get(quizListbox.curselection()), questionFrame, answerOneFrame, answerOneLabel, answerTwoFrame, answerTwoLabel, answerThreeFrame, answerThreeLabel, answerFourFrame, answerFourLabel, backgroundImageLabel, timeLimitFrame, timeLimitLabel, rightFrame, Login.titleFont, Login.defaultFont, Login.buttonFont))

        questionsFrame = tk.Frame(viewQuizzesPage, bg = '#73ade5')
        questionsFrame.place(relx = 0.205, rely = 0.1, relheight = 0.9, relwidth = 0.2)

        questionListbox = tk.Listbox(questionsFrame, font = defaultFont, exportselection = False)

        rightFrame = tk.Frame(viewQuizzesPage, bg = '#80c1ff')
        rightFrame.place(relx = 0.410, rely = 0.1, relheight = 0.9, relwidth = 0.590)

        backgroundImageLabel = tk.Label(rightFrame)
        questionFrame = tk.Frame(rightFrame)
        questionLabel = tk.Label(questionFrame)
        answerOneFrame = tk.Frame(rightFrame)
        answerOneLabel = tk.Label(answerOneFrame)
        answerTwoFrame = tk.Frame(rightFrame)
        answerTwoLabel = tk.Label(answerTwoFrame)
        answerThreeFrame = tk.Frame(rightFrame)
        answerThreeLabel = tk.Label(answerThreeFrame)
        answerFourFrame = tk.Frame(rightFrame)
        answerFourLabel = tk.Label(answerFourFrame)
        timeLimitFrame = tk.Frame(rightFrame)
        timeLimitLabel = tk.Label(timeLimitFrame)

        viewQuizzesPage.mainloop()

    def displayQuestions(self, quizListbox, questionListbox, questionLabel, selectedQuiz, questionFrame, answerOneFrame, answerOneLabel, answerTwoFrame, answerTwoLabel, answerThreeFrame, answerThreeLabel, answerFourFrame, answerFourLabel, backgroundImageLabel, timeLimitFrame, timeLimitLabel, rightFrame, titleFont, defaultFont, buttonFont):
        ## Retrieve quiz ID from database for selected quiz
        index = quizListbox.get(0, "end").index(selectedQuiz)
        quizID = viewingFromDatabase.viewFromDatabase(c, False, True, "quizID", None, None, "Quiz LIMIT " + str(index) + ", 1")
        quizID = quizID[0][0] ## Isolate it from list and tuple
        ## Retrieve all questions from database for selected quiz
        questions = viewingFromDatabase.viewFromDatabase(c, True, False, None, 'quizID', str(quizID), 'Question')

        ## Clear the question list box (to allow for changing questions)
        questionListbox.delete(0,'end')
        listboxHeight = 0
        ## Add each question from questions list to questions list box
        for each in questions:
            questionListbox.insert('end', each[3])
            if listboxHeight < 0.8:
                listboxHeight += 0.1
        questionListbox.place(relx = 0.1, rely = 0.05, relheight = listboxHeight, relwidth = 0.8)
        ## Bind any selection within listbox to event
        questionListbox.bind('<<ListboxSelect>>', lambda x: self.displayQuestion('View Quizzes', None, None, questionListbox, questions, questionLabel, questionListbox.get(questionListbox.curselection()), questionFrame, answerOneFrame, answerOneLabel, answerTwoFrame, answerTwoLabel, answerThreeFrame, answerThreeLabel, answerFourFrame, answerFourLabel, backgroundImageLabel, timeLimitFrame, timeLimitLabel, rightFrame, Login.titleFont, Login.defaultFont, Login.buttonFont))
        
    questions = [['No Questions']]
    def createQuiz(self, username, titleFont, defaultFont, buttonFont):
        ## Retrieves the assigned height, width and fonts for the main create question page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()
        
        mainCreateQuizPage = tk.Tk()
        mainCreateQuizPage.title("Create Quiz")

        canvas = tk.Canvas(mainCreateQuizPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(mainCreateQuizPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        welcomeLabel = tk.Label(mainframe, text = "Create Question", bg = 'gray', font = titleFont)
        welcomeLabel.place(relheight = 0.1, relwidth = 1)

        returnButton = tk.Button(mainframe, text = "Go\nBack", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.returnConfirmation(mainCreateQuizPage, username, Login.titleFont, Login.defaultFont, Login.buttonFont))
        returnButton.place(relheight = 0.1, relwidth = 0.1)

        background = tk.Frame(mainCreateQuizPage, bg = 'black')
        background.place(rely = 0.1, relheight = 0.9, relwidth = 1)

        questionsFrame = tk.Frame(mainCreateQuizPage, bg = '#73ade5')
        questionsFrame.place(rely = 0.1, relheight = 0.9, relwidth = 0.3)

        questionListbox = tk.Listbox(questionsFrame, font = defaultFont, exportselection = False)
        listboxHeight = 0
        buttonPos = 0.1
        for each in self.questions:
            if len(self.questions) == 1:
                questionListbox.insert('end', each[0])
            else:
                if each != ['No Questions']:
                    questionListbox.insert('end', each[0])
            if buttonPos < 0.8:
                listboxHeight += 0.1
                buttonPos += 0.1
        questionListbox.place(relx = 0.1, rely = 0.05, relheight = listboxHeight, relwidth = 0.8)
        questionListbox.bind('<<ListboxSelect>>', lambda x: self.displayQuestion('Create Quiz', None, None, questionListbox, None, questionLabel, questionListbox.get(questionListbox.curselection()), questionFrame, answerOneFrame, answerOneLabel, answerTwoFrame, answerTwoLabel, answerThreeFrame, answerThreeLabel, answerFourFrame, answerFourLabel, backgroundImageLabel, timeLimitFrame, timeLimitLabel, rightFrame, Login.titleFont, Login.defaultFont, Login.buttonFont))

        addQuestionButton = tk.Button(questionsFrame, text = "Add Question", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.mainCreateQuestionMenu(username, mainCreateQuizPage, Login.titleFont, Login.defaultFont, Login.buttonFont))
        addQuestionButton.place(relx = 0.2, rely = buttonPos, relheight = 0.1, relwidth = 0.6)

        rightFrame = tk.Frame(mainCreateQuizPage, bg = '#80c1ff')
        rightFrame.place(relx = 0.305, rely = 0.1, relheight = 0.9, relwidth = 0.695)

        backgroundImageLabel = tk.Label(rightFrame)
        questionFrame = tk.Frame(rightFrame)
        questionLabel = tk.Label(questionFrame)
        answerOneFrame = tk.Frame(rightFrame)
        answerOneLabel = tk.Label(answerOneFrame)
        answerTwoFrame = tk.Frame(rightFrame)
        answerTwoLabel = tk.Label(answerTwoFrame)
        answerThreeFrame = tk.Frame(rightFrame)
        answerThreeLabel = tk.Label(answerThreeFrame)
        answerFourFrame = tk.Frame(rightFrame)
        answerFourLabel = tk.Label(answerFourFrame)
        timeLimitFrame = tk.Frame(rightFrame)
        timeLimitLabel = tk.Label(timeLimitFrame)
        
        saveButton = tk.Button(rightFrame, text = "Save", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.saveQuiz(mainCreateQuizPage, username, Login.titleFont, Login.defaultFont, Login.buttonFont))
        saveButton.place(relx = 0.2, rely = 0.8, relheight = 0.1, relwidth = 0.2)

        mainCreateQuizPage.mainloop()
        

    ########################## BUTTONS FOR MAIN CREATE QUIZ PAGE ##########################

    def returnConfirmation(self, previousPage, username, titleFont, defaultFont, buttonFont):
        ## Retrieves the assigned height, width and fonts for the main create question page
        mainScreenWidth = saveNewQuiz.getScreenWidth()
        mainScreenHeight = saveNewQuiz.getScreenHeight()
        
        returnConfirmationPage = tk.Tk()
        returnConfirmationPage.title("Confirm Return")

        canvas = tk.Canvas(returnConfirmationPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(returnConfirmationPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        confirmationLabel = tk.Label(mainframe, text = "Are you sure you want to return?\nAnything not saved will be discarded", bg = 'gray', font = defaultFont)
        confirmationLabel.place(relx = 0.2, rely = 0.25, relheight = 0.2, relwidth = 0.6)

        confirmButton = tk.Button(mainframe, text = "Confirm", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: (returnConfirmationPage.destroy(), self.returnToMainMenu(previousPage, username)))
        confirmButton.place(relx = 0.375, rely = 0.65, relheight = 0.15, relwidth = 0.25)

        returnConfirmationPage.mainloop()

    def returnToMainMenu(self, previousPage, username):        
        previousPage.destroy()
        userType = viewingFromDatabase.viewFromDatabase(c, False, False, 'accountType', 'username', "'"+username+"'", 'UserDetails')
        if userType[0][0] == 'Admin':
            mainMenu.adminMainMenuPage(username, Login.titleFont, Login.buttonFont, Login.defaultFont)
        if userType[0][0] == 'Student':
            mainMenu.studentMainMenuPage(username, Login.titleFont, Login.buttonFont, Login.defaultFont)
        if userType[0][0] == 'Parent':
            mainMenu.parentMainMenuPage(username, Login.titleFont, Login.buttonFont, Login.defaultFont)

    def displayQuestion(self, previousFunction, answerOneEntry, playQuizPage, questionListbox, questions, questionLabel, selectedQuestion, questionFrame, answerOneFrame, answerOneLabel, answerTwoFrame, answerTwoLabel, answerThreeFrame, answerThreeLabel, answerFourFrame, answerFourLabel, backgroundImageLabel, timeLimitFrame, timeLimitLabel, rightFrame, titleFont, defaultFont, buttonFont):
        ## Hide all answer frames (in the case of changing questions)
        answerOneFrame.place_forget()
        answerOneFrame.config(highlightthickness = 0)
        answerTwoFrame.place_forget()
        answerTwoFrame.config(highlightthickness = 0)
        answerThreeFrame.place_forget()
        answerThreeFrame.config(highlightthickness = 0)
        answerFourFrame.place_forget()
        answerFourFrame.config(highlightthickness = 0)

        ## Check if class questions list is above 0
        if previousFunction == 'Create Quiz':
            ## Find position of selected question
            for each in self.questions:
                if each[0] == selectedQuestion:
                    try:
                        answers = each[1]
                        correctAnswer = each[2]
                        timeLimit = each[3]
                        background = each[4]
                    except:
                        answers = []
                        correctAnswer = ''
                        timeLimit = ''
                        background = ''
        elif previousFunction == 'View Quizzes':
            ## If retrieving from database
            index = questionListbox.get(0, "end").index(selectedQuestion)
            answers = [questions[index][5], questions[index][6], questions[index][7], questions[index][8]] 
            correctAnswer = questions[index][5]
            timeLimit = questions[index][9]
            background = questions[index][11]
        elif previousFunction == 'Play Quiz':
            ## Retrieve question details from list (where selectedQuestion is the round of the for loop)
            answers = [questions[selectedQuestion][5], questions[selectedQuestion][6], questions[selectedQuestion][7], questions[selectedQuestion][8]]
            ## Shuffle answers list
            random.shuffle(answers)
            correctAnswer = questions[selectedQuestion][5]
            timeLimit = questions[selectedQuestion][9]
            background = questions[selectedQuestion][11]
            selectedQuestion = questions[selectedQuestion][3]
                    
        if background == 1:
            ## Import and convert background one and place it as background
            backgroundOneImage = Image.open('BackgroundOne.jpg')
            backgroundOneImage = backgroundOneImage.resize((1500,1000))
            tkBackgroundOneImage = ImageTk.PhotoImage(backgroundOneImage)
            backgroundImageLabel.configure(image = tkBackgroundOneImage)
            backgroundImageLabel.image = tkBackgroundOneImage
            backgroundImageLabel.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        elif background == 2:
            ## Import and convert background two and place it as background
            backgroundTwoImage = Image.open('BackgroundTwo.jpg')
            backgroundTwoImage = backgroundTwoImage.resize((1500,1000))
            tkBackgroundTwoImage = ImageTk.PhotoImage(backgroundTwoImage)
            backgroundImageLabel.configure(image = tkBackgroundTwoImage)
            backgroundImageLabel.image = tkBackgroundTwoImage
            backgroundImageLabel.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        elif background == 3:
            ## Import and convert background three and place it as background
            backgroundThreeImage = Image.open('BackgroundThree.jpg')
            backgroundThreeImage = backgroundThreeImage.resize((1500,1000))
            tkBackgroundThreeImage = ImageTk.PhotoImage(backgroundThreeImage)
            backgroundImageLabel.configure(image = tkBackgroundThreeImage)
            backgroundImageLabel.image = tkBackgroundThreeImage
            backgroundImageLabel.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)

        answers = [x for x in answers if x != None]
        if len(answers) > 0:
            ## Configure and place question frame and label and configure answer one label
            questionLabel.config(text = selectedQuestion, bg = 'gray', font = titleFont, wraplength = 500)
            questionFrame.place(relx = 0.05, rely = 0.05, relheight = 0.25, relwidth = 0.9)
            questionLabel.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
            answerOneLabel.config(text = answers[0], bg = 'gray', wraplength = 100)
        if len(answers) == 1:
            ## Place answer one frame and label for answer input questions (wider frame)
            answerOneFrame.place(relx = 0.15, rely = 0.35, relheight = 0.15, relwidth = 0.7)
            answerOneLabel.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        if len(answers) > 1:
            ## Configure and place answer one and two frame and label for multiple choice questions
            answerOneFrame.place(relx = 0.15, rely = 0.35, relheight = 0.15, relwidth = 0.3)
            answerOneLabel.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
            answerTwoLabel.config(text = answers[1], bg = 'gray', wraplength = 100)
            answerTwoFrame.place(relx = 0.55, rely = 0.35, relheight = 0.15, relwidth = 0.3)
            answerTwoLabel.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        if len(answers) > 2:
            ## Configure and place answer three frame and label
            answerThreeLabel.config(text = answers[2], bg = 'gray', wraplength = 100)
            answerThreeFrame.place(relx = 0.15, rely = 0.55, relheight = 0.15, relwidth = 0.3)
            answerThreeLabel.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        if len(answers) > 3:
            ## Configure and place answer four frame and label
            answerFourLabel.config(text = answers[3], bg = 'gray', wraplength = 100)
            answerFourFrame.place(relx = 0.55, rely = 0.55, relheight = 0.15, relwidth = 0.3)
            answerFourLabel.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)

        if previousFunction == 'Play Quiz':
            ## If answer input question...
            if len(answers) == 1:
                ## Hide answer label
                answerOneLabel.place(relheight = 0, relwidth = 0)
                ## Create entry
                answerOneEntry.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
            ## If multiple choice question...
            else:
                ## Bind answer labels to highlightOption function
                answerOneLabel.bind("<Button-1>", lambda x: self.highlightOption(answerOneFrame, answerOneFrame, answerTwoFrame, answerThreeFrame, answerFourFrame))
                answerTwoLabel.bind("<Button-1>", lambda x: self.highlightOption(answerTwoFrame, answerOneFrame, answerTwoFrame, answerThreeFrame, answerFourFrame))
                answerThreeLabel.bind("<Button-1>", lambda x: self.highlightOption(answerThreeFrame, answerOneFrame, answerTwoFrame, answerThreeFrame, answerFourFrame))
                answerFourLabel.bind("<Button-1>", lambda x: self.highlightOption(answerFourFrame, answerOneFrame, answerTwoFrame, answerThreeFrame, answerFourFrame))

        if correctAnswer == 1:
            answerOneFrame.config(highlightthickness = 3, highlightbackground = 'green')
        elif correctAnswer == 2:
            answerTwoFrame.config(highlightthickness = 3, highlightbackground = 'green')
        elif correctAnswer == 3:
            answerThreeFrame.config(highlightthickness = 3, highlightbackground = 'green')
        elif correctAnswer == 4:
            answerFourFrame.config(highlightthickness = 3, highlightbackground = 'green')            

        answerInput = ''
        correct = False
        if timeLimit != '':
            timeLimitLabel.config(text = 'Time Limit: ' + str(timeLimit), bg = 'gray')
            timeLimitFrame.place(relx = 0.75, rely = 0.75, relheight = 0.1, relwidth = 0.2)
            timeLimitLabel.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
            if previousFunction == 'Play Quiz':
                ## While time limit is greater than 0 (i.e. there is time remaining)
                while timeLimit > 0:
                    timeLimit -= 1
                    time.sleep(1)
                    timeLimitLabel.config(text = 'Time Limit: ' + str(timeLimit))
                    playQuizPage.update()
                ## When time has finished
                if timeLimit == 0:
                    ## Create variable for user's input for the answer
                    answerInput = ''
                    if len(answers) == 1:
                        answerInput = answerOneEntry.get()
                    else:
                        ## For each widget in the mainframe of the play quiz page
                        for child in rightFrame.winfo_children():
                            ## Check thickness of the widget to see if 3
                            if child.cget('highlightthickness') == 3:
                                ## If 3, find children of the given frame
                                for child1 in child.winfo_children():
                                    ## Assign answer from retrieving text from that frame
                                    answerInput = child1.cget('text')
                progressID = viewingFromDatabase.viewFromDatabase(c, False, True, 'progressID', None, None, 'Progress ORDER BY progressID DESC LIMIT 1')
                correct = self.checkAnswer(answerInput, correctAnswer)
                updatingDatabase.updateInDatabase(conn, c, 'correct', str(correct), 'progressID', "'"+str(progressID[0][0])+"'", 'Progress')

        return answerInput, correctAnswer, correct
                
    def highlightOption(self, selectedFrame, answerOneFrame, answerTwoFrame, answerThreeFrame, answerFourFrame):
        ## Remove border from all options (in case of previous selection)
        answerOneFrame.config(highlightthickness = 0)
        answerTwoFrame.config(highlightthickness = 0)
        answerThreeFrame.config(highlightthickness = 0)
        answerFourFrame.config(highlightthickness = 0)
        ## Add blue border on chosen frame
        selectedFrame.config(highlightthickness = 3, highlightbackground = 'blue')

    def checkAnswer(self, answerInput, correctAnswer):
        if answerInput == correctAnswer:
            return True
        else:
            return False

    def saveQuiz(self, mainCreateQuizPage, username, titleFont, defaultFont, buttonFont):
        print('Save Quiz')
        ## Retrieves the assigned height, width and fonts for the main create question page
        mainScreenWidth = saveNewQuiz.getScreenWidth()
        mainScreenHeight = saveNewQuiz.getScreenHeight()
        
        saveQuizPage = tk.Tk()
        saveQuizPage.title("Save Quiz")

        canvas = tk.Canvas(saveQuizPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(saveQuizPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        ## If no questions have been created
        if len(self.questions) == 1:
            blankLabel = tk.Label(mainframe, text = "You cannot save an empty quiz!", bg = 'gray', font = defaultFont)
            blankLabel.place(relx = 0.15, rely = 0.2, relheight = 0.1, relwidth = 0.5)

            returnButton = tk.Button(mainframe, text = "Return", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = saveQuizPage.destroy)
            returnButton.place(relx = 0.7, rely = 0.8, relheight = 0.15, relwidth = 0.25)
            
        ## If questions have been created
        else:
            subjectFrame = tk.Frame(mainframe, bg = 'gray')
            subjectFrame.place(relx = 0.1, rely = 0.2, relheight = 0.15, relwidth = 0.85)

            subjectLabel = tk.Label(subjectFrame, text = "Enter the subject:", font = defaultFont)
            subjectLabel.place(relx = 0.02, rely = 0.1, relheight = 0.8, relwidth = 0.35)

            subjectEntry = tk.Entry(subjectFrame)
            subjectEntry.place(relx = 0.4, rely = 0.1, relheight = 0.8, relwidth = 0.58)
            subjectEntry.bind("<Return>", lambda x: self.confirmSave(subjectEntry.get(), levelEntry.get()))

            levelFrame = tk.Frame(mainframe, bg = 'gray')
            levelFrame.place(relx = 0.1, rely = 0.4, relheight = 0.15, relwidth = 0.85)

            levelLabel = tk.Label(levelFrame, text = "Enter the level: ", font = defaultFont)
            levelLabel.place(relx = 0.02, rely = 0.1, relheight = 0.8, relwidth = 0.35)

            levelEntry = tk.Entry(levelFrame)
            levelEntry.place(relx = 0.4, rely = 0.1, relheight = 0.8, relwidth = 0.58)
            levelEntry.bind("<Return>", lambda x: self.confirmSave(subjectEntry.get(), levelEntry.get()))

            confirmButton = tk.Button(mainframe, text = "Confirm", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.confirmSave(subjectEntry.get(), levelEntry.get(), mainCreateQuizPage, saveQuizPage, username))
            confirmButton.place(relx = 0.4, rely = 0.7, relheight = 0.15, relwidth = 0.2)

            saveQuizPage.mainloop()

    def confirmSave(self, subject, level, mainCreateQuizPage, previousPage, username):
        ## Create record for quiz table and add it to database
        quizRecord = [None, subject, level, len(self.questions)-1]
        addingToDatabase.addToDatabase(conn, c, quizRecord, 'Quiz')

        ## Retrieve the quiz ID of the last entry in the quiz table
        quizID = viewingFromDatabase.viewFromDatabase(c, False, True, 'quizID', None, None, 'Quiz ORDER BY quizID DESC LIMIT 1')
        quizID = quizID[0][0]

        ## Remove ['No Questions'] from questions list 
        self.questions.remove(['No Questions'])

        characterLimit = None
        ## For each question
        for each in self.questions:
            ## Retrieve answers from questions list
            if len(each[1]) == 1:
                answerOne = each[1][0]
                questionType = 'Answer Input'
                characterLimit = each[2]
            if len(each[1]) > 1:
                ## If correct answer is greater than 1 (i.e. the correct answer is not at the front of the list)
                if each[2] > 1:
                    ## Place correct answer at front of answers list
                    each[1].insert(0, each[1].pop(each[2]-1))
                answerOne = each[1][0]
                answerTwo = each[1][1]
                questionType = 'Multiple Choice'
            else:
                answerTwo = None
            if len(each[1]) > 2:
                answerThree = each[1][2]
            else:
                answerThree = None
            if len(each[1]) > 3:
                answerFour = each[1][3]
            else:
                answerFour = None
            ## Create record for question table
            questionRecord = [None, quizID, questionType, each[0], len(each[1]), answerOne, answerTwo, answerThree, answerFour, each[3], characterLimit, each[4]]
            addingToDatabase.addToDatabase(conn, c, questionRecord, 'Question')

        ## Reset the questions list
        self.questions = [['No Questions']]

        ## Return to main menu
        mainCreateQuizPage.destroy()
        self.returnToMainMenu(previousPage, username)

    ######################################## END OF ###########################################

    ## Creates the main create question page interface
    def mainCreateQuestionMenu(self, username, mainCreateQuizPage, titleFont, defaultFont, buttonFont):
        ## Retrieves the assigned height, width and fonts for the main create question page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()
        
        mainCreateQuestionMenuPage = tk.Tk()
        mainCreateQuestionMenuPage.title("Create Question")

        canvas = tk.Canvas(mainCreateQuestionMenuPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(mainCreateQuestionMenuPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        welcomeLabel = tk.Label(mainframe, text = "Create Question", bg = 'gray', font = titleFont)
        welcomeLabel.place(relx = 0, rely = 0, relheight = 0.15, relwidth = 1)

        selectQuestionTypeLabel = tk.Label(mainframe, text = "Please select a question type:", bg = '#80c1ff', font = defaultFont) 
        selectQuestionTypeLabel.place(relx = 0.03, rely = 0.18, relheight = 0.1, relwidth = 0.4)

        multipleChoiceFrame = tk.Frame(mainframe, bg = 'gray')
        multipleChoiceFrame.place(relx = 0.325, rely = 0.31, relheight = 0.15, relwidth = 0.35)

        multipleChoiceButton = tk.Button(multipleChoiceFrame, text = "Multiple Choice", highlightbackground = '#E5E7E9', font = buttonFont, command = lambda: self.createNewQuestion('Multiple Choice', mainCreateQuestionMenuPage, username, mainCreateQuizPage, Login.titleFont, Login.defaultFont, Login.buttonFont))
        multipleChoiceButton.place(relx = 0.03, rely = 0.1, relheight = 0.8, relwidth = 0.94)

        answerInputFrame = tk.Frame(mainframe, bg = 'gray')
        answerInputFrame.place(relx = 0.325, rely = 0.51, relheight = 0.15, relwidth = 0.35)

        answerInputButton = tk.Button(answerInputFrame, text = "Answer Input", highlightbackground = '#E5E7E9', font = buttonFont, command = lambda: self.createNewQuestion('Answer Input', mainCreateQuestionMenuPage, username, mainCreateQuizPage, Login.titleFont, Login.defaultFont, Login.buttonFont))
        answerInputButton.place(relx = 0.03, rely = 0.1, relheight = 0.8, relwidth = 0.94)

        orderAnswersFrame = tk.Frame(mainframe, bg = 'gray')
        orderAnswersFrame.place(relx = 0.325, rely = 0.71, relheight = 0.15, relwidth = 0.35)

        orderAnswersButton = tk.Button(orderAnswersFrame, text = "Order Answers", highlightbackground = '#E5E7E9', font = buttonFont, command = lambda: self.createNewQuestion('Order Answers', mainCreateQuestionMenuPage, username, mainCreateQuizPage, Login.titleFont, Login.defaultFont, Login.buttonFont))
        orderAnswersButton.place(relx = 0.03, rely = 0.1, relheight = 0.8, relwidth = 0.94)

        returnButton = tk.Button(mainframe, text = "Return", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = mainCreateQuestionMenuPage.destroy)
        returnButton.place(relx = 0.77, rely = 0.87, relheight = 0.1, relwidth = 0.2)
        
        mainCreateQuestionMenuPage.mainloop()

    ########################## BUTTONS FOR MAIN CREATE QUESTION PAGE ##########################

    ## Creates the create multiple choice question page interface
    answerOptions = 2
    answers =[]
    def createNewQuestion(self, typeOfQuestion, previousPage, username, mainCreateQuizPage, titleFont, defaultFont, buttonFont):
        previousPage.destroy()
        ## Retrieves the assigned height, width and fonts for the main create question page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()
        
        mainCreateQuestionPage = tk.Toplevel()
        mainCreateQuestionPage.title("Create Question")

        canvas = tk.Canvas(mainCreateQuestionPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        background = tk.Frame(mainCreateQuestionPage, bg = 'black')
        background.place(relheight = 1, relwidth = 1)

        mainframe = tk.Frame(mainCreateQuestionPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 0.695)

        questionEntry = tk.Entry(mainframe, font = titleFont, justify = 'center')
        questionEntry.place(relx = 0.05, rely = 0.05, relheight = 0.25, relwidth = 0.9)
        questionEntry.insert('end', 'Enter a Question...')

        createButton = tk.Button(mainframe, text = "Create", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.validateTimeLimit(mainCreateQuestionPage, username, mainCreateQuizPage, typeOfQuestion, questionEntry.get(), answerOneEntry, answerTwoEntry, answerThreeEntry, answerFourEntry, characterLimitEntry, timeLimitEntry.get(), trackCheckbutton, trackRadiobutton, maxTimeLimitLabel))
        createButton.place(relx = 0.4, rely = 0.85, relheight = 0.1, relwidth = 0.2)

        sideframe = tk.Frame(mainCreateQuestionPage, bg = '#80c1ff')
        sideframe.place(relheight = 1, relwidth = 0.3, relx = 0.7)

        timeLimitLabel = tk.Label(sideframe, text = 'Time Limit:', bg = 'gray', font = defaultFont)
        timeLimitLabel.place(relx = 0.225, rely = 0.5, relheight = 0.06, relwidth = 0.55)

        timeLimitEntry = tk.Entry(sideframe, justify = 'center', validate = 'key', validatecommand = (sideframe.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
        timeLimitEntry.place(relx = 0.4, rely = 0.59, relheight = 0.05, relwidth = 0.2)
        timeLimitEntry.insert('end', 30)

        maxTimeLimitLabel = tk.Label(sideframe)

        selectBackgroundLabel = tk.Label(sideframe, text = "Choose Background:", bg = 'gray', font = defaultFont) 
        selectBackgroundLabel.place(relx = 0.225, rely = 0.715, relheight = 0.06, relwidth = 0.55)

        backgroundOneImage = Image.open('BackgroundOne.jpg')
        backgroundOneImage = backgroundOneImage.resize((40,40))
        tkBackgroundOneImage = ImageTk.PhotoImage(backgroundOneImage)
        backgroundOneImageLabel = tk.Label(sideframe, image = tkBackgroundOneImage)
        backgroundOneImageLabel.place(relx = 0.24, rely = 0.8, relheight = 0.05, relwidth = 0.12)

        backgroundTwoImage = Image.open('BackgroundTwo.jpg')
        backgroundTwoImage = backgroundTwoImage.resize((40,40))
        tkBackgroundTwoImage = ImageTk.PhotoImage(backgroundTwoImage)
        backgroundTwoImageLabel = tk.Label(sideframe, image = tkBackgroundTwoImage)
        backgroundTwoImageLabel.place(relx = 0.44, rely = 0.8, relheight = 0.05, relwidth = 0.12)

        backgroundThreeImage = Image.open('BackgroundThree.jpg')
        backgroundThreeImage = backgroundThreeImage.resize((40,40))
        tkBackgroundThreeImage = ImageTk.PhotoImage(backgroundThreeImage)
        backgroundThreeImageLabel = tk.Label(sideframe, image = tkBackgroundThreeImage)
        backgroundThreeImageLabel.place(relx = 0.64, rely = 0.8, relheight = 0.05, relwidth = 0.12)

        trackRadiobutton = tk.IntVar() ## Creating a variable which will track the selected radiobutton
        radioButtonList = [] ## Empty list which is going to hold all the radiobuttons
        ## Creating three radiobuttons (where only one can be selected at a time)
        position = 0.24
        for j in range(3):
            radioButtonList.append(tk.Radiobutton(sideframe, value = j, variable = trackRadiobutton, text = j+1))
            radioButtonList[j].place(relx = position, rely = 0.85)
            position += 0.2

        answerOneEntry = tk.Entry(mainframe, justify = 'center')
        answerTwoEntry = tk.Entry(mainframe, justify = 'center')
        answerThreeEntry = tk.Entry(mainframe, justify = 'center')
        answerFourEntry = tk.Entry(mainframe, justify = 'center')
        trackCheckbutton = None

        characterLimitEntry = tk.Entry(sideframe, justify = 'center', validate = 'key', validatecommand = (sideframe.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))

        if typeOfQuestion == 'Multiple Choice':
            answerOneEntry.place(relx = 0.15, rely = 0.4, relheight = 0.15, relwidth = 0.3)
            answerOneEntry.insert('end', 'Answer 1...')

            answerTwoEntry.place(relx = 0.55, rely = 0.4, relheight = 0.15, relwidth = 0.3)
            answerTwoEntry.insert('end', 'Answer 2...')
            
            addAnswerOptionButton = tk.Button(sideframe, text = 'Add Answer Option', highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.addOption(answerThreeEntry, answerFourEntry, fourOptionsLabel, checkButtonList, sideframe, mainframe))
            addAnswerOptionButton.place(relx = 0.225, rely = 0.1, relheight = 0.06, relwidth = 0.55)

            fourOptionsLabel = tk.Label(sideframe)

            correctAnswerLabel = tk.Label(sideframe, text = 'Correct Answer:', bg = 'gray', font = defaultFont)
            correctAnswerLabel.place(relx = 0.225, rely = 0.25, relheight = 0.06, relwidth = 0.55)

            trackCheckbutton = tk.IntVar() ## Creating a variable which will track the selected checkbutton
            checkButtonList = [] ## Empty list which is going to hold all the checkbuttons
            ## Creating four checkbuttons (where only one can be selected at a time)
            for i in range(4):
                checkButtonList.append(tk.Checkbutton(sideframe, onvalue = i, variable = trackCheckbutton, text = i+1))
            checkButtonList[0].place(relx = 0.22, rely = 0.35)
            checkButtonList[1].place(relx = 0.37, rely = 0.35)
        elif typeOfQuestion == 'Answer Input':
            answerOneEntry.place(relx = 0.15, rely = 0.4, relheight = 0.15, relwidth = 0.7)
            answerOneEntry.insert('end', 'Answer...')

            characterLimitLabel = tk.Label(sideframe, text = 'Character Limit:', bg = 'gray', font = defaultFont)
            characterLimitLabel.place(relx = 0.225, rely = 0.12, relheight = 0.06, relwidth = 0.55)

            characterLimitEntry.place(relx = 0.4, rely = 0.21, relheight = 0.05, relwidth = 0.2)
            characterLimitEntry.insert('end', 30)

        mainCreateQuestionPage.mainloop()

    ########################## BUTTONS FOR CREATE MULTIPLE CHOICE QUESTION PAGE ##########################
            
    def validate(self, action, index, valueIfAllowed, priorValue, text, validationType, triggerType, widgetName):
        if valueIfAllowed:
            try:
                int(valueIfAllowed)
                return True
            except:
                return False
        else:
            return False

    def addOption(self, answerThreeEntry, answerFourEntry, fourOptionsLabel, checkButtonList, sideframe, mainframe):
        if self.answerOptions == 2:
            answerThreeEntry.place(relx = 0.15, rely = 0.6, relheight = 0.15, relwidth = 0.3)
            answerThreeEntry.insert('end', 'Answer 3...')
            checkButtonList[2].place(relx = 0.52, rely = 0.35)
            self.answerOptions += 1
        elif self.answerOptions == 3:
            answerFourEntry.place(relx = 0.55, rely = 0.6, relheight = 0.15, relwidth = 0.3)
            answerFourEntry.insert('end', 'Answer 4...')
            checkButtonList[3].place(relx = 0.67, rely = 0.35)
            self.answerOptions += 1
        elif self.answerOptions == 4:
            fourOptionsLabel.config(bg = 'gray', fg = 'red', text = 'Maximum Options Reached')
            fourOptionsLabel.place(relx = 0.215, rely = 0.18, relheight = 0.05, relwidth = 0.57)

    def validateTimeLimit(self, previousPage, username, mainCreateQuizPage, questionType, question, answerOne, answerTwo, answerThree, answerFour, characterLimitEntry, timeLimit, trackCheckbutton, trackRadiobutton, maxTimeLimitLabel):
        if 0 < int(timeLimit) <= 60:
            self.createQuestion(previousPage, username, mainCreateQuizPage, questionType, question, answerOne, answerTwo, answerThree, answerFour, characterLimitEntry, timeLimit, trackCheckbutton, trackRadiobutton)
        else:
            maxTimeLimitLabel.config(bg = 'gray', fg = 'red', text = 'Maximum Time Limit is 60s')
            maxTimeLimitLabel.place(relx = 0.2, rely = 0.66, relheight = 0.05, relwidth = 0.6)

    def createQuestion(self, previousPage, username, mainCreateQuizPage, questionType, question, answerOne, answerTwo, answerThree, answerFour, characterLimitEntry, timeLimit, trackCheckbutton, trackRadiobutton):
        background = trackRadiobutton.get() + 1

        if questionType == 'Multiple Choice':
            self.answers = [answerOne.get(), answerTwo.get()]
            if self.answerOptions > 2:
                self.answers.append(answerThree.get())
            if self.answerOptions == 4:
                self.answers.append(answerFour.get())
            correctAnswer = trackCheckbutton.get() + 1
            self.questions.append([question, self.answers, correctAnswer, timeLimit, background])
            self.answerOptions = 2
        elif questionType == 'Answer Input':
            self.answers = [answerOne.get()]
            characterLimit = int(characterLimitEntry.get())
            self.questions.append([question, self.answers, characterLimit, timeLimit, background])

        self.answers = []
        previousPage.destroy()
        mainCreateQuizPage.destroy()
        self.createQuiz(username, Login.titleFont, Login.defaultFont, Login.buttonFont)
        
    ######################################## END OF ###########################################

    def viewClasses(self, username, titleFont, defaultFont, buttonFont):
        ## Retrieve account type for given username from database
        accountType = viewingFromDatabase.viewFromDatabase(c, False, False, 'accountType', 'username', "'"+username+"'", 'UserDetails')
        accountType = accountType[0][0]
        ## If Admin set title of page and welcome label text to 'View Classes'
        if accountType == 'Admin':
            title = 'View Classes'
        ## If Student set title of page and welcome label text to 'View Progress'
        elif accountType == 'Student' or 'Parent':
            title = 'View Progress'
        
        ## Retrieves the assigned height, width and fonts for the main create question page
        mainScreenWidth = viewQuiz.getScreenWidth()
        mainScreenHeight = viewQuiz.getScreenHeight()

        ## Create page and title
        viewClassesPage = tk.Tk()
        viewClassesPage.title(title)

        ## Create canvas with dimensions of the view quizzes page
        canvas = tk.Canvas(viewClassesPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        ## Create main frame with default background
        mainframe = tk.Frame(viewClassesPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        ## Create label displaying 'View Classes'
        welcomeLabel = tk.Label(mainframe, text = title, bg = 'gray', font = titleFont)
        welcomeLabel.place(relheight = 0.1, relwidth = 1)

        ## Create return button to allow users to return to main menu
        returnButton = tk.Button(mainframe, text = "Go\nBack", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.returnToMainMenu(viewClassesPage, username))
        returnButton.place(relheight = 0.1, relwidth = 0.1)

        ## Create black background frame to show partition between studentsFrame, studentQuizzesFrame and studentProgressFrame
        background = tk.Frame(viewClassesPage, bg = 'black')
        background.place(rely = 0.1, relheight = 0.9, relwidth = 1)

        ## Create frame for all relevant students
        studentsFrame = tk.Frame(viewClassesPage, bg = '#73ade5')
        studentsFrame.place(rely = 0.1, relheight = 0.9, relwidth = 0.2)

        ## Create listbox for all relevant students
        studentsListbox = tk.Listbox(studentsFrame, font = defaultFont, exportselection = False)
        ## Set height of listbox and position of select button
        listboxHeight = 0
        buttonPos = 0.1
        ## If Admin retrieve all students for that user
        if accountType == 'Admin':
            ## Retrieve userID from database with given username
            userID = viewingFromDatabase.viewFromDatabase(c, False, False, 'userID', 'username', "'"+username+"'", 'UserDetails')
            ## Retrieve students' usernames from database with given adminID and 'Students' as account type
            students = viewingFromDatabase.viewFromDatabase(c, False, False, 'username', 'adminID', str(userID[0][0])+" AND accountType = 'Student'", 'UserDetails')
        ## If Student add username to students list in correct format
        elif accountType == 'Student':
            students = [[username]]
        #elif accountType == 'Parent': --> ASSIGN STUDENT TO PARENT IN DB
        for i in range(len(students)):
            ## Insert each student into the listbox
            studentsListbox.insert('end', students[i][0])
            ## If not reached bottom of page
            if buttonPos < 0.8:
                ## Increase height of listbox and button position
                listboxHeight += 0.1
                buttonPos += 0.1
        ## Place the listbox
        studentsListbox.place(relx = 0.1, rely = 0.05, relheight = listboxHeight, relwidth = 0.8)
        studentsListbox.bind('<<ListboxSelect>>', lambda x: self.displayStudentQuizzes(username, viewClassesPage, studentsListbox.get(studentsListbox.curselection()), studentQuizzesListbox, selectButton, selectLabel, quizTitleLabel, usernameLabel, attemptsLabel, progressListbox))

        ## Create frame for all quizzes undertook by selected student
        studentQuizzesFrame = tk.Frame(viewClassesPage, bg = '#73ade5')
        studentQuizzesFrame.place(relx = 0.205, rely = 0.1, relheight = 0.9, relwidth = 0.2)

        ## Create listbox for all quizzes undertook by selected student
        studentQuizzesListbox = tk.Listbox(studentQuizzesFrame, font = defaultFont, exportselection = False)

        ## Create frame for progress of selected quiz of a selected student
        studentProgressFrame = tk.Frame(viewClassesPage, bg = '#80c1ff')
        studentProgressFrame.place(relx = 0.410, rely = 0.1, relheight = 0.9, relwidth = 0.590)

        ## Create and place label to select student
        selectLabel = tk.Label(studentProgressFrame, text = "Select a student", bg = 'gray', font = defaultFont)
        selectLabel.place(relx = 0.35, rely = 0.1, relheight = 0.1, relwidth = 0.3)
        
        ## Create button to select student
        selectButton = tk.Button(studentProgressFrame, text = "Select", highlightbackground = '#424949', fg = 'blue', font = defaultFont)

        ## Create labels and listbox for progress frame to use later
        quizTitleLabel = tk.Label(studentProgressFrame, bg = 'gray', font = defaultFont)
        usernameLabel = tk.Label(studentProgressFrame, bg = 'gray', font = defaultFont)
        attemptsLabel = tk.Label(studentProgressFrame, bg = 'gray', font = defaultFont)
        progressListbox = tk.Listbox(studentProgressFrame, font = defaultFont, exportselection = False)
        
        viewClassesPage.mainloop()

    def displayStudentQuizzes(self, username, viewClassesPage, student, studentQuizzesListbox, selectButton, selectLabel, quizTitleLabel, usernameLabel, attemptsLabel, progressListbox):
        ## Clear the question list box (to allow for changing questions)
        studentQuizzesListbox.delete(0,'end')
        ## Set height of listbox and position of select button
        listboxHeight = 0
        buttonPos = 0.1
        ## Retrieve userID from database with given student
        userID = viewingFromDatabase.viewFromDatabase(c, False, False, 'userID', 'username', "'"+student+"'", 'UserDetails')
        ## Retrieve quizIDs from database for given student
        quizIDList = viewingFromDatabase.viewFromDatabase(c, False, False, 'quizID', 'userID', str(userID[0][0]), 'Progress')
        ## Remove duplicates
        quizIDList = list(dict.fromkeys(quizIDList))
        
        quizzes = []
        for each in quizIDList:
            ## Retrieve quizzes from database for given student and add to quizzes list
            quiz = viewingFromDatabase.viewFromDatabase(c, True, False, None, 'quizID', str(each[0]), 'Quiz')
            quizzes.append(quiz)
        ## Add each quiz to the listbox
        for i in range(len(quizzes)):
            studentQuizzesListbox.insert('end', quizzes[i][0][1] + ' ' + quizzes[i][0][2])
            if buttonPos < 0.8:
                listboxHeight += 0.1
                buttonPos += 0.1
        studentQuizzesListbox.place(relx = 0.1, rely = 0.05, relheight = listboxHeight, relwidth = 0.8)
        studentQuizzesListbox.bind('<<ListboxSelect>>', lambda x: self.displayStudentProgress(username, viewClassesPage, student, userID, selectButton, selectLabel, quizzes, studentQuizzesListbox, studentQuizzesListbox.get(studentQuizzesListbox.curselection()), quizTitleLabel, usernameLabel, attemptsLabel, progressListbox))

        ## Configure select label
        selectLabel.config(text = 'Select a quiz')

    def displayStudentProgress(self, username, viewClassesPage, student, userID, selectButton, selectLabel, quizzes, studentQuizzesListbox, selectedQuiz, quizTitleLabel, usernameLabel, attemptsLabel, progressListbox):
        ## Find which row of the listbox was selected
        index = studentQuizzesListbox.get(0, "end").index(selectedQuiz)
        ## Find the quizID of selected quiz using above index
        quizID = quizzes[index][0][0]
        noOfQuestions = quizzes[index][0][3]
        ## Find progress of student for selected quiz
        progress = viewingFromDatabase.viewFromDatabase(c, True, False, None, 'userID', str(userID[0][0]) + ' AND quizID = ' + str(quizID), 'Progress')
        ## Find how many attempts the user had at the quiz (by dividing the number of progress records by the number of questions)
        attempts = len(progress) // noOfQuestions

        ## Clear the progress list box (to allow for changing quizzes)
        progressListbox.delete(0,'end')

        ## Configure and place the labels, the select button and listbox created before
        selectLabel.place(relheight = 0, relwidth = 0)
        selectButton.config(command = lambda: self.displayProgress(viewClassesPage, username, student, progress, noOfQuestions, Login.titleFont, Login.defaultFont, Login.buttonFont))
        selectButton.place(relx = 0.4, rely = 0.83, relheight = 0.1, relwidth = 0.2)
        quizTitleLabel.config(text = quizzes[index][0][1] + ' ' + quizzes[index][0][2])
        quizTitleLabel.place(relx = 0.1, rely = 0.05, relheight = 0.08, relwidth = 0.2)
        usernameLabel.config(text = student)
        usernameLabel.place(relx = 0.75, rely = 0.05, relheight = 0.08, relwidth = 0.2)
        attemptsLabel.config(text = 'Number of attemps: ' + str(attempts))
        attemptsLabel.place(relx = 0.1, rely = 0.18, relheight = 0.08, relwidth = 0.3)
        progressListbox.place(relx = 0.1, rely = 0.29, relheight = 0.5, relwidth = 0.8)
        
        correctAnswers = 0
        counter = 0
        ## For each question in the selected quiz
        for each in progress:
            counter += 1
            ## Find questionID and corresponding question from database
            questionID = each[3]
            question = viewingFromDatabase.viewFromDatabase(c, False, False, 'question', 'questionID', str(questionID), 'Question')
            if each[4] == 'True':
                answer = 'Correct'
                correctAnswers += 1
            elif each[4] == 'False':
                answer = 'Incorrect'
            ## Insert the question, whether correct and the date and time to the progress listbox
            progressListbox.insert('end', question[0][0] + '  ' + answer + '  ' + each[5])
            if counter == noOfQuestions:
                ## Show number of correctly answered questions out of total for each attempt
                progressListbox.insert('end', str(correctAnswers) + '/' + str(noOfQuestions))
                correctAnswers = 0
                counter = 0

    def displayProgress(self, previousPage, username, student, progress, noOfQuestions, titleFont, defaultFont, buttonFont):
        ## Destroy previous page
        previousPage.destroy()
        
        ## Retrieves the assigned height, width and fonts for the main create question page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()

        ## Create page and title
        displayProgressPage = tk.Tk()
        displayProgressPage.title("View Progress")

        ## Create canvas with dimensions of the view quizzes page
        canvas = tk.Canvas(displayProgressPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        ## Create main frame with default background
        mainframe = tk.Frame(displayProgressPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        ## Create label displaying 'View Progress'
        welcomeLabel = tk.Label(mainframe, text = "View Progress", bg = 'gray', font = titleFont)
        welcomeLabel.place(relheight = 0.1, relwidth = 1)

        ## Create return button to allow users to return to main menu
        returnButton = tk.Button(mainframe, text = "Go\nBack", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: (displayProgressPage.destroy(), self.viewClasses(username, Login.titleFont, Login.defaultFont, Login.buttonFont)))
        returnButton.place(relheight = 0.1, relwidth = 0.1)

        ## Create counter to track questions
        counter = 0
        ## Create counter to track correct answers
        correctAnswers = 0
        ## Create list to store number of correct answers for each attempt
        correctAnswersList = []
        ## For each record in progress list
        for each in progress:
            counter += 1
            ## Find all correct answers and add to counter
            if each[4] == 'True':
                correctAnswers += 1
            if counter == noOfQuestions:
                ## If correctAnswersList is empty...add correctAnswers counter
                if len(correctAnswersList) == 0:
                    correctAnswersList.append(correctAnswers)
                ## If not...add correctAnswers counter - previous value (or last term of list)
                else:
                    ## Subtract correctAnswers answer by all previous values
                    correctAnswersCounter = correctAnswers
                    for each in correctAnswersList:
                        correctAnswersCounter = correctAnswersCounter - each
                    ## Append subtracted value to correct answers list
                    correctAnswersList.append(correctAnswersCounter)
                ## Reset the question counter
                counter = 0
                
        ## Determine size of pie chart slices
        data = [correctAnswers, len(progress)-correctAnswers]
        ## Initiate createPieChart function to create pie chart frame
        pieChart = self.createPieChart(displayProgressPage, data)
        ## Place pie chart frame
        pieChart.get_tk_widget().place(relx = 0.05, rely = 0.15, relheight = 0.6, relwidth = 0.5)

        ## Create labels displaying quiz progress information
        attempsLabel = tk.Label(mainframe, text = 'Number of attemps: ' + str(len(correctAnswersList)), bg = 'gray', font = defaultFont)
        attempsLabel.place(relx = 0.6, rely = 0.12, relheight = 0.1, relwidth = 0.35)

        ## Create counter to track attempts
        attempt = 0
        progressText = ''
        ## For each attempt...
        for each in correctAnswersList:
            attempt += 1
            ## Add attempt number and progress to progressText string
            progressText = progressText + '\n' + 'Attempt ' + str(attempt) + ': ' + '\n' + str(each) + '/' + str(noOfQuestions) + '\n'

        ## Create label for progress of all attempts
        progressLabel = tk.Label(mainframe, text = progressText, bg = 'gray', font = defaultFont)
        progressLabel.place(relx = 0.6, rely = 0.24, relheight = 0.54, relwidth = 0.35)

        ## Retrieve account type for given username from database
        accountType = viewingFromDatabase.viewFromDatabase(c, False, False, 'accountType', 'username', "'"+username+"'", 'UserDetails')
        accountType = accountType[0][0]
        ## If Admin create button to view full progress
        if accountType == 'Admin':
            ## Create button to view full progress
            viewFullProgressButton = tk.Button(mainframe, text = "View Full Progress", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: (displayProgressPage.destroy(), self.viewFullProgress(username, student, Login.titleFont, Login.defaultFont, Login.buttonFont)))
            viewFullProgressButton.place(relx = 0.4, rely = 0.82, relheight = 0.1, relwidth = 0.2)

        displayProgressPage.mainloop()

    def createPieChart(self, page, data):
        ## Create list for pie chart labels, i.e. Correct and Incorrect
        pieLabels = ['Correct', 'Incorrect']
        ## Create list for pie chart colours, i.e. green and red
        colours = ['#9FE2BF', '#F08080']

        ## Create figure for pie chart
        figure = plt.Figure(figsize=(5,5))
        ## Create background for pie chart
        figure.patch.set_facecolor('#73ade5')
        ## Create pie chart
        ax = figure.add_subplot(111)
        ax.pie(data, labels = pieLabels, colors = colours, explode = (0.1, 0), autopct = '%1.1f%%') 

        ## Create canvas for pie chart
        pieChart = FigureCanvasTkAgg(figure, page)
        return pieChart

    def viewFullProgress(self, username, student, titleFont, defaultFont, buttonFont):
        ## Retrieves the assigned height, width and fonts for the view full progress page
        mainScreenWidth = mainMenu.getScreenWidth()
        mainScreenHeight = mainMenu.getScreenHeight()

        ## Create page and title
        viewFullProgressPage = tk.Tk()
        viewFullProgressPage.title("View Progress")

        ## Create container and canvas with dimensions of the main menu page
        container = tk.Frame(viewFullProgressPage)
        container.pack()
        canvas = tk.Canvas(container, height = mainScreenHeight, width = mainScreenWidth, highlightthickness = 0, relief = 'ridge')
        canvas.pack(side = "left", fill = "both", expand = True)
        
        ## Create scroll bar
        scrollbar = ttk.Scrollbar(container, orient = "vertical", command = canvas.yview)
        scrollbar.pack(side = "right", fill = "y")

        ## Create frame which will be scrolled
        scrollableFrame = tk.Frame(canvas, bg = '#80c1ff')
        canvasFrame = canvas.create_window((0, 0), window = scrollableFrame, anchor = "nw")
        canvas.itemconfig(canvasFrame, height = 1400, width = mainScreenWidth)
        canvas.configure(yscrollcommand = scrollbar.set)
        scrollableFrame.bind("<Configure>", lambda x: canvas.configure(scrollregion = canvas.bbox("all")))

        ## Create label displaying 'View Progress'
        welcomeLabel = tk.Label(scrollableFrame, text = "View Progress", bg = 'gray', font = titleFont)
        welcomeLabel.place(relheight = 0.05, relwidth = 1)

        ## Create return button to allow users to return to view classes page
        returnButton = tk.Button(scrollableFrame, text = "Go\nBack", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: (viewFullProgressPage.destroy(), self.viewClasses(username, Login.titleFont, Login.defaultFont, Login.buttonFont)))
        returnButton.place(relheight = 0.05, relwidth = 0.1)

        studentLabel = tk.Label(scrollableFrame, text = student, bg = 'gray', font = defaultFont)
        studentLabel.place(relx = 0.75, rely = 0.07, relheight = 0.04, relwidth = 0.2)

        ## Retrieve userID from database with given student
        userID = viewingFromDatabase.viewFromDatabase(c, False, False, 'userID', 'username', "'"+student+"'", 'UserDetails')
        ## Retrieve quizIDs from database for given student
        quizIDList = viewingFromDatabase.viewFromDatabase(c, False, False, 'quizID', 'userID', str(userID[0][0]), 'Progress')
        ## Remove duplicates
        quizIDList = list(dict.fromkeys(quizIDList))
        
        quizzes = []
        quizLabels = ['Select Quiz']
        for each in quizIDList:
            ## Retrieve quizzes from database for given student and add to quizzes list
            quiz = viewingFromDatabase.viewFromDatabase(c, True, False, None, 'quizID', str(each[0]), 'Quiz')
            quizzes.append(quiz)
        ## Add names for each quiz to quizLabels list (i.e. what will appear in combobox)
        for each in quizzes:
            quizLabels.append([each[0][1],each[0][2]])
        ## Create combobox for all quizzes completed by selected student
        quizCombobox = ttk.Combobox(scrollableFrame, values = quizLabels, font = buttonFont, state = 'readonly')
        quizCombobox.place(relx = 0.05, rely = 0.08, relheight = 0.02, relwidth = 0.3)
        quizCombobox.current(0)
        quizCombobox.bind('<<ComboboxSelected>>', lambda x: self.showProgressGraph(student, userID, quizCombobox.get(), quizzes, scrollableFrame, otherUsersLabel, tableFrame))

        ## Create label for progress of other users
        otherUsersLabel = tk.Label(scrollableFrame, text = 'Other users for this quiz:', bg = 'gray')

        ## Create frame for all users progress table
        tableFrame = tk.Frame(scrollableFrame, bg = '#80c1ff')

        viewFullProgressPage.mainloop()

    def showProgressGraph(self, student, studentUserID, quiz, quizzes, page, otherUsersLabel, tableFrame):
        if quiz != 'Select Quiz':
            for each in range(len(quizzes)):
                if quiz == quizzes[each][0][1] + ' ' + quizzes[each][0][2]:
                    quizID = quizzes[each][0][0]
                    noOfQuestions = quizzes[each][0][3]

            progress = viewingFromDatabase.viewFromDatabase(c, True, False, None, 'userID', str(studentUserID[0][0]) + ' AND quizID = ' + str(quizID), 'Progress')
            ## Create counter to track questions
            counter = 0
            ## Create counter to track correct answers
            correctAnswers = 0
            ## Create list to store number of correct answers for each attempt
            correctAnswersList = []
            ## For each record in progress list
            for each in progress:
                counter += 1
                ## Find all correct answers and add to counter
                if each[4] == 'True':
                    correctAnswers += 1
                if counter == noOfQuestions:
                    ## If correctAnswersList is empty...add correctAnswers counter
                    if len(correctAnswersList) == 0:
                        correctAnswersList.append(correctAnswers)
                    ## If not...add correctAnswers counter - previous value (or last term of list)
                    else:
                        ## Subtract correctAnswers answer by all previous values
                        correctAnswersCounter = correctAnswers
                        for each in correctAnswersList:
                            correctAnswersCounter = correctAnswersCounter - each
                        ## Append subtracted value to correct answers list
                        correctAnswersList.append(correctAnswersCounter)
                    ## Reset the question counter
                    counter = 0
                    
            percentages = []
            ## If only one attempt...create pie chart
            if len(progress) == noOfQuestions:
                ## Determine size of pie chart slices
                data = [correctAnswers, len(progress)-correctAnswers]
                ## Initiate createPieChart function to create pie chart frame
                pieChart = self.createPieChart(page, data)
                ## Place pie chart frame
                pieChart.get_tk_widget().place(relx = 0.01, rely = 0.12, relheight = 0.3, relwidth = 0.5)
            ## Else create line graph
            else:
                ## For each result, find the percentage and append to percentages list
                for each in correctAnswersList:
                    percentage = each / noOfQuestions * 100
                    percentages.append(int(percentage))
                lineGraph = self.createLineGraph(page, len(progress)//noOfQuestions, percentages)
                lineGraph.get_tk_widget().place(relx = 0.01, rely = 0.12, relheight = 0.3, relwidth = 0.5)

            ## Create frame and scroll bar for selected user progress table
            container2 = tk.Frame(page)
            container2.place(relx = 0.52, rely = 0.12, relheight = 0.3, relwidth = 0.475)
            canvas2 = tk.Canvas(container2, highlightthickness = 0, relief = 'ridge')
            canvas2.pack(side = "left", fill = "both", expand = True)
            scrollbar2 = ttk.Scrollbar(container2, orient = "vertical", command = canvas2.yview)
            scrollbar2.pack(side = "right", fill = "y")

            ## Create frame for selected user progress table which will be scrolled
            scrollableFrame2 = tk.Frame(canvas2, bg = 'gray')
            canvasFrame2 = canvas2.create_window((0, 0), window = scrollableFrame2, anchor = "nw")
            canvas2.itemconfig(canvasFrame2, height = 500)
            canvas2.configure(yscrollcommand = scrollbar2.set)
            scrollableFrame2.bind("<Configure>", lambda x: canvas2.configure(scrollregion = canvas2.bbox("all")))

            ## Clear frame in case of changing quizzes
            for widget in tableFrame.winfo_children():
                widget.destroy()
            ## Create and place table for progress of all students for selected quiz
            ## Fetch the relevant data from the database by performing an inner join between the Progress, UserDetails and Quiz tables
            newTable = c.execute(""" SELECT UserDetails.username, Quiz.subject, Quiz.level, Progress.questionID, Progress.correct, Progress.time
                                FROM ((Progress
                                INNER JOIN UserDetails ON Progress.userID = UserDetails.userID)
                                INNER JOIN Quiz ON Progress.quizID = Quiz.quizID); """)
            newTableData = newTable.fetchall()

            table1Data = []
            table2Data = []
            ## For each record that matches the selected quiz...
            for each in newTableData:
                if quiz == each[1] + ' ' + each[2]:
                    ## Retrieve question from database
                    question = viewingFromDatabase.viewFromDatabase(c, False, False, 'question', 'questionID', str(each[3]), 'Question')
                    if each[4] == 'True':
                        correctField = 'Correct'
                    else:
                        correctField = 'Incorrect'
                    ## If progress of selected student...
                    if each[0] == student:
                        ## Append the question, whether correct and the time for each such record to table 1 list
                        table1Data.append([question[0][0], correctField, each[5]])
                    ## If not selected student...
                    else:
                        ## Append the username, the question, whether correct and the time for each such record to table 2 list
                        table2Data.append([each[0], question[0][0], correctField, each[5]])

            ## Create table for selected user's progress
            self.createTable(table1Data, scrollableFrame2, Login.defaultFont)
            ## Create table for progress of all other users
            self.createTable(table2Data, tableFrame, Login.defaultFont)
            ## Place other users label
            otherUsersLabel.place(relx = 0.05, rely = 0.44, relheight = 0.04, relwidth = 0.2)
            ## Place the frame for the table for progress of all other users
            tableFrame.place(relx = 0.05, rely = 0.49, relheight = 0.5, relwidth = 0.96)
                
    def createLineGraph(self, page, noOfAttemps, percentages):
        ## Create list for each number for number of attempts
        attempts = [x+1 for x in range(noOfAttemps)]
        
        ## Create figure for line graph
        figure = plt.Figure(figsize=(5,5))
        ## Create background for line graph
        figure.patch.set_facecolor('#73ade5')
        ## Create line graph
        ax = figure.add_subplot(111)
        ax.plot(attempts, percentages)
        ax.set_xlabel('Attempt')
        ax.set_ylabel('Percentage')

        ## Create and plot line of best fit
        x = np.array(attempts)
        y = np.array(percentages)
        m, c = np.polyfit(x, y, 1)
        ax.plot(x, m*x + c)

        ## Create canvas for line graph
        lineGraph = FigureCanvasTkAgg(figure, page)
        return lineGraph
                      
    def logOff(self):
        mainLogin.mainLoginPage(mainLogin.titleFont, mainLogin.buttonFont, mainLogin.defaultFont)

## Creates a child class for the login pages
class Login(Interface):
    def __init__(self, newScreenWidth, newScreenHeight, newType):
        ## Assigns attributes for login pages (height and width) from parent class Interface
        Interface.__init__(self, newScreenWidth, newScreenHeight)
        ## Assigns additional attribute unique to Login class (the type of login page, i.e. Admin, Student, Parent or the main login page)
        self.__type = newType

    ## Encapsulation of Login Class (Set Methods)
    def setNewType(self, newType):    
        self.__type = newType
        
    ## Encapsulation of Login Class (Get Methods)
    def getType(self):    
        return self.__type

    ## Sets the font and size for the title of the pages, the buttons and default writing on the mainframe
    titleFont = ('Helvetica', 25)
    buttonFont = ('Helvetica', 20)
    defaultFont = ('Helvetica', 17)

    # Creates the main login page interface
    def mainLoginPage(self, titleFont, buttonFont, defaultFont):
        root = tk.Tk()
        root.title("Login")

        ## Retrieves the assigned width and height for the main login page
        mainScreenWidth = mainLogin.getScreenWidth()
        mainScreenHeight = mainLogin.getScreenHeight()

        canvas = tk.Canvas(root, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(root, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        welcomeLabel = tk.Label(mainframe, text = "Login", bg = 'gray', font = titleFont)
        welcomeLabel.place(relx = 0, rely = 0, relheight = 0.15, relwidth = 1)

        selectUserLabel = tk.Label(mainframe, text = "Please select a type of user:", bg = '#80c1ff', font = defaultFont) 
        selectUserLabel.place(relx = 0.03, rely = 0.18, relheight = 0.1, relwidth = 0.4)

        teacherFrame = tk.Frame(root, bg = 'gray')
        teacherFrame.place(relx = 0.325, rely = 0.31, relheight = 0.15, relwidth = 0.35)

        teacherButton = tk.Button(teacherFrame, text = "Teacher", bg = '#E5E7E9', font = buttonFont, command = lambda: self.teacherButtonClicked(root))
        teacherButton.place(relx = 0.03, rely = 0.1, relheight = 0.8, relwidth = 0.94)

        studentFrame = tk.Frame(root, bg = 'gray')
        studentFrame.place(relx = 0.325, rely = 0.51, relheight = 0.15, relwidth = 0.35)

        studentButton = tk.Button(studentFrame, text = "Student", bg = '#E5E7E9', font = buttonFont, command = lambda: self.studentButtonClicked(root))
        studentButton.place(relx = 0.03, rely = 0.1, relheight = 0.8, relwidth = 0.94)

        parentFrame = tk.Frame(root, bg = 'gray')
        parentFrame.place(relx = 0.325, rely = 0.71, relheight = 0.15, relwidth = 0.35)

        parentButton = tk.Button(parentFrame, text = "Parent", bg = '#E5E7E9', font = buttonFont, command = lambda: self.parentButtonClicked(root))
        parentButton.place(relx = 0.03, rely = 0.1, relheight = 0.8, relwidth = 0.94)

        createAccountButton = tk.Button(mainframe, text = "Create Account", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.createAccountClicked(root, self.titleFont, self.buttonFont, self.defaultFont))
        createAccountButton.place(relx = 0.77, rely = 0.87, relheight = 0.1, relwidth = 0.2)
        
        root.mainloop()

    def teacherButtonClicked(self, root):
        ## Retrieves the assigned type for the admin login page
        loginType = adminLogin.getType()
        self.newLoginPage(loginType, root)

    def studentButtonClicked(self, root):
        ## Retrieves the assigned type for the student login page
        loginType = studentLogin.getType()
        self.newLoginPage(loginType, root)

    def parentButtonClicked(self, root):
        ## Retrieves the assigned type for the student login page
        loginType = parentLogin.getType()
        self.newLoginPage(loginType, root)
        
    def newLoginPage(self, loginType, root):
        screenWidth, screenHeight, title, differentLogin1, differentLogin2, differentLogin3, differentLogin4, differentLogin5 = self.loginPageDetails(loginType)
        root.destroy()
        self.loginPages(screenWidth, screenHeight, title, loginType, differentLogin1, differentLogin2, differentLogin3, differentLogin4, differentLogin5, self.titleFont, self.buttonFont, self.defaultFont)

    def loginPageDetails(self, loginType):
        ## Creates variables for fixed parts of message used in loginPages function
        differentLogin3 = ' or '
        differentLogin5 = ' login'
        ## Retrieves the assigned width, height and type for the relevant login page and accordingly assigns certain text to variables for login page
        if loginType == 'Admin':
            screenWidth = adminLogin.getScreenWidth()
            screenHeight = adminLogin.getScreenHeight()
            ## Assign the title of the page
            title = 'Teacher Login'
            ## Creates variables for parts of different login message in loginPages function which change with the type of login page
            differentLogin1 = 'Not a teacher? Try the'
            differentLogin2 = 'Student'
            differentLogin4 = 'Parent'
        elif loginType == 'Student':
            screenWidth = studentLogin.getScreenWidth()
            screenHeight = studentLogin.getScreenHeight()
            title = 'Student Login'
            differentLogin1 = 'Not a student? Try the'
            differentLogin2 = 'Teacher'
            differentLogin4 = 'Parent'
        elif loginType == 'Parent':
            screenWidth = parentLogin.getScreenWidth()
            screenHeight = parentLogin.getScreenHeight()
            title = 'Parent Login'
            differentLogin1 = 'Not a parent? Try the'
            differentLogin2 = 'Teacher'
            differentLogin4 = 'Student'
        return screenWidth, screenHeight, title, differentLogin1, differentLogin2, differentLogin3, differentLogin4, differentLogin5

    def loginPages(self, screenWidth, screenHeight, title, loginType, differentLogin1, differentLogin2, differentLogin3, differentLogin4, differentLogin5, titleFont, buttonFont, defaultFont):
        loginPage = tk.Tk()
        loginPage.title(title)

        canvas = tk.Canvas(loginPage, height = screenHeight, width = screenWidth)
        canvas.pack()

        mainframe = tk.Frame(loginPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        welcomeLabel = tk.Label(mainframe, text = "Login", bg = 'gray', font = titleFont)
        welcomeLabel.place(relx = 0, rely = 0, relheight = 0.1, relwidth = 1)

        differentLoginLabel1 = tk.Label(mainframe, text = differentLogin1, bg = 'gray', font = defaultFont)
        differentLoginLabel1.place(relx = 0.05, rely = 0.17, relheight = 0.1, relwidth = 0.25)

        differentLoginLabel2 = tk.Label(mainframe, text = differentLogin2, bg = 'gray', fg = 'blue', font = defaultFont)
        differentLoginLabel2.place(relx = 0.3, rely = 0.17, relheight = 0.1, relwidth = 0.09)
        differentLoginLabel2.bind("<Button-1>", lambda x: self.changeLogin(differentLogin2, loginPage))

        differentLoginLabel3 = tk.Label(mainframe, text = differentLogin3, bg = 'gray', font = defaultFont)
        differentLoginLabel3.place(relx = 0.39, rely = 0.17, relheight = 0.1, relwidth = 0.03)

        differentLoginLabel4 = tk.Label(mainframe, text = differentLogin4, bg = 'gray', fg = 'blue', font = defaultFont)
        differentLoginLabel4.place(relx = 0.42, rely = 0.17, relheight = 0.1, relwidth = 0.09)
        differentLoginLabel4.bind("<Button-1>", lambda x: self.changeLogin(differentLogin4, loginPage))
        
        differentLoginLabel5 = tk.Label(mainframe, text = differentLogin5, bg = 'gray', font = defaultFont)
        differentLoginLabel5.place(relx = 0.51, rely = 0.17, relheight = 0.1, relwidth = 0.07)

        usernameFrame = tk.Frame(mainframe, bg = 'gray')
        usernameFrame.place(relx = 0.2, rely = 0.35, relheight = 0.1, relwidth = 0.65)

        usernameLabel = tk.Label(usernameFrame, text = "Username: ", font = defaultFont)
        usernameLabel.place(relx = 0.02, rely = 0.1, relheight = 0.8, relwidth = 0.35)

        usernameEntry = tk.Entry(usernameFrame)
        usernameEntry.place(relx = 0.4, rely = 0.1, relheight = 0.8, relwidth = 0.58)
        usernameEntry.bind("<Return>", lambda x: self.loginClicked(loginPage, usernameEntry.get(), passwordEntry.get(), loginType, errorLabel))

        passwordFrame = tk.Frame(mainframe, bg = 'gray')
        passwordFrame.place(relx = 0.2, rely = 0.5, relheight = 0.1, relwidth = 0.65)

        passwordLabel = tk.Label(passwordFrame, text = "Password: ", font = defaultFont)
        passwordLabel.place(relx = 0.02, rely = 0.1, relheight = 0.8, relwidth = 0.35)

        passwordEntry = tk.Entry(passwordFrame, show = '*')
        passwordEntry.place(relx = 0.4, rely = 0.1, relheight = 0.8, relwidth = 0.58)
        passwordEntry.bind("<Return>", lambda x: self.loginClicked(loginPage, usernameEntry.get(), passwordEntry.get(), loginType, errorLabel))

        errorLabel = tk.Label(mainframe, bg = '#80c1ff')
        errorLabel.place(relx = 0.15, rely = 0.62, relheight = 0.06, relwidth = 0.75)
        
        loginButton = tk.Button(mainframe, text = "Log in", bg = 'gray', font = buttonFont, command = lambda: self.loginClicked(loginPage, usernameEntry.get(), passwordEntry.get(), loginType, errorLabel))
        loginButton.place(relx = 0.25, rely = 0.7, relheight = 0.1, relwidth = 0.25)

        quitButton = tk.Button(mainframe, text = "Quit", bg = 'gray', font = buttonFont, command = lambda: self.quitClicked(loginPage, self.titleFont, self.buttonFont, self.defaultFont))
        quitButton.place(relx = 0.55, rely = 0.7, relheight = 0.1, relwidth = 0.25)

        forgotPasswordButton = tk.Button(mainframe, text = "Forgot password", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: (loginPage.destroy(), self.forgotPasswordClicked(self.titleFont, self.buttonFont, self.defaultFont)))
        forgotPasswordButton.place(relx = 0.23, rely = 0.83, relheight = 0.08, relwidth = 0.2)

        createAccountButton = tk.Button(mainframe, text = "Create Account", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.createAccountClicked(loginPage, self.titleFont, self.buttonFont, self.defaultFont))
        createAccountButton.place(relx = 0.77, rely = 0.87, relheight = 0.1, relwidth = 0.2)
        
        loginPage.mainloop()

    def changeLogin(self, labelText, loginPage):
        if labelText == 'Teacher':
            self.teacherButtonClicked(loginPage)
        elif labelText == 'Student':
            self.studentButtonClicked(loginPage)
        elif labelText == 'Parent':
            self.parentButtonClicked(loginPage)

    blockCounter = 0
    def loginClicked(self, loginPage, usernameEntry, passwordEntry, loginType, errorLabel):
        correctUsername = False
        correctPassword = False
        accountBlocked = False
        accountUnverified = False

        if self.blockCounter < 3:
            ## Retrieve all usernames of the correct account type from database
            allUsers = viewingFromDatabase.viewFromDatabase(c, False, False, 'username', 'accountType', "'"+loginType+"'", 'UserDetails')
            allUsersList = []
            for each in range(len(allUsers)):
                allUsersList.append(allUsers[each][0])
            ## Check whether username exists & retrieves its corresponding password
            if usernameEntry in allUsersList:
                self.blockCounter+=1
                correctUsername = True
                password = viewingFromDatabase.viewFromDatabase(c, False, False, 'password', 'username', "'"+usernameEntry+"'", 'UserDetails')
                password = password[0][0]
                ## Compare hashed password input with correct password hash
                if self.hashPassword(passwordEntry) == password:
                    correctPassword = True
                accountReview = viewingFromDatabase.viewFromDatabase(c, False, False, 'reviewID', 'username', "'"+usernameEntry+"'", 'UserDetails')
                accountReview = accountReview[0][0]
                if accountReview == 4:
                    accountBlocked = True
                elif accountReview == 2:
                    accountUnverified = True
                
        if correctUsername == True and correctPassword == True and accountBlocked == False and accountUnverified == False:
            if loginType == 'Admin':
                ## Destroy log in page
                loginPage.destroy()
                ## Open admin main menu page
                mainMenu.adminMainMenuPage(usernameEntry, Login.titleFont, Login.buttonFont, Login.defaultFont)
            if loginType == 'Student':
                ## Destroy log in page
                loginPage.destroy()
                ## Open student main menu page
                mainMenu.studentMainMenuPage(usernameEntry, Login.titleFont, Login.buttonFont, Login.defaultFont)
            if loginType == 'Parent':
                ## Destroy log in page
                loginPage.destroy()
                ## Open parent main menu page
                mainMenu.parentMainMenuPage(usernameEntry, Login.titleFont, Login.buttonFont, Login.defaultFont)
        else:
            if self.blockCounter == 3:
                error = 'Your account has been blocked. Please ask an adminstator to unblock your account.'
                updatingDatabase.updateInDatabase(conn, c, 'reviewID', '4', 'username', "'"+usernameEntry+"'", 'UserDetails')
            elif accountBlocked == True:
                error = 'Your account is blocked. Please ask an adminstator to unblock your account.'
            elif accountUnverified == True:
                error = 'An adminstator must verify your account before you can start to use VisuaLearning.'
            elif correctUsername == True and correctPassword == False:
                error = 'Incorrect Password'
            elif correctUsername == False and correctPassword == False:
                error = 'This user does not exist. Please check if you are using the correct login.'
            errorLabel.config(text = error, bg = 'gray', fg = 'red')
        
    def quitClicked(self, previousPage, titleFont, buttonFont, defaultFont):
        ## Quit confirmation page
        ## Retrieves the assigned width and height for the quit confirmation page
        mainScreenWidth = quitConfirmation.getScreenWidth()
        mainScreenHeight = quitConfirmation.getScreenHeight()
        
        quitPage = tk.Tk()
        quitPage.title("Quit")

        canvas = tk.Canvas(quitPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(quitPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        confirmationLabel = tk.Label(mainframe, text = 'Are you sure you want to quit?', bg = 'gray', font = defaultFont)
        confirmationLabel.place(relx = 0.05, rely = 0.17, relheight = 0.15, relwidth = 0.5)

        yesButton = tk.Button(mainframe, text = "Yes", highlightbackground = '#424949', font = buttonFont, command = lambda: (previousPage.destroy(), quitPage.destroy()))
        yesButton.place(relx = 0.25, rely = 0.5, relheight = 0.15, relwidth = 0.25)

        noButton = tk.Button(mainframe, text = "No", highlightbackground = '#424949', font = buttonFont, command = quitPage.destroy)
        noButton.place(relx = 0.55, rely = 0.5, relheight = 0.15, relwidth = 0.25)

        quitPage.mainloop()

    def forgotPasswordClicked(self, titleFont, buttonFont, defaultFont):
        ## Retrieves the assigned width and height for the forgot password page
        mainScreenWidth = forgotPassword.getScreenWidth()
        mainScreenHeight = forgotPassword.getScreenHeight()

        forgotPasswordPage = tk.Tk()
        forgotPasswordPage.title("Forgotten Password")

        canvas = tk.Canvas(forgotPasswordPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(forgotPasswordPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        welcomeLabel = tk.Label(mainframe, text = "Forgotten Password", bg = 'gray', font = titleFont)
        welcomeLabel.place(relx = 0, rely = 0, relheight = 0.1, relwidth = 1)

        requestAdminLabel = tk.Label(mainframe, text = 'Please request an admin user to reset your password', bg = 'gray', font = defaultFont)
        requestAdminLabel.place(relx = 0.05, rely = 0.17, relheight = 0.1, relwidth = 0.6)

        selectAdminLabel = tk.Label(mainframe, text = 'Please enter your username\nand select an admin user:', bg = 'gray', font = defaultFont)
        selectAdminLabel.place(relx = 0.05, rely = 0.29, relheight = 0.1, relwidth = 0.34)

        usernameEntry = tk.Entry(mainframe)
        usernameEntry.place(relx = 0.45, rely = 0.29, relheight = 0.1, relwidth = 0.45)

        listbox = tk.Listbox(mainframe, font = defaultFont)
        listbox.place(relx = 0.15, rely = 0.415, relheight = 0.21, relwidth = 0.7)
        adminUsers = viewingFromDatabase.viewFromDatabase(c, False, False, 'username', 'accountType', "'Admin'", 'UserDetails')
        position = 1
        for each in adminUsers:
            listbox.insert(position, each)
            position += 1

        errorLabel = tk.Label(mainframe, bg = '#80c1ff')
        errorLabel.place(relx = 0.15, rely = 0.64, relheight = 0.08, relwidth = 0.7)

        selectButton = tk.Button(mainframe, text = "Select", highlightbackground = '#424949', font = buttonFont, command = lambda: self.selectAdminUser(listbox, usernameEntry.get(), errorLabel))
        selectButton.place(relx = 0.4, rely = 0.73, relheight = 0.1, relwidth = 0.2)

        loginAdminLabel = tk.Label(mainframe, text = 'Would you like to log in as an', bg = 'gray', font = defaultFont)
        loginAdminLabel.place(relx = 0.05, rely = 0.85, relheight = 0.1, relwidth = 0.34)

        adminLabel = tk.Label(mainframe, text = 'admin', bg = 'gray', fg = 'blue', font = defaultFont)
        adminLabel.place(relx = 0.38, rely = 0.85, relheight = 0.1, relwidth = 0.07)
        adminLabel.bind("<Button-1>", lambda x: teacherButtonClicked)

        questionMarkLabel = tk.Label(mainframe, text = '?', bg = 'gray', font = defaultFont)
        questionMarkLabel.place(relx = 0.445, rely = 0.85, relheight = 0.1, relwidth = 0.03)

        returnButton = tk.Button(mainframe, text = "Return", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.returnPage(forgotPasswordPage))
        returnButton.place(relx = 0.77, rely = 0.87, relheight = 0.1, relwidth = 0.2)

        forgotPasswordPage.mainloop()

    def selectAdminUser(self, listbox, username, errorLabel):
        ## Retrieve all usernames of the correct account type from database
        allUsers = viewingFromDatabase.viewFromDatabase(c, False, True, 'username', None, None, 'UserDetails')
        allUsersList = []
        for each in range(len(allUsers)):
            allUsersList.append(allUsers[each][0])
        ## Check whether inputted username is present in database
        if username in allUsersList:
            ## Retrieve selection from list-box (in the case of no selection, display error)
            try:
                adminUser = listbox.get(listbox.curselection())
                updatingDatabase.updateInDatabase(conn, c, 'reviewID', '3', 'username', "'"+username+"'", 'UserDetails')
                adminID = viewingFromDatabase.viewFromDatabase(c, False, False, 'userID', 'username', "'"+adminUser[0]+"'", 'UserDetails')
                updatingDatabase.updateInDatabase(conn, c, 'adminID', str(adminID[0][0]), 'username', "'"+username+"'", 'UserDetails')
                print('Done')
            except:
                error = 'Please select a user to reset your password'
                errorLabel.config(text = error, bg = 'gray', fg = 'red')
        else:
            ## If not found in database
            error = 'This username has not been found'
            errorLabel.config(text = error, bg = 'gray', fg = 'red')

    def createAccountClicked(self, previousPage, titleFont, buttonFont, defaultFont):
        # Destroys previous page
        previousPage.destroy()
        
        ## Retrieves the assigned width and height for the create account page
        mainScreenWidth = createAccount.getScreenWidth()
        mainScreenHeight = createAccount.getScreenHeight()

        createAccountPage = tk.Tk()
        createAccountPage.title("Create Account")

        canvas = tk.Canvas(createAccountPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(createAccountPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        welcomeLabel = tk.Label(mainframe, text = "Create Account", bg = 'gray', font = titleFont)
        welcomeLabel.place(relx = 0, rely = 0, relheight = 0.1, relwidth = 1)

        selectTypeLabel = tk.Label(mainframe, text = 'Please select the type of account you wish to create:', bg = 'gray', font = defaultFont)
        selectTypeLabel.place(relx = 0.05, rely = 0.15, relheight = 0.07, relwidth = 0.6)

        userTypeList = ttk.Combobox(mainframe, values = ["Teacher", "Student", "Parent"], font = buttonFont, state = 'readonly')
        userTypeList.place(relx = 0.7, rely = 0.16, relheight = 0.04, relwidth = 0.15)
        userTypeList.current(0)

        enterFirstNameLabel = tk.Label(mainframe, text = 'Enter your first name:', bg = 'gray', font = defaultFont)
        enterFirstNameLabel.place(relx = 0.05, rely = 0.27, relheight = 0.07, relwidth = 0.26)

        firstNameEntry = tk.Entry(mainframe)
        firstNameEntry.place(relx = 0.38, rely = 0.27, relheight = 0.07, relwidth = 0.55)
        firstNameEntry.bind("<Return>", lambda x: self.createUserAccount(createAccountPage, userTypeList.get(), firstNameEntry.get(), lastNameEntry.get(), usernameEntry.get(), passwordEntry.get(), adminUsersList.get(), firstNameEntry, lastNameEntry, usernameEntry, passwordEntry))

        enterLastNameLabel = tk.Label(mainframe, text = 'Enter your last name:', bg = 'gray', font = defaultFont)
        enterLastNameLabel.place(relx = 0.05, rely = 0.39, relheight = 0.07, relwidth = 0.26)

        lastNameEntry = tk.Entry(mainframe)
        lastNameEntry.place(relx = 0.38, rely = 0.39, relheight = 0.07, relwidth = 0.55)
        lastNameEntry.bind("<Return>", lambda x: self.createUserAccount(createAccountPage, userTypeList.get(), firstNameEntry.get(), lastNameEntry.get(), usernameEntry.get(), passwordEntry.get(), adminUsersList.get(), firstNameEntry, lastNameEntry, usernameEntry, passwordEntry))

        enterUsernameLabel = tk.Label(mainframe, text = 'Enter a username:', bg = 'gray', font = defaultFont)
        enterUsernameLabel.place(relx = 0.05, rely = 0.51, relheight = 0.07, relwidth = 0.22)

        usernameEntry = tk.Entry(mainframe)
        usernameEntry.place(relx = 0.38, rely = 0.51, relheight = 0.07, relwidth = 0.55)
        usernameEntry.bind("<Return>", lambda x: self.createUserAccount(createAccountPage, userTypeList.get(), firstNameEntry.get(), lastNameEntry.get(), usernameEntry.get(), passwordEntry.get(), adminUsersList.get(), firstNameEntry, lastNameEntry, usernameEntry, passwordEntry))

        enterPasswordLabel = tk.Label(mainframe, text = 'Enter a password:', bg = 'gray', font = defaultFont)
        enterPasswordLabel.place(relx = 0.05, rely = 0.63, relheight = 0.07, relwidth = 0.22)

        passwordEntry = tk.Entry(mainframe, show = '*')
        passwordEntry.place(relx = 0.38, rely = 0.63, relheight = 0.07, relwidth = 0.55)
        passwordEntry.bind("<Return>", lambda x: self.createUserAccount(createAccountPage, userTypeList.get(), firstNameEntry.get(), lastNameEntry.get(), usernameEntry.get(), passwordEntry.get(), adminUsersList.get(), firstNameEntry, lastNameEntry, usernameEntry, passwordEntry))
        
        selectAdminLabel = tk.Label(mainframe, text = 'Please select an admin account to verify your account', bg = 'gray', font = defaultFont)
        selectAdminLabel.place(relx = 0.05, rely = 0.75, relheight = 0.07, relwidth = 0.6)

        adminUsers = viewingFromDatabase.viewFromDatabase(c, False, False, 'username', 'accountType', "'Admin'", 'UserDetails')
        adminUserList = []
        for each in range(len(adminUsers)):
            adminUserList.append(adminUsers[each][0])
        adminUsersList = ttk.Combobox(mainframe, values = adminUserList, font = buttonFont, state = 'readonly')
        adminUsersList.place(relx = 0.67, rely = 0.76, relheight = 0.04, relwidth = 0.3)
        adminUsersList.current(0)

        createAccountButton = tk.Button(mainframe, text = "Create Account", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.createUserAccount(createAccountPage, userTypeList.get(), firstNameEntry.get(), lastNameEntry.get(), usernameEntry.get(), passwordEntry.get(), adminUsersList.get(), firstNameEntry, lastNameEntry, usernameEntry, passwordEntry))
        createAccountButton.place(relx = 0.35, rely = 0.87, relheight = 0.07, relwidth = 0.25)

        returnButton = tk.Button(mainframe, text = "Return", highlightbackground = '#424949', fg = 'blue', font = defaultFont, command = lambda: self.returnPage(createAccountPage))
        returnButton.place(relx = 0.83, rely = 0.92, relheight = 0.05, relwidth = 0.14)

        createAccountPage.mainloop()

    def createUserAccount(self, previousPage, userType, firstName, lastName, username, password, adminUser, firstNameEntry, lastNameEntry, usernameEntry, passwordEntry):
        ## Validation checks
        takenUsername = self.checkTakenUsername(username)
        invalidUsername, usernameErrorList = self.checkValidUsername(username)
        weakPassword, passwordErrorList = self.checkValidPassword(password)
        invalidFirstName = self.checkValidName(firstName)
        invalidLastName = self.checkValidName(lastName)

        ## If no inconsistencies...
        if takenUsername == False and invalidUsername == False and weakPassword == False and invalidFirstName == False and invalidLastName == False:
            ## Close previous page
            previousPage.destroy()
            newPassword = self.hashPassword(password)
            if userType == 'Teacher':
                userType = 'Admin'
            adminID = viewingFromDatabase.viewFromDatabase(c, False, False, 'userID', 'username', "'"+adminUser+"'", 'UserDetails')
            adminID = adminID[0][0]
            record = [None, userType, username, newPassword, firstName.capitalize(), lastName.capitalize(), 2, adminID]
            self.accountSuccessful(record, self.titleFont, self.buttonFont, self.defaultFont)
        else:
            self.accountFailed(invalidFirstName, firstNameEntry, invalidLastName, lastNameEntry, takenUsername, invalidUsername, usernameEntry, weakPassword, passwordEntry, usernameErrorList, passwordErrorList, self.titleFont, self.buttonFont, self.defaultFont)
        
    def checkTakenUsername(self, username):
        ## Check whether inputted username is already taken
        takenUsername = False
        ## Fetch all usernames from the database and put it in a list
        takenUsernames = viewingFromDatabase.viewFromDatabase(c, False, True, 'username', None, None, 'UserDetails')
        ## Check inputted username against list of current usernames
        for each in takenUsernames:
            if each[0] == username:
                takenUsername = True
        return takenUsername

    def checkValidUsername(self, username):
        ## Check whether inputted username is valid (to prevent SQL injection)
        invalidUsername = False
        ## Create list of all errors
        usernameErrorList = []
        if '=' in username or ';' in username:
            usernameErrorList.append('=;')
        if ' ' in username:
            usernameErrorList.append('Space')
        if username == '':
            usernameErrorList.append('empty')
        if username == 'username':
            usernameErrorList.append('username')
        if len(usernameErrorList) != 0:
            invalidUsername = True
        return invalidUsername, usernameErrorList

    def checkValidPassword(self, password):
        ## Check whether inputted password is valid (i.e. length > 7, contains number, character, symbol, upper and lower case)
        weakPassword = False
        passwordErrorList = []

        ## Checks to see whether password is greater than 7 characters
        if len(password) < 8:
            passwordErrorList.append('short')

        ## Check to see whether (lower case) character in password
        if not(re.search(r'[a-z]', password)):
            passwordErrorList.append('lowerCase')

        ## Check to see whether (upper case) character in password
        if not(re.search(r'[A-Z]', password)):
            passwordErrorList.append('upperCase')
        
        ## Check to see whether number in password
        if not(re.search(r'[0-9]', password)):
            passwordErrorList.append('number')
        
        ## Check to see whether symbol in password
        if not(re.search("[!@£$%^&*()_+={};:‘“\|`~,<.>/?'-]", password)):
            passwordErrorList.append('symbol')

        ## Check to see whether symbol in password
        if (re.search("[=;]", password)):
            passwordErrorList.append('=;')

        ## Check to see whether input is 'password' or blank (to prevent SQL injection or other errors)
        if password == 'password':
            passwordErrorList.append('password')
        if password == '':
            passwordErrorList.append('empty')

        if len(passwordErrorList) != 0:
            weakPassword = True
        return weakPassword, passwordErrorList

    def checkValidName(self, name):
        invalidName = not(name.isalpha())
        return invalidName

    def hashPassword(self, password):
        newPassword = hashlib.sha256(password.encode()).hexdigest()
        return newPassword
        
    def returnPage(self, page):
        page.destroy()
        self.mainLoginPage(self.titleFont, self.buttonFont, self.defaultFont)

    def accountSuccessful(self, record, titleFont, buttonFont, defaultFont):
        addingToDatabase.addToDatabase(conn, c, record, 'UserDetails')

        accountSuccessfulPage = tk.Tk()
        accountSuccessfulPage.title('Successful!')

        mainScreenWidth = newAccount.getScreenWidth()
        mainScreenHeight = newAccount.getScreenHeight()

        canvas = tk.Canvas(accountSuccessfulPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(accountSuccessfulPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        successfulLabel = tk.Label(mainframe, text = 'Your account has been successfully created!', bg = 'gray', font = defaultFont)
        successfulLabel.place(relx = 0.05, rely = 0.12, relheight = 0.1, relwidth = 0.6)

        askAdminLabel = tk.Label(mainframe, text = 'Please ask your adminstrator user to verify your\naccount before you are able to start using VisuaLearning', bg = 'gray', font = defaultFont)
        askAdminLabel.place(relx = 0.05, rely = 0.27, relheight = 0.2, relwidth = 0.73)

        loginLabel = tk.Label(mainframe, text = 'You can login in as an admin here:', bg = 'gray', font = defaultFont)
        loginLabel.place(relx = 0.05, rely = 0.52, relheight = 0.1, relwidth = 0.5)

        adminLoginLabel = tk.Label(mainframe, text = 'Admin Login', bg = 'gray', fg = 'blue', font = defaultFont)
        adminLoginLabel.place(relx = 0.6, rely = 0.52, relheight = 0.1, relwidth = 0.18)
        adminLoginLabel.bind("<Button-1>", lambda x: self.teacherButtonClicked(accountSuccessfulPage))

        closeButton = tk.Button(mainframe, text = "Close", highlightbackground = '#424949', font = buttonFont, command = lambda: self.returnPage(accountSuccessfulPage))
        closeButton.place(relx = 0.375, rely = 0.7, relheight = 0.15, relwidth = 0.25)

    def accountFailed(self, invalidFirstName, firstNameEntry, invalidLastName, lastNameEntry, takenUsername, invalidUsername, usernameEntry, weakPassword, passwordEntry, usernameErrorList, passwordErrorList, titleFont, buttonFont, defaultFont):
        if invalidFirstName == True:
            firstNameEntry.config(highlightthickness = 2, highlightbackground = 'red')
        else:
            firstNameEntry.config(highlightthickness = 2, highlightbackground = 'black')
            
        if invalidLastName == True:
            lastNameEntry.config(highlightthickness = 2, highlightbackground = 'red')
        else:
            lastNameEntry.config(highlightthickness = 2, highlightbackground = 'black')
            
        if takenUsername == True or invalidUsername == True:
            usernameEntry.config(highlightthickness = 2, highlightbackground = 'red')
        else:
            usernameEntry.config(highlightthickness = 2, highlightbackground = 'black')
            
        if weakPassword == True:
            passwordEntry.config(highlightthickness = 2, highlightbackground = 'red')
        else:
            passwordEntry.config(highlightthickness = 2, highlightbackground = 'black')

        self.failedPage(invalidFirstName, invalidLastName, takenUsername, usernameErrorList, passwordErrorList, self.titleFont, self.buttonFont, self.defaultFont)

    def failedPage(self, invalidFirstName, invalidLastName, takenUsername, usernameErrorList, passwordErrorList, titleFont, buttonFont, defaultFont):
        accountFailedPage = tk.Tk()
        accountFailedPage.title('Failed!')

        mainScreenWidth = newAccount.getScreenWidth()
        mainScreenHeight = newAccount.getScreenHeight()

        canvas = tk.Canvas(accountFailedPage, height = mainScreenHeight, width = mainScreenWidth)
        canvas.pack()

        mainframe = tk.Frame(accountFailedPage, bg = '#80c1ff')
        mainframe.place(relheight = 1, relwidth = 1)

        failedLabel = tk.Label(mainframe, text = 'Your account has failed to create', bg = 'gray', font = defaultFont)
        failedLabel.place(relx = 0.05, rely = 0.12, relheight = 0.1, relwidth = 0.45)

        checkLabel = tk.Label(mainframe, text = 'Please check the following:', bg = 'gray', font = defaultFont)
        checkLabel.place(relx = 0.05, rely = 0.25, relheight = 0.1, relwidth = 0.38)

        listbox = tk.Listbox(mainframe, font = defaultFont)
        listbox.place(relx = 0.1, rely = 0.4, relheight = 0.3, relwidth = 0.8)
        errorList = ['You have entered an invalid first name',
                     'You have entered an invalid last name',
                     'This username has already been taken. Please choose another one',
                     'Your username must not contain any of the following symbols: = ; ',
                     'Your username must not contain a space',
                     'Your username cannot be blank',
                     'Your username cannot be username',
                     'Your password is too short',
                     'Your password needs to contain a lower case letter',
                     'Your password needs to contain an upper case letter',
                     'Your password needs to contain a numerical character',
                     'Your password needs to contain a symbol',
                     'Your password must not contain any of the following symbols: = ; ',
                     'Your password is not secure enough',
                     'Your password cannot be blank']

        position = 1
        if invalidFirstName == True:
            listbox.insert(position, errorList[0])
            position += 1
        if invalidLastName == True:
            listbox.insert(position, errorList[1])
            position += 1
        if takenUsername == True:
            listbox.insert(position, errorList[2])
            position += 1
        if len(usernameErrorList) != 0:
            for each in usernameErrorList:
                if each == '=;':
                    listbox.insert(position, errorList[3])
                    position += 1
                if each == 'Space':
                    listbox.insert(position, errorList[4])
                    position += 1
                if each == 'empty':
                    listbox.insert(position, errorList[5])
                    position += 1
                if each == 'username':
                    listbox.insert(position, errorList[6])
                    position += 1
                    
        if len(passwordErrorList) != 0:
            for each in passwordErrorList:
                if each == 'short':
                    listbox.insert(position, errorList[7])
                    position += 1
                if each == 'lowerCase':
                    listbox.insert(position, errorList[8])
                    position += 1
                if each == 'upperCase':
                    listbox.insert(position, errorList[9])
                    position += 1
                if each == 'number':
                    listbox.insert(position, errorList[10])
                    position += 1
                if each == 'symbol':
                    listbox.insert(position, errorList[11])
                    position += 1
                if each == '=;':
                    listbox.insert(position, errorList[12])
                    position += 1
                if each == 'password':
                    listbox.insert(position, errorList[13])
                    position += 1
                if each == 'empty':
                    listbox.insert(position, errorList[14])
                    position += 1
        
        closeButton = tk.Button(mainframe, text = "Close", highlightbackground = '#424949', font = buttonFont, command = accountFailedPage.destroy)
        closeButton.place(relx = 0.375, rely = 0.75, relheight = 0.15, relwidth = 0.25)

## Creates a new instance of the Login class for the main login page and the admin, student and parent login pages
mainLogin = Login(700, 500, 'Main')
adminLogin = Login(700, 500, 'Admin')
studentLogin = Login(700, 500, 'Student')
parentLogin = Login(700, 500, 'Parent')
## Creates a new instance of the Login class for the forgot password, quit confirmation and create account pages
forgotPassword = Login(700, 500, 'ForgotPassword')
createAccount = Login(700, 800, 'CreateAccount')
newAccount = Login(600, 400, 'SuccessfulAccount')

quitConfirmation = Interface(500, 300)
mainMenu = Interface(1000, 700)
settings = Interface(800, 500)
reviewUser = Interface(1020, 500)
saveNewQuiz = Interface(500, 300)
viewQuiz = Interface(1300, 700)

mainLogin.mainLoginPage(mainLogin.titleFont, mainLogin.buttonFont, mainLogin.defaultFont)
#mainMenu.adminMainMenuPage('hemanseego01', Login.titleFont, Login.buttonFont, Login.defaultFont)
#mainMenu.createQuiz('hemanseego01', Login.titleFont, Login.defaultFont, Login.buttonFont)
#mainMenu.viewQuizzes('hemanseego01', Login.titleFont, Login.defaultFont, Login.buttonFont)
#mainMenu.playQuiz('hemanseego01', Login.titleFont, Login.defaultFont, Login.buttonFont)
#mainMenu.viewClasses('hemanseego01', Login.titleFont, Login.defaultFont, Login.buttonFont)

#mainMenu.studentMainMenuPage('sampinch02', Login.titleFont, Login.buttonFont, Login.defaultFont)
#mainMenu.parentMainMenuPage('mattbumpus03', Login.titleFont, Login.buttonFont, Login.defaultFont)


closingConnection.closeConnection()

    

    
