#!/usr/bin/python3

class MyDoc:

    @staticmethod
    def Do_Start():
        print("Content-Type: text/html; charset=UTF-8\n")
        print("<!DOCTYPE html>")
        print ("<html>")
        print ("<head>")
        print ("<meta charset='utf-8'>")
        print ('<link rel="stylesheet" type="text/css" href="../../styles.css">')
        print ("</head>")
        print ("<body>")
        print ("<body>")
        print ("<nav>")
        print ("<ul>")
        print ('<li><a href="front.py">Home</a></li>')
        print ('<li><a href="enter.py">Enter</a></li>')
        print ('<li><a href="view.py">View</a></li>')
        print ('<li><a href="edit.py">Edit</a></li>')
        print ("</ul>")
        print ("</nav>")

    @staticmethod
    def Do_End():
        print("</body>")
        print("</html>")


