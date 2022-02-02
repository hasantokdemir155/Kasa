import locale
from ssql import *
import pyodbc
from datetime import date
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from ksa import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator



class ekrn():
    i=0
    j=0
    t=0
    e=0
    im=0
    def __init__(self):
        
       
        self.uyg=QApplication(sys.argv)
        self.penAna=QMainWindow()
        self.ui=Ui_MainWindow()

        self.ui.setupUi(self.penAna)
        self.penAna.show()

        
        self.conn = pyodbc.connect(
           "Driver={SQL Server Native Client 11.0};"
           "Server=HASAN\SQLEXPRESS1;"
           "Database=verx;"
           "Trusted_Connection=yes;"
                )

        self.crs=self.conn.cursor()
       
        locale.setlocale(locale.LC_ALL,"tr_TR.UTF-8")

        ax=str(date.today())+'ksx'        
        kmt1x=self.conn.cursor()
        print('bbbbbbbb')
        kmt1x.execute('select ksakod from ksacal where  ksakod = ?',ax)
        kaytlarx=kmt1x.fetchall()

        if kaytlarx == [] :
           
            self.kmt1=self.conn.cursor()
            
            self.kmt1.execute('select carad from carler')
            self.kaytlar=self.kmt1.fetchall()

           
           
            self.ui.pushButton.clicked.connect(self.odmeaktar)
            self.ui.pushButton_2.clicked.connect(self.tahsltaktar)
            self.ui.pushButton_3.clicked.connect(self.kaytaktar)

            self.ui.pushButton_4.clicked.connect(self.islemsl)
            self.ui.pushButton_5.clicked.connect(self.islemsl2)
            
      
            print('kayıt yok')

        else:

            print('kayıt var')   


        
        self.m=0
        

        

               
        self.kmt1x=self.conn.cursor()
        self.kmt1x.execute('select ksakod from ksacal group by ksakod')
        self.kaytlarx=self.kmt1x.fetchall()
        
        print(self.kaytlarx)
        for self.k in self.kaytlarx:
            
            self.str1=self.kaytlarx[self.m][0].split("k")
            print(self.str1)
            
            if self.str1[1][2] == 'o':
                    self.ui.comboBox_2.addItem(self.str1[0])
            #self.ui.comboBox_2.addItem(self.kaytlarx[self.m][0])
            self.m= self.m + 1
        self.m=0    

        for self.k in self.kaytlar:
            self.ui.comboBox.addItem(str(self.kaytlar[self.m][0]))
            
            self.m= self.m + 1
            self.ui.tableWidget.setRowCount(99)
            self.item = QtWidgets.QTableWidgetItem()




        
            

            
        self.ui.pushButton_6.clicked.connect(self.islemsl3)
        self.ui.label_2.setText(str(date.today())+'ksx')

        self.penAna.show()

    def islemsl3(self,w):
        
        self.bx=self.ui.comboBox_2.currentText()
        
        self.kmt1xm=self.conn.cursor()
        
        self.kmt1xm.execute('select * from ksacal where ksakod = ? ',self.bx+'ksxo')

        self.kaytlarx=self.kmt1xm.fetchall()

        self.kmt1xm.execute('select * from ksacal where ksakod = ? ',self.bx+'ksxt')
              
        self.kaytlarm=self.kmt1xm.fetchall()
        
        self.i=0
        self.ui.tableWidget_3.clearContents()

        for self.w in self.kaytlarx:
          
            self.ui.tableWidget_3.setItem(self.i,0,QTableWidgetItem(self.w[1]))
            self.ui.tableWidget_3.setItem(self.i,1,QTableWidgetItem(str(self.w[2])))
            self.i = self.i + 1
            
        self.i=0
        
        for self.x in self.kaytlarm:    
            self.ui.tableWidget_3.setItem(self.i,3,QTableWidgetItem(self.x[1]))
            self.ui.tableWidget_3.setItem(self.i,4,QTableWidgetItem(str(self.x[2])))

            self.i = self.i + 1
            
       
        
    def odmeaktar(self,i):
         print('essseee')
         #╣global i,j
          
       
         self.a= str(date.today())+'ksx'
           
         self.b=self.ui.comboBox.currentText()
         print(self.b)
         print(self.ui.lineEdit_onlyint.text())
         self.c=self.ui.lineEdit_onlyint.text()
         print('rrrr')
         print(self.c)
         self.ui.tableWidget.setItem(self.im,0,QTableWidgetItem(str(self.b)))
    #    print(ui.tableWidget.item(i,0).text())
         self.ui.tableWidget.setItem(self.im,1,QTableWidgetItem(str(self.c)))
         self.ui.tableWidget.item(self.im,0).setBackground(QtGui.QColor(125,77,255))
         self.ui.tableWidget.item(self.im,1).setBackground(QtGui.QColor(125,77,255))
        
         self.im=self.im+1

        

    def tahsltaktar(self,j):
         #═global i,j,kasnet
         self.a= str(date.today())+'ksx'
   
         self.b=self.ui.comboBox.currentText()
         self.c=self.ui.lineEdit_onlyint.text()

         self.ui.tableWidget_2.setItem(self.j,0,QTableWidgetItem(str(self.b)))
         self.ui.tableWidget_2.setItem(self.j,1,QTableWidgetItem(str(self.c)))
         self.ui.tableWidget_2.item(self.j,0).setBackground(QtGui.QColor(77,208,225))
         self.ui.tableWidget_2.item(self.j,1).setBackground(QtGui.QColor(77,208,225))
        
         self.j=self.j+1

        
    def kaytaktar(self):
         if self.im !=0 : 
             for self.s  in range(0,self.im-1):
                print(self.s)
                self.d=str(date.today())+'ksx'+'o'
            
                self.e=self.ui.tableWidget.item(self.s,0).text()
                self.f=int(self.ui.tableWidget.item(self.s,1).text())
                self.g='odme'
                self.h=str(date.today())
                print(self.d,self.e,self.f,self.g,self.h)
            #Lif  self.e != ' '  :

                if self.e != '':

                   self.crs.execute("insert into [ksacal] (ksakod,cariad,tutar,odtr,tarh) values(?,?,?,?,?)",(self.d,self.e,self.f,self.g,self.h))

            
           
         print('cmmmm') 

         print(self.j)
         
         #¬if self.ui.tableWidget_2.item(0,0).text() != '':
         if self.j !=0 :    
             for self.t  in(0,self.j-1):
             
           
                self.d1=str(date.today())+'ksx'+'t'
                self.e1=self.ui.tableWidget_2.item(self.t,0).text()
                self.f1=int(self.ui.tableWidget_2.item(self.t,1).text())
                self.g1='tahs'
                self.h1=str(date.today())    
        
                if self.e1 != '':
                    self.crs.execute("insert into [ksacal] (ksakod,cariad,tutar,odtr,tarh) values(?,?,?,?,?)",(self.d1,self.e1,self.f1,self.g1,self.h1))
         
     
    #QTableWidget:item:selected{ background-color: red }
         
         
   
         self.conn.commit()
        
         self.ui.tableWidget.clearContents()
    
         self.ui.tableWidget_2.clearContents()

         self.im =0
         self.j = 0




        
    def islemsl(self):

        self.cm=self.ui.tableWidget.selectedItems()
               
        #for se in self.cm :
         #   print(se.text())
            
        
        self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())
        self.im=self.im-1

        
    def islemsl2(self):
        self.ui.tableWidget_2.removeRow(self.ui.tableWidget_2.currentRow())
        self.j=self.j-1


gn=ekrn()


gn  



#gn=ekrn()

#ekrn   
