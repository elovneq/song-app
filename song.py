import sqlite3

class Song():

	def __init__(self,name,singer,media_company,duration):
		self.name = name
		self.singer = singer
		self.media_company = media_company
		self.duration = duration
		
	def __str__():
		return "Name: {}\n Singer: {}\n Media Company: {}\n Duration: {}".format(self.name,self.singer,self.media_company,self.duration)
		
class Song_List():
	
	def __init__(self):
		
		self.con = sqlite3.connect("songs.db")
		self.cursor = self.con.cursor()
		query = "CREATE TABLE IF NOT EXISTS songs (Name TEXT, Singer TEXT, Media_Company TEXT, Duration INT)"
		self.cursor.execute(query)
		self.con.commit()
	
	def show_songs(self):
		query = "SELECT * FROM songs"
		self.cursor.execute(query)
		songs = self.cursor.fetchall()
		
		if len(songs) != 0 :
			for i in songs:
				print(i)
		else:
			print("No songs boss")
			
	# You should create a object song=Song() before this point
			
	def add_song(self,song):
		query = "INSERT INTO songs VALUES(?,?,?,?)"
		self.cursor.execute(query,(song.name,song.singer,song.media_company,song.duration))
		self.con.commit()
		
	def delete_song(self,name):
		
		query = "DELETE FROM songs WHERE name = ?"
		self.cursor.execute(query,(name,))
		self.con.commit()
		
	def search_song(self,name):
		query = "SELECT * FROM songs WHERE name = ?"
		self.cursor.execute(query,(name,))
		songs = self.cursor.fetchall()
		if len(songs) != 0:
			print(songs)
		else:
			print("There is no song named",name,"Boss")
		
	
