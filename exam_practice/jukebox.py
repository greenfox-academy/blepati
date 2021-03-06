# Create a Song class, that stores it's title and author
# Create a constructor for setting those values
# It should have 2 methods:
# one should add a rating to the song, the rating should be a number between 1 and 5
# if it is higher it should take it as 5 and if it is take it as 1
#
# The other should return the average rating of the song (the average of all the rates)
#
# Create a Jukebox class
# it should store the songs in an array
# it should have a method add a song
# it should have a method to rate the song with the given title
# it should have a method that returns a list of song titles that have the given artist
# it should hame a method that returns the top rated songs title

import random

class Song(object):
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.ratings = []

    def __repr__(self):
        return self.author + ": " + self.title

    def add_rate(self, rate):
        if rate >= 5:
            rate = 5
        if rate <= 0:
            rate = 1
        self.ratings.append(rate)

    def avg_rating(self):
        sum_rating = 0
        for rating in self.ratings:
            sum_rating += rating
        try:
            return sum_rating/len(self.ratings)
        except ZeroDivisonError:
            return 0

class Jukebox(object):
    def __init__(self):
        self.list_of_songs = []

    def add_song(self, song):
        new_song = song
        self.list_of_songs.append(new_song)

    def songs_of_artist(self, author):
        songs_of_artist = []
        for song in self.list_of_songs:
            if author == song.author:
                songs_of_artist.append(song.title)
        return songs_of_artist

    def add_rating_by_title(self, title, rate):
        for song in self.list_of_songs:
            if title == song.title:
                song.add_rate(rate)

song1 = Song("Nneka", "Hartbeat")
song2 = Song("Nneka", "Restless")
song3 = Song("Akua Naru", "The world is listening")
song1.add_rate(5)
song1.add_rate(3)
#print(song1.avg_rating())
jukebox = Jukebox()
jukebox.add_song(song1)
jukebox.add_song(song2)
jukebox.add_song(song3)
print(jukebox.list_of_songs)
print(jukebox.songs_of_artist("Nneka"))
jukebox.add_rating_by_title("Hartbeat", 5)
print(song1.avg_rating())
