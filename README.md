
# food-menu spreadsheet

## Link to the app on heroku
[food-menu-terminal](https://food-menu-spreadsheet.herokuapp.com/)

## Purpose
To provide a way of interactive with google sheets through the terminal.

## Features
The app is based on an italian pizza takeaway-menu I found on google.
It is connected to the google sheets API and let's the user input desired
food from the menu, which updates the google sheet provided [here](https://docs.google.com/spreadsheets/d/1ZMafE3iASF4JajNNqcCspRB4JMgc5zVP0gE1stCrSDc/edit#gid=1597246693).

## Development
For development of this app, I used code institutes mock terminal (which they kindly made available for this project).
The reason for this is simplicity: the user won't therefore have to download any files, but can instead use
the python program directly though the browser.

The main thing to do was to figure out a way get the sheets from google.
This was done installing and importing the gspread module (for example: "GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)").

It's a straight forward app. User types in the terminal and the sheet updates with price and product that
the user chose.


![Screenshot of the app](https://github.com/jonny-bjornhager/food-menu/blob/main/img/screencap.png?raw=true)



## Learning outcomes
Using python for getting and showing userful information to the user.
I had a blast doing this!
