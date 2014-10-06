# Filename: sound_cloud_scraper.py
# Authors: Justine Lee, Jake Utter
# Date: 10.5.2014 
# Description: program for scraping SoundCloud for urls of cover songs


def main(song_filename,url_filename):
	# Open the files for reading and writing
	song_file = open(song_filename,'r')
	url_file = open(url_filename,'w')

	#Read in songs line by line
	for line in song_file:
		song_info = line.split("~");
		print song_info

	# Close the files
	song_file.close()
	url_file.close()

main('songs.txt','test_out.txt')
