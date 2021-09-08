from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import *
from affichage import *
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
        Dialog.resize(824, 486)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 0, 3, 1, 1)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("securite.db")
        self.db.open()
        self.model = QSqlTableModel()
        self.model.setTable("trois")
        self.model.select()
        self.model.setHeaderData(1, QtCore.Qt.Horizontal,"Prenom")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal,"Nom")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal,"Batiment")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal,"Etage")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal,"Motif")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal,"Date et Heure")
        self.tableView.setModel(self.model)
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 4)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        QtCore.QObject.connect(self.pushButton_4,QtCore.SIGNAL("clicked()"),self.rechercher)
        QtCore.QObject.connect(self.pushButton_5,QtCore.SIGNAL("clicked()"),self.suppression)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.voir_bilan)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "GESTION VISITEURS", None))
        self.label.setText(_translate("Dialog", "ENREGISTREMENTS", None))
        self.pushButton_4.setText(_translate("Dialog", "Trier", None))
        self.pushButton_5.setText(_translate("Dialog", "Supprimer", None))
        self.pushButton.setText(_translate("Dialog", "Details", None))

    def rechercher(self):
        self.model.setFilter("prenom like '"+self.lineEdit.text()+"%'")

    def suppression(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.model.submitAll()

    def voir_bilan(self):
        self.Dialog1 = QtGui.QDialog()
        ui = Ui_Dialog1()
        ui.setupUi(self.Dialog1)
        self.Dialog1.show()
        self.Dialog1.exec_()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
