from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import *
from traffic import *
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(660, 454)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        #self.radioButton = QtGui.QRadioButton(Dialog)
        #self.radioButton.setObjectName(_fromUtf8("radioButton"))
        #self.gridLayout.addWidget(self.radioButton, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),self.voir_enregistrement)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.voir_bilan)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Liste des enregistrements", None))
        self.pushButton_2.setText(_translate("Dialog", "Voir", None))
        self.pushButton.setText(_translate("Dialog", "Bilan journalier", None))
        #self.radioButton.setText(_translate("Dialog", "Sorti", None))


    def voir_enregistrement(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("securite.db")
        self.db.open()
        self.model = QSqlTableModel()
        self.model.setTable("onze")
        self.model.select()
        self.model.setHeaderData(1, QtCore.Qt.Horizontal,"Prenom")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal,"Nom")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal,"Batiment")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal,"Etage")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal,"Motif")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal,"Date et Heure")
        self.tableView.setModel(self.model)
    
    def voir_bilan(self):
        self.Dialog1 = QtGui.QDialog()
        ui = Ui_Dialog1()
        ui.setupUi(self.Dialog1)
        self.Dialog1.show()
        self.Dialog1.exec_()

'''
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
'''
