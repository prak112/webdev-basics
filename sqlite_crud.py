# import library to build DB
import sqlite3

# create database in source
sqlConnect = sqlite3.connect("D:\VSCode_Projects\py310-webdev\pets_data.db")

# C- create database script
createTable = """
DROP TABLE IF EXISTS PETS;
CREATE TABLE PETS
(ID INT NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL);
"""
# I- data insertion script
insertData = """
INSERT INTO PETS (ID, NAME, AGE) VALUES (23, 'Sally', 5);
INSERT INTO PETS (ID, NAME, AGE) VALUES (41, 'Suuridu', 2);
INSERT INTO PETS (ID, NAME, AGE) VALUES (99, 'Anna', 29);
INSERT INTO PETS (ID, NAME, AGE) VALUES (9379, 'Prakirth', 380);
INSERT INTO PETS (ID, NAME, AGE) VALUES (10203, 'Drakamoma', 102031);
"""

# R- select data
selectData = """SELECT * FROM PETS;"""

# U- update data
updateData = """UPDATE PETS SET ID = 1023 WHERE NAME = 'Prakirth';"""

# D- delete data
deleteData = """DELETE FROM PETS WHERE AGE > 1000;"""

# execute queries
#sqlConnect.executescript(createTable)
#sqlConnect.executescript(insertData)
#sqlConnect.executescript(updateData)
sqlConnect.executescript(deleteData)
dbData = sqlConnect.execute(selectData)


# data selection script
print("My Pets are :\n")
for row in dbData:
    print(row,"\n")

# close DB connection
sqlConnect.close()

