from song import *
import time
import os

print("""
**********************************

Welcome to eLovNeQ's Music Shop

1- Show songs        
2- Add a song	     
3- Delete a song
4- Search a song
5- Clear the screen

Press q to quit

""")

song_list = Song_List()

while True:
	inp = input("\nWhat do you wanna do ? :")
	
	if inp == "1":
		print("Listing all the songs...")
		time.sleep(1)
		song_list.show_songs()
	
	elif inp == "2":
		name = input("Name: ")
		singer = input("Singer: ")
		media_company = input("Media Company: ")
		Duration = float(input("Duration: "))
		
		new_song = Song(name,singer,media_company,Duration)
		song_list.add_song(new_song)
		print("Song added succesfully")
		
	elif inp == "3":
	
		name = input("Name: ")
		print("Deleting the song...")
		time.sleep(1)
		song_list.delete_song(name)
		print("Song deleted successfully")
	elif inp == "4":
		name = input("Name: ")
		song_list.search_song(name)
	
	elif inp == "5":
		print("Cleaning the screen...")
		time.sleep(1)
		os.system("clear" or "cls")
		
	elif inp == "q":
		print("Quiting... See you again...")
		time.sleep(1)
		break
	
	else:
		print("Please enter valid value")
