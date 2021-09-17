from PyQt5.QtWidgets import *
import sys
import HSPMKN
import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Pencere(QMainWindow, HSPMKN.Ui_hesapMakinas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()
        
        self.sayi1.clicked.connect(self.tikla1)
        self.sayi2.clicked.connect(self.tikla2)
        self.sayi3.clicked.connect(self.tikla3)
        self.sayi4.clicked.connect(self.tikla4)
        self.sayi5.clicked.connect(self.tikla5)
        self.sayi6.clicked.connect(self.tikla6)
        self.sayi7.clicked.connect(self.tikla7)
        self.sayi8.clicked.connect(self.tikla8)
        self.sayi9.clicked.connect(self.tikla9)
        self.sifir.clicked.connect(self.tikla0)
        self.ciftSifir.clicked.connect(self.ciftsifirTikla)
        self.carpi.clicked.connect(self.carpiTikla)
        self.arti.clicked.connect(self.artiTikla)
        self.eksi.clicked.connect(self.eksiTikla)
        self.karekok.clicked.connect(self.karekokTikla)
        self.ustlu.clicked.connect(self.ustluTikla)
        self.bolme.clicked.connect(self.bolmeTikla)
        self.esittir.clicked.connect(self.esittirTikla)
        self.temizle.clicked.connect(self.temizleTikla)





    def tikla1(self):
        yazi = self.ekran.text() + "1"
        self.ekran.setText(yazi)
    
    def tikla2(self):
        yazi = self.ekran.text() + "2"
        self.ekran.setText(yazi)

    def tikla3(self):
        yazi = self.ekran.text() + "3"
        self.ekran.setText(yazi)

    def tikla4(self):
        yazi = self.ekran.text() + "4"
        self.ekran.setText(yazi)

    def tikla5(self):
        yazi = self.ekran.text() + "5"
        self.ekran.setText(yazi)

    def tikla6(self):
        yazi = self.ekran.text() + "6"
        self.ekran.setText(yazi)

    def tikla7(self):
        yazi = self.ekran.text() + "7"
        self.ekran.setText(yazi)

    def tikla8(self):
        yazi = self.ekran.text() + "8"
        self.ekran.setText(yazi)
    
    def tikla9(self):
        yazi = self.ekran.text() + "9"
        self.ekran.setText(yazi)

    def tikla0(self):
        yazi = self.ekran.text() + "0"
        self.ekran.setText(yazi)

    def ciftsifirTikla(self):
        yazi = self.ekran.text() + "00"
        self.ekran.setText(yazi)

    def carpiTikla(self):
        yazi = self.ekran.text() + "*"
        self.ekran.setText(yazi)

    def artiTikla(self):
        yazi = self.ekran.text() + "+"
        self.ekran.setText(yazi)
    
    def eksiTikla(self):
        yazi = self.ekran.text() + "-"
        self.ekran.setText(yazi)

    def karekokTikla(self):
        try:
            self.ekran.setText(self.ekran.text())
            txt = self.ekran.text()
            integer = int(txt)   
            rp = int(math.sqrt(abs(integer)))     
        
        
            ans = eval("{}*{}".format(str(rp),str(rp)))
        
            if str(ans) == self.ekran.text():
                self.ekran.setText(str(rp)+"√2") 
            
            
            else:         
                self.ekran.setText("Bu Sayının Karekökü Yoktur")
            
        except ValueError:
            self.ekran.setText("Geçersiz İşlem")

    
    def ustluTikla(self):
        yazi = self.ekran.text() + "**"
        self.ekran.setText(yazi)



    def bolmeTikla(self):
        yazi = self.ekran.text() + "/"
        self.ekran.setText(yazi)

    def esittirTikla(self):
        # get the label text 
        equation = self.ekran.text() 
  
        try: 
            # getting the ans 
            ans = eval(equation) 
  
            # setting text to the label 
            self.ekran.setText(str(ans)) 
  
        except: 
            # setting text to the label 
            self.ekran.setText("Geçersiz İşlem")
            
        
        self.ekran.setText(self.ekran.text())

    
    def temizleTikla(self):
        text = self.ekran.text()
        print(text[:len(text)-1]) 
        self.ekran.setText(text[:len(text)-1])
    







app = QApplication(sys.argv)
pencere = Pencere()
pencere.setWindowTitle("Hesap Makinesi")
pencere.show()
sys.exit(app.exec_())
# İyi eğlenceler
