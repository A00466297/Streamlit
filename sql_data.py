import pandas as pd
import sqlite3

con = sqlite3.connect("data/Chinook_Sqlite.sqlite")
cursor = con.cursor()

query = "Select * from artist"
artists = pd.read_sql_query(query, con)
print(artists)

query = "Select * from album"
albums = pd.read_sql_query(query, con)
print(albums)

query = "Select at.ArtistId, at.Name, al.Title from album al inner join artist at on at.ArtistId = al.ArtistId where at.Name = \'Accept\'"
value = pd.read_sql_query(query, con)
print(value)
print("\n")

query = "Select at.ArtistId, at.Name, al.Title from album al inner join artist at on at.ArtistId = al.ArtistId"
records = pd.read_sql_query(query, con)
print(records)
