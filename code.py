from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import * 
import sys
import subprocess

class Application(QtGui.QMainWindow):
	def __init__(self, *args):
		#Creates the main window with the menu bar and buttons``
		QtGui.QMainWindow.__init__(self, *args)
		self.UI()

	def UI(self):
		self.setWindowTitle("Volatility 2.3.1 GUI")		
		self.resize(640,480)
		#self.menuBar_()
		self.Buttons()
		self.text_output = QtGui.QTextEdit(self)
		#self.text_output.move(300,200)
		#self.setCentralWidget(self.text_output)
		self.text_output.setGeometry(10,100,500,370)
		#self.setCentralWidget(self.text_output)

		#Creates the menubar
		self.File = self.menuBar().addMenu("File")
		self.openFile = QtGui.QAction("Open File", self, triggered=self.chooseFile)
		self.File.addAction(self.openFile)

		#This is where the a person can input a command and where the command will appear from all the options that the user selected
		self.linetext = QtGui.QLineEdit(self)
		self.linetext.setGeometry(10,60,500,30)
		

	def chooseFile(self):
		chooseFile = QtGui.QFileDialog.getOpenFileName(self, "Choose the image")		
		#test = subprocess.call(["echo", chooseFile])
		self.linetext.insert(" -f ")
		file_Selected = self.linetext.insert(chooseFile)
		

	def Buttons(self):
		button1 = QtGui.QPushButton('Run', self)
		button1.move(510,60)
		button1.clicked.connect(self.runCommand)
		
		profilesPush = QtGui.QPushButton('Profiles', self)
		profilesPush.setText("Profiles")
		profilesPush.clicked.connect(self.findProfiles)
		profilesPush.move(200,25)

		msgBox = QtGui.QMessageBox()
		msgBox.setText("Select the plugin")

		pluginsbutton = QtGui.QPushButton('Plugins', self)
		pluginsbutton.move(50,25)
		pluginsbutton.clicked.connect(self.findPlugins)

	def findPlugins(self):
		#Creates the popup for the plugins
		pluginPop = QtGui.QDialog()
		pluginList = QtGui.QButtonGroup() 
		pluginPop.setWindowTitle("Plugin Selection")
		
		
		label3 = QtGui.QLabel("Image Identification", pluginPop)
		label4 = QtGui.QLabel("Process Listings",pluginPop)
		label5 = QtGui.QLabel("Process Information",pluginPop)
		label6 = QtGui.QLabel ("PE File Extraction",pluginPop)
		label7 = QtGui.QLabel("Injected Code",pluginPop)		
	
		checkbox_1 = QtGui.QCheckBox("imageinfo", pluginPop)
		checkbox_2 = QtGui.QCheckBox("kdbgscan", pluginPop)
		checkbox_3 = QtGui.QCheckBox("pslist", pluginPop)
		checkbox4 = QtGui.QCheckBox("VistaSP1x86", popUp)
		checkbox5 = QtGui.QCheckBox("VistaSP2x64", popUp)
		checkbox6 = QtGui.QCheckBox("Win07x86", popUp)
		checkbox7 = QtGui.QCheckBox("Win07x64", popUp)
		checkbox8 = QtGui.QCheckBox("Win10x86", popUp)
		checkbox9 = QtGui.QCheckBox("Win10x64", popUp)
		checkbox10 = QtGui.QCheckBox("CentOSx64", popUp)



		checkbox_1.move(0,20)
		pluginList.addButton(checkbox_1)
		checkbox_1.show()

		checkbox_2.move(0,40)
		pluginList.addButton(checkbox_2)
		checkbox_2.show()

		label4.move(0,60)
		label4.setFont(QtGui.QFont("Times",weight = QtGui.QFont.Bold))
		label4.show()
		
		checkbox_3.move(0,80)
		pluginList.addButton(checkbox_3)
		checkbox_3.show()
		
		checkbox4.move(0,80)
		buttonList.addButton(checkbox4)
		checkbox4.show()

		checkbox5.move(0,100)
		buttonList.addButton(checkbox5)
		checkbox5.show()
		
		checkbox6.move(0,120)
		buttonList.addButton(checkbox6)
		checkbox6.show()

		checkbox7.move(0,140)
		buttonList.addButton(checkbox7)
		checkbox7.show()
		
		checkbox8.move(0,160)
		buttonList.addButton(checkbox8)
		checkbox8.show()
		
		checkbox9.move(0,180)
		buttonList.addButton(checkbox9)
		checkbox9.show()
			
		label2.move(0,200)
		label2.setFont(QtGui.QFont("Times",weight = QtGui.QFont.Bold))
		label2.show()

		checkbox10.move(0,220)
		buttonList.addButton(checkbox10)
		checkbox10.show()
		

	def profileInfo(self, button):
		text = self.linetext.text()
		length_initial = text.length()
		self.linetext.insert(" --profile=") 
		self.linetext.insert(button.text())
		thing = " --profile="
		
		#length_initial = text.length()
		counter = 0
		#Get length of the string and get length of the both inserts. Remove them and input the new insert.
		if thing in text:
			hi = text.count(thing)
			if hi >= 1:
				length_e = self.linetext.text()
				length_entire = length_e.length()
				length_cut = length_entire - length_initial
				#print("length_entire: ", length_entire)	
				#print("length_initial: ", length_initial)			
				#print("length_cut: ",length_cut)
				real = length_cut * 2
				#self.linetext.cursorBackward(real, length_cut)
				while( counter < real):
					self.linetext.backspace()
					counter = counter + 1		
		
	


	
	def runCommand(self, button):
		thing1 = str(self.linetext.text())
		print thing1
		#print("volatility"," -f ", thing1)
		Kappa = subprocess.check_output(["volatility " + thing1], shell=True)
		self.text_output.setText(Kappa)
		return Kappa

def main():
	app = QtGui.QApplication(sys.argv)
	win = Application()
	win.show()
	app.exec_()	


if __name__ == "__main__":
	main()
