
import sqlite3

def datenbank_erstellen():
    verbindung = sqlite3.connect("lager.db")
    cursor =  verbindung.cursor()
    with open("schema.sql", "r") as datei:
        sql = datei.read()
        cursor.executescript(sql)
        verbindung.commit()
        verbindung.close()
        print ("Datenbank und Tabellen wurden erfolgreich erstellt.")

if __name__ == "__main__":
    datenbank_erstellen()
    