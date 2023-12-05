import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
import random

#These two functions are called from clicked and from checkplus functions
#From clicked these funcions are called to get values of correct and incorrect answers, so to avoid changes variable aux receives 0
#In case of being called from checkplus, aux gets value of 1 to add to the total number of correct or incorrect answers
def correctfunc(aux, correct):
	correct = correct + aux
	return correct
	
def incorrectfunc(aux, incorrect):
	incorrect = incorrect + aux
	return incorrect



def checkplus(win, result, text, pluswin, correct, incorrect):
	answer = text.get_text()
	pluswin.close()
	
	if (int(answer) == int(result)):
		print("correct")
		correct = correctfunc(1, correct)
		
	else:
		print("incorrect")
		incorrect = incorrectfunc(1, incorrect)
		

	clicked(win, correct, incorrect)
		
	
	
	

def clicked(win, correct, incorrect):
	win.close()
	#randint in this case generates a random number from 1 to 100 to a value of num and num2. It can be changed later to other numbers
	num = random.randint(1,100)
	num2 = random.randint(1,100)
	
	var = random.randint(1, 2)	
	
	#var decides if the question will be to sum numbers or rest numbers
	if (var == 1):
		result = num + num2
		sign = '+'
		
	else:
		result = num - num2
		sign = '-'
		
	
	pluswin= Gtk.ApplicationWindow(application=app)
	

	box1 = Gtk.Box()
	box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	
	correct = correctfunc(0, correct)
	incorrect = incorrectfunc(0, incorrect)
	
	
	text = Gtk.Entry()	#Text here should be an integer, otherwise it throws an error and exits the programm
	label = Gtk.Label(label="How much will be " + str(num) + " " + sign + " " + str(num2) + " ?")
	button = Gtk.Button(label="Check")
	label2 = Gtk.Label(label="Correct: " + str(correct) + " Incorrect: " + str(incorrect))
		
	box1.append(text)
	box1.append(label)
	box1.append(button)
	box1.append(label2)
	    
	pluswin.set_child(box1)
	pluswin.present()
	
	button.connect('clicked', lambda x: checkplus(win, result, text, pluswin, correct, incorrect))

def on_activate(app):
	win = Gtk.ApplicationWindow(application=app)
	#win.set_default_size(400, 300) this line if used can change the size of the window

	#Box Layout is probably the easiest to use, it can be set to be VERTICAL or HORIZONTAL
	box1 = Gtk.Box()
	box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

	label = Gtk.Label(label="This is mathematics game")
	label2 = Gtk.Label(label="Do you want to start this game?")
	button = Gtk.Button(label="Start")

	box1.append(label)
	box1.append(label2)
	box1.append(button)
	    
	win.set_child(box1)
	win.present()
	
	button.connect('clicked', lambda x: clicked(win, 0, 0))	#Sets an action for the button to go to another function
	#Passes win as main window to close it later and and two zeroes to inicialize correct and incorrect attempts
	

app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
