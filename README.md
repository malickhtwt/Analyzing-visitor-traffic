# Analyzing-visitor-traffic

Application created for Sonatel which became Orange senegal. It allowed them to control visitors coming in and out the site.

I developed this software for their security department in order to analyze the visitors traffic based on the floor, 

the building name and the reason of their visit. We gathered data for several months from visitors to help us 

make decisions such as restricting access to certain floor, provide more security, make predictions and 

much more.



LIBRARIES USED FOR THIS PROJECT:

==> PyQt4 (will need to install sip for this version)

==> SQLite3

==> Numpy

==> Matplotlib


<img width="702" alt="Screen Shot 2021-11-15 at 8 01 24 PM" src="https://user-images.githubusercontent.com/90251223/141883950-0e41f20a-28f5-47f3-93d3-c98306dc0ae1.png">

def enregistrement_sqlite(self):
  self.db = QSqlDatabase.addDatabase("QSQLITE")
  self.db.setDatabaseName("securite.db")
  self.db.open()
  self.model = QSqlTableModel()
  self.model.setTable("ving")
  query = QSqlQuery()
  query.prepare("INSERT INTO
  ving(prenom,nom,batiment,etage,motif,heure)\
  VALUES (?,?,?,?,?,?)")
  query.addBindValue(prenom)
  query.addBindValue(nom)
  query.addBindValue(combo1)
  query.addBindValue(combo2)
  query.addBindValue(combo3)
  query.addBindValue(heure)
  query.exec_()
  self.db.close()
  
<img width="704" alt="Screen Shot 2021-11-15 at 8 01 55 PM" src="https://user-images.githubusercontent.com/90251223/141884004-5ca1c4ad-a13c-49fc-b7fa-a0060be67b6f.png">

<img width="598" alt="Screen Shot 2021-11-15 at 8 02 19 PM" src="https://user-images.githubusercontent.com/90251223/141884021-b7dedb54-ac89-41c6-938c-a46b62db539f.png">

<img width="648" alt="Screen Shot 2021-11-15 at 8 02 53 PM" src="https://user-images.githubusercontent.com/90251223/141884025-ed916c3c-5a56-4de8-af86-ebef5ed26fa9.png">

<img width="643" alt="Screen Shot 2021-11-15 at 8 03 07 PM" src="https://user-images.githubusercontent.com/90251223/141884036-dd3bfd36-0f91-43f7-b01b-57bbec3d8484.png">

