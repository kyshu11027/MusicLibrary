#Kevin Shu, kyshu@usc.edu
#ITP 115, Spring 2021
#Assignment 10
#Description:
#This script will simulates a music library through importing existing librraries
#provided. The progam will allow the user to change the music library and save it
#to the same original document

import MusicLibraryHelper
import random

def displayMenu():
    print("Welcome to Your Music Library")
    print("Options: ")
    print("\t1) Display library")
    print("\t2) Display all artists")
    print("\t3) Add an album")
    print("\t4) Delete an album")
    print("\t5) Delete an artist")
    print("\t6) Search library")
    print("\t7) Generate a random playlist")
    print("\t8) Exit")

def displayLibrary(musicLibDictionary):
    #loop to get every artist
    for key in musicLibDictionary:
        print("Artist: " + key)
        #getting the list of each album
        tempAlbumList = list(musicLibDictionary.get(key))
        print("Albums: ")
        #printing each album accordingly
        for album in tempAlbumList:
            print("\t- "+album)
        #deleting the list to reinitialize it for the next loop
        tempAlbumList.clear()

def displayArtists(musicLibDictionary):
    print("Displaying all artists: ")
    for key in musicLibDictionary:
        print("\t- " + key)

def addAlbum(musicLibDictionary):
    artist = input("Enter artist: ")
    artist = artist.lower()
    album = input("Enter album: ")
    album = album.lower()
    #to be used later to keep track of the right key
    correctKey = ""

    #all of this is to account for upper and lowercase and see if the album and artist already exists
    albumExists = False
    artistExists = False
    for key in musicLibDictionary:
        if artist == key.lower():
            artistExists = True
            correctKey = key
            for value in musicLibDictionary[key]:
                if album == value.lower():
                    albumExists = True

    #forming lists so that the new albums can be appended
    if artistExists and not albumExists:
        albumList = musicLibDictionary.get(correctKey)
        albumList.append(album.capitalize())
        musicLibDictionary[correctKey] = albumList
    elif not artistExists and not albumExists:
        albumList = []
        albumList.append(album.capitalize())
        musicLibDictionary[artist.capitalize()] = albumList



def deleteAlbum(musicLibDictionary):
    deleted = False
    artist = input("Enter artist: ")
    artist = artist.lower()
    album = input("Enter album: ")
    album = album.lower()

    #same method as above
    correctKey = ""
    correctValue = ""
    albumExists = False
    artistExists = False
    for key in musicLibDictionary:
        if artist == key.lower():
            artistExists = True
            correctKey = key
            for value in musicLibDictionary[key]:
                if album == value.lower():
                    correctValue = value
                    albumExists = True

    if albumExists and artistExists:
        musicLibDictionary[correctKey].remove(correctValue)
        deleted = True

    if deleted == True:
        print("Album successfully deleted.")
    else:
        print("Failed to delete Album.")
    return deleted

def deleteArtist(musicLibDictionary):
    deleted = False
    artist = input("Enter artist to delete: ")
    artist = artist.lower()

    #same method as above
    artistExists = False
    correctKey = ""

    for key in musicLibDictionary:
        if artist == key.lower():
            artistExists = True
            correctKey = key

    if artistExists:
        del musicLibDictionary[correctKey]
        deleted = True

    if deleted == True:
        print("Artist successfully deleted.")
    else:
        print("Failed to delete artist.")
    return deleted

def searchLibrary(musicLibDictionary):
    term = input("Please enter a search term: ")
    term = term.lower()

    artistList = []
    print("Artists containing '" + term + "'")
    for artist in musicLibDictionary:
        if artist.lower().find(term) != -1:
            artistList.append(artist)

    if len(artistList) == 0:
        print("\tNo results")
    else:
        for artist in artistList:
            print("\t- " + artist)

    albumList = []
    print("Albums containing '" + term + "'")
    for artist in musicLibDictionary:
        for album in musicLibDictionary[artist]:
            if album.lower().find(term) != -1:
                albumList.append(album)


    if len(albumList) == 0:
        print("\tNo results")
    else:
        for album in albumList:
            print("\t- "+album)

def generateRandomPlaylist(musicLibDictionary):
    print("Here is your random playlist:")
    for artist in musicLibDictionary:
        rand = random.randrange(0, len(musicLibDictionary[artist]))
        album = musicLibDictionary[artist][rand]
        print("- " + album + " by " + artist)


def main():
    musicLibDictionary = MusicLibraryHelper.loadLibrary('musicLibrary.dat')

    choice = "1"
    while choice != "8":
        displayMenu()
        choice = input(">")
        if choice == "1":
            displayLibrary(musicLibDictionary)
        elif choice == "2":
            displayArtists(musicLibDictionary)
        elif choice == "3":
            addAlbum(musicLibDictionary)
        elif choice == "4":
            deleteAlbum(musicLibDictionary)
        elif choice == "5":
            deleteArtist(musicLibDictionary)
        elif choice == "6":
            searchLibrary(musicLibDictionary)
        elif choice == "7":
            generateRandomPlaylist(musicLibDictionary)
        elif choice == "8":
            MusicLibraryHelper.saveLibrary("musicLibrary.dat", musicLibDictionary)
            print("Saving music library... \nGoodbye!")
        else:
            choice = print("Invalid choice. Try again.")



main()

