from PyQt4 import QtCore, QtGui
import sqlite3
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName(_fromUtf8("Dialog"))
        Dialog1.resize(400, 312)
        self.gridLayout = QtGui.QGridLayout(Dialog1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textBrowser = QtGui.QTextBrowser(Dialog1)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 3)
        self.lineEdit = QtGui.QLineEdit(Dialog1)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(Dialog1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Dialog1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.figure)
        QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL('clicked()'),self.figure2)

    def retranslateUi(self, Dialog1):
        Dialog1.setWindowTitle(_translate("Dialog", "GESTION VISITEURS", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">MOYENNE DES ENTREES </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">PAR JOUR DURANT LES 5 SEMAINES</span></p></body></html>", None))
        self.pushButton.setText(_translate("Dialog", "Diagramme", None))
        self.pushButton_2.setText(_translate("Dialog", "Tendances", None))
        self.requete()

        self.diagramme_a()
        self.diagramme_b()
        self.diagramme_c()

        self.barmVISITE()
        self.barmCOURRIER()
        self.barmCAISSE()
        self.barmBON()
        self.barmREUNION()
        self.barmCOURSIER()
        self.barmRDV()
        self.barmFACTURE()
        self.barmLIVRAISON()
        self.barmAUTRES()

        self.etagA1()
        self.etagA2()
        self.etagA3()
        self.etagA4()
        self.etagA5()
        self.etagA6()
        self.etagA7()
        self.etagA8()
        self.etagB1()
        self.etagB2()
        self.etagB3()
        self.etagB4()
        self.etagB5()
        self.etagB6()
        self.etagB7()
        self.etagB8()
        self.etagC1()
        self.etagC2()
        self.etagC3()
        self.etagC4()
        self.etagC5()
        self.etagC6()
        self.etagC7()
        self.etagC8()
        self.journee = self.lineEdit.text()

    def requete(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(nom) from onze")  
        rows = liste.fetchall()  
        if rows:
            for p in rows:
                self.textBrowser.append(str(''.join(map(str,p))))
        c.close()

    def diagramme_a(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(batiment) from quatre where batiment='a'")
        rows = liste.fetchall()       
        if rows:
            for x in rows:
                self.a = int(''.join(map(str,x))) 
        c.close()

    def diagramme_b(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(batiment) from quatre where batiment='b'")
        rows = liste.fetchall()       
        if rows:
            for y in rows:
                self.b = int(''.join(map(str,y)))
        c.close()

    def diagramme_c(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(batiment) from quatre where batiment='c'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.c = int(''.join(map(str,z)))
        c.close()

    def figure(self):
        import matplotlib.pyplot as plt
        name = ['Batiment A','Batiment B','Batiment C']
        data = [self.a,self.b,self.c]

        plt.figure('GESTION VISITEURS')
        explode = (0.1,0.1,0.1)
        plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
        #plt.axis('equal')
        plt.show()

    def barmVISITE(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(motif) from quatre where motif='visite perso'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.visite = int(''.join(map(str,z)))
        c.close()

    def barmCOURRIER(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(motif) from quatre where motif='courrier'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.courrier = int(''.join(map(str,z)))
        c.close()

    def barmCAISSE(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(motif) from quatre where motif='caisse'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.caisse = int(''.join(map(str,z)))
        c.close()

    def barmBON(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(motif) from quatre where motif='bon de commande'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.bon = int(''.join(map(str,z)))
        c.close()

    def barmREUNION(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(motif) from quatre where motif='reunion'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.reunion = int(''.join(map(str,z)))
        c.close()

    def barmCOURSIER(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(motif) from quatre where motif='coursier'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.coursier = int(''.join(map(str,z)))
        c.close()

    def barmRDV(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(motif) from quatre where motif='rendez-vous'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.rdv = int(''.join(map(str,z)))
        c.close()

    def barmFACTURE(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(motif) from quatre where motif='depot facture'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.facture = int(''.join(map(str,z)))
        c.close()

    def barmLIVRAISON(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(motif) from quatre where motif='livraison'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.livraison  = int(''.join(map(str,z)))
        c.close()

    def barmAUTRES(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(motif) from quatre where motif='autres'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.autres = int(''.join(map(str,z)))
        c.close()


    def etagA1(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=1 and batiment='a'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etA1 = int(''.join(map(str,z)))
        c.close()

    def etagA2(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=2 and batiment='a'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etA2 = int(''.join(map(str,z)))
        c.close()

    def etagA3(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=3 and batiment='a'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etA3 = int(''.join(map(str,z)))
        c.close()

    def etagA4(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=4 and batiment='a'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etA4 = int(''.join(map(str,z)))
        c.close()

    def etagA5(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=5 and batiment='a'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etA5 = int(''.join(map(str,z)))
        c.close()

    def etagA6(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=6 and batiment='a'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etA6 = int(''.join(map(str,z)))
        c.close()

    def etagA7(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=7 and batiment='a'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etA7 = int(''.join(map(str,z)))
        c.close()

    def etagA8(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=8 and batiment='a'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etA8 = int(''.join(map(str,z)))
        c.close()

    def etagB1(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=1 and batiment='b'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etB1 = int(''.join(map(str,z)))
        c.close()

    def etagB2(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=2 and batiment='b'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etB2 = int(''.join(map(str,z)))
        c.close()

    def etagB3(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=3 and batiment='b'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etB3 = int(''.join(map(str,z)))
        c.close()

    def etagB4(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=4 and batiment='b'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etB4 = int(''.join(map(str,z)))
        c.close()

    def etagB5(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=5 and batiment='b'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etB5 = int(''.join(map(str,z)))
        c.close()

    def etagB6(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=7 and batiment='b'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etB6 = int(''.join(map(str,z)))
        c.close()

    def etagB7(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=7 and batiment='b'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etB7 = int(''.join(map(str,z)))
        c.close()

    def etagB8(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=8 and batiment='b'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etB8 = int(''.join(map(str,z)))
        c.close()

    def etagC1(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=1 and batiment='c'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etC1 = int(''.join(map(str,z)))
        c.close()

    def etagC2(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=2 and batiment='c'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etC2 = int(''.join(map(str,z)))
        c.close()

    def etagC3(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=3 and batiment='c'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etC3 = int(''.join(map(str,z)))
        c.close()

    def etagC4(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=4 and batiment='c'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etC4 = int(''.join(map(str,z)))
        c.close()

    def etagC5(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=5 and batiment='c'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etC5 = int(''.join(map(str,z)))
        c.close()

    def etagC6(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=6 and batiment='c'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etC6 = int(''.join(map(str,z)))
        c.close()

    def etagC7(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=7 and batiment='c'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etC7 = int(''.join(map(str,z)))
        c.close()

    def etagC8(self):
        self.conn = sqlite3.connect("securite.db")
        c = self.conn.cursor()
        liste = c.execute("SELECT count(etage) from quatre where etage=8 and batiment='c'")
        rows = liste.fetchall()       
        if rows:
            for z in rows:
                self.etC8 = int(''.join(map(str,z)))
        c.close()

    def figure2(self):
        from matplotlib.ticker import FuncFormatter
        import matplotlib.pyplot as pyplot
        import numpy as np

        x =     np.arange(10)
        motif = [self.visite,self.courrier,self.caisse,self.bon,self.reunion,self.coursier,self.rdv,self.facture,self.livraison,self.autres]

        pyplot.figure('GESTION VISITEURS')
        pyplot.subplot(2, 1, 1)
        pyplot.bar(x +0.5, motif, color = '#336600')
        pyplot.xticks(x + 1, ('VIST', 'COUR', 'CAISS', 'BON','REUN','CRSE','RDV','FACT','LIVR','AUTRS'))
        pyplot.title('MOTIF')

        ############ BATIMENT A ############
        x1 =     np.arange(8)
        etageA = [self.etA1,self.etA2,self.etA3,self.etA4,self.etA5,self.etA6,self.etA7,self.etA8]
        
        pyplot.subplot(2, 3, 4)
        pyplot.bar(x1 + 0.5, etageA, color = '#99CC33')
        pyplot.xticks(x1 + 1, ('E1', 'E2', 'E3', 'E4','E5','E6','E7','E8'))
        pyplot.title('BATIMENT A')

        ############ BATIMENT B ############
        x2 =     np.arange(8)
        etageB = [self.etB1,self.etB2,self.etB3,self.etB4,self.etB5,self.etB6,self.etB7,self.etB8]

        pyplot.subplot(2, 3, 5)
        pyplot.bar(x2 + 0.5, etageB, color = '#99CC66')
        pyplot.xticks(x2 + 1, ('E1', 'E2', 'E3', 'E4','E5','E6','E7','E8'))
        pyplot.title('BATIMENT B')
        ############ BATIMENT C ############

        x3 =     np.arange(8)
        etageC = [self.etC1,self.etC2,self.etC3,self.etC4,self.etC5,self.etC6,self.etC7,self.etC8]

        pyplot.subplot(2, 3, 6)
        pyplot.bar(x3 + 0.5, etageC, color = '#CCFF99')
        pyplot.xticks(x3 + 1, ('E1', 'E2', 'E3', 'E4','E5','E6','E7','E8'))
        pyplot.title('BATIMENT C')

        pyplot.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog1 = QtGui.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec_())
