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


		label3.move(0,0)
		label3.setFont(QtGui.QFont("Times",weight = QtGui.QFont.Bold))
		label3.show()
		

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
