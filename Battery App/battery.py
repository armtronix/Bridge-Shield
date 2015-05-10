import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import math
import time, threading
from time import sleep
from i2clibraries import i2c_attiny85_adc
from time import *
from PySide import QtGui
from PySide import QtCore
from threading import Timer
from datetime import datetime
from time import *
import time

attiny85adc= i2c_attiny85_adc.i2c_attiny85_adc(1)

class MainWindow(QtGui.QMainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()

		self.progressBar =QtGui.QProgressBar(self)
		self.progressBar.setGeometry(10,10,300,25)
		
		self.lblstatus=QtGui.QLabel(self)
		self.lblstatus.setGeometry(80,30,140,25)	
		#self.status.addPermanentWidget(self.progressBar)



		
		self.buttonstart = QtGui.QPushButton(self)
		self.buttonstart.setText("Observe")
		self.buttonstart.move(90,60)
		self.buttonstart.clicked.connect(self.periodical_call)
		
		self.initUI()
		self.thread = QtCore.QThread()
		self.worker = Worker()
		self.worker.moveToThread(self.thread)
		self.thread.started.connect(self.worker.loop)
		self.thread.start()

	def initUI(self):               
        
		self.resize(250, 150)
		self.center()
		self.statusBar()
		self.setWindowTitle('Bridge Board Battery Monitoring')    
		self.show()
		
	def closeEvent(self, x):
		self.worker.stop()
		self.thread.quit()
		self.thread.wait()

	def periodical_call(self):
		self.worker.do_stuff("main window") # this works
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.do_stuff) # this also works
		self.timer.start(300)

	def do_stuff(self):
		dumpval1=((attiny85adc.getAdc02())*0.094)
		round(dumpval1,2)
		print (str(dumpval1))
		if(attiny85adc.getAdc03()<500):
			
			self.lblstatus.setText("<b><font color=red size=3>Battery Charging</font></b>")
		else: 
			#self.txtattiny85adc02.setText("On Battery")
			self.lblstatus.setText("<b><font color=red size=3>On Battery</font></b>")

		#self.txtattiny85adc03.setText(str(dumpval1))
		self.progressBar.setValue(dumpval1)
		#self.txtattiny85adc02.setText(str(attiny85adc.getAdc03()))
		self.worker.do_stuff("timer main window")

	def center(self):
        
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())



class Worker(QtCore.QObject):
	def do_stuff_timer(self):
		do_stuff("timer worker")

	def do_stuff(self, origin):
		self.origin = origin
		self.wait.wakeOne()

	def stop(self):
		self._exit = True
		self.wait.wakeAll()

	def loop(self):
		self.wait = QtCore.QWaitCondition()
		self.mutex = QtCore.QMutex()
		self._exit = False
		while not self._exit:
			self.wait.wait(self.mutex)
			print ("loop from %s" % (self.origin,))

			self.timer = QtCore.QTimer()
			self.timer.setSingleShot(True)
			self.timer.timeout.connect(self.do_stuff_timer)
			self.timer.start(1000) # <---- this doesn't work


	

def main():
	app = QtGui.QApplication(sys.argv)
	ex=MainWindow()
	ex.resize(320,100)
	sys.exit(app.exec_())	



if __name__ == '__main__':
	main()


