#Linked List
class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.nextSong = None
        self.prevSong = None


    def showSongDetails(self):
         print("{}\t{}\t{}".format(self.title, self.artist, self.duration))

song1 = Song("1. Gun Label", "Jiggar", 5.52)
song2 = Song("2. Old Skool", "Sidhu Moose Wala", 6.37)
song3 = Song("3. Legend", "Sidhu Moose Wala", 2.56)
song4 = Song("4. Malanag", "Yash", 5.23)
song5 = Song("5. Sheh", "Singga", 4.32)


print(">>1. song1 is:", song1)
print(">>2. song2 is:", song2)
print(">>3. song3 is:", song3)
print(">>4. song4 is:", song4)
print(">>5. song5 is:", song5)

song1.nextSong = song2
song2.nextSong = song3
song3.nextSong = song4
song4.nextSong = song5
song5.nextSong = song1

song5.prevSong = song4
song4.prevSong = song3
song3.prevSong = song2
song2.prevSong = song1
song1.prevSong = song5

temp = song1

while temp.nextSong != song1:
    print("------------------------")
    temp.showSongDetails()
    print("------------------------")
    temp = temp.nextSong

# Showing the Last Song Details
temp.showSongDetails()
print("------------------------")

current = song5

while current.prevSong != song5:
    print(">>>>>>>>>>>>")
    current.showSongDetails()
    print("<<<<<<<<<<")
    current = current.prevSong


current.showSongDetails()

