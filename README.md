# Analyzing-visitor-traffic

Application built to control visitor traffic.

It analyzes the visitors traffic with data gathered based on the floor, the building name and the reason of their visit. 

Decisions can be made such as restricting access to certain floor, provide more security, make predictions and 

much more.



LIBRARIES USED FOR THIS PROJECT:

==> PyQt4 (will need to install sip for this version)

==> SQLite3

==> Numpy

==> Matplotlib


<img width="702" alt="Screen Shot 2021-11-15 at 8 01 24 PM" src="https://user-images.githubusercontent.com/90251223/141883950-0e41f20a-28f5-47f3-93d3-c98306dc0ae1.png">

  takes the first and last name, building, floor, time and saves it to the database.
  
<img width="704" alt="Screen Shot 2021-11-15 at 8 01 55 PM" src="https://user-images.githubusercontent.com/90251223/141884004-5ca1c4ad-a13c-49fc-b7fa-a0060be67b6f.png">

  display the database entries from a date specified. the option to filter by first or last name is available.
  
<img width="598" alt="Screen Shot 2021-11-15 at 8 02 19 PM" src="https://user-images.githubusercontent.com/90251223/141884021-b7dedb54-ac89-41c6-938c-a46b62db539f.png">

  Gives an average of how many visitors the site counted in the last 5 weeks.

<img width="648" alt="Screen Shot 2021-11-15 at 8 02 53 PM" src="https://user-images.githubusercontent.com/90251223/141884025-ed916c3c-5a56-4de8-af86-ebef5ed26fa9.png">

  Shows a diagram of the 3 different department.

<img width="643" alt="Screen Shot 2021-11-15 at 8 03 07 PM" src="https://user-images.githubusercontent.com/90251223/141884036-dd3bfd36-0f91-43f7-b01b-57bbec3d8484.png">
  
  charts showing activities that is most in demand and busyness of the floor of each department.
  
METHOD THAT CONNECTS TO THE SQLITE DATABASE:

```
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
```

GET VALUE FROM SQLITE DATABSE BEFORE PASSING IT TO MATPLOTLIB

```
def requete_sqlite(self):
  self.conn = sqlite3.connect("securite.db")
  c = self.conn.cursor()
  liste =c.execute("SELECT count(batiment) from quatre where\
  batiment='b'")
  rows = liste.fetchall()
  if rows:
    for y in rows:
      self.b = int(''.join(map(str,y)))
  c.close()
```

in this method we create an instance of the database from python buit in sql command instead of the PyQt one. 
We then take the value of the matrix and convert it to in integer. This value can now be passed to our matplotlib library.

METHOD THAT GIVES MATPLOTLIB THE DATA SO IT CAN BE DISPLAYED IN GRAPHS

```
def transfert_matplotlib(self):
  from matplotlib.ticker import FuncFormatter
  import matplotlib.pyplot as pyplot
  import numpy as np
  x = np.arange(10)
  
motif=\
[self.visite,self.courrier,self.caisse,self.bon,self.reunion,self.cours
ier,self.rdv,self.facture,self.livraison,self.autres]
pyplot.figure('GESTION VISITEURS')
pyplot.subplot(2, 1, 1)
pyplot.bar(x +0.5, motif, color = '#336600')
pyplot.xticks(x + 1, ('VIST', 'COUR', 'CAISS',
'BON','REUN','CRSE','RDV','FACT','LIVR','AUTRS'))
pyplot.title('MOTIF')

############ BATIMENT A ############
x1 = np.arange(8)
etageA =
[self.etA1,self.etA2,self.etA3,self.etA4,self.etA5,self.etA6,self.etA7,
self.etA8]
pyplot.subplot(2, 3, 4)
pyplot.bar(x1 + 0.5, etageA, color = '#99CC33')
pyplot.xticks(x1 + 1, ('E1', 'E2', 'E3', 'E4','E5','E6','E7','E8'))
pyplot.title('BATIMENT A')

############ BATIMENT B ############
x2 = np.arange(8)
etageB=\
[self.etB1,self.etB2,self.etB3,self.etB4,self.etB5,self.etB6,self.etB7,
self.etB8]
pyplot.subplot(2, 3, 5)
pyplot.bar(x2 + 0.5, etageB, color = '#99CC66')
pyplot.xticks(x2 + 1, ('E1', 'E2', 'E3', 'E4','E5','E6','E7','E8'))
pyplot.title('BATIMENT B')

############ BATIMENT C ############
x3 = np.arange(8)
etageC=\
[self.etC1,self.etC2,self.etC3,self.etC4,self.etC5,self.etC6,self.etC7,
self.etC8]
pyplot.subplot(2, 3, 6)
pyplot.bar(x3 + 0.5, etageC, color = '#CCFF99')
pyplot.xticks(x3 + 1, ('E1', 'E2', 'E3', 'E4','E5','E6','E7','E8'))
pyplot.title('BATIMENT C')
pyplot.show()
```
