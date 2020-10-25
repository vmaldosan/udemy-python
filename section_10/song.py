class Song:
  """ Class to represent a song

  Attributes:
    title (str): The title of the song
    artist (Artist): An Artist object representing the creator of the song
    duration (int): The duration of the song in seconds. May be zero
  """

  def __init__(self, title, artist, duration=0):
    self.title = title
    self.artist = artist
    self.duration = duration

class Album:
  """ Class to represent an Album, using its track list

  Attributes:
    name (str): The name of the album
    year (int): The year when the album was released
    artist (Artist): The artist responsible for the album. If not specified,
    the artist will dofault to an artist with the name "Various artists"
    tracks (List[Song]): A list of the songs in the album

  Methods:
    addSong: Used to add a new song to the Album's track list
  """

  def __init__(self, name, year, artist=None):
    self.name = name
    self.year = year
    if artist is None:
      self.artist = Artist('Various artists')
    else:
      self.artist = artist
    
    self.tracks = []

  def addSong(self, song, position=None):
    """ Adds a song to the track list

    Args:
      song (Song): A song to add
      position (Optional[int]): if specified, the song will be added to that position
      in the track list - inserting it between other songs if necessary.
      Otherwise, the song will be added to the end of the list
    """

    if position is None:
      self.tracks.append(song)
    else:
      self.tracks.insert(position, song)


class Artist:
  """ Basic class to store artist details.

  Attributes:
    name (str): The name of the artist
    albums (List[Album]): A list of the albums by this artist.
      The list includes only those albums in this collection.
    
  Methods:
    addAlbum: Use to add a new ablum to the artist's albums list
  """

  def __init__(self, name):
    self.name = name
    self.albums = []

  def addAlbum(self, album):
    """ Add a new album to the list.

    Args:
      album (Album): Album object to add to the list.
        If the album is already present, it will not be added again
    """
    self.albums.append(album)


def findObject(field, objectList):
  """ Check 'objectList' to see if an object with a 'name' attribute equal to 'field' exists, return it if so """
  for item in objectList:
    if item.name == field:
      return item
  return None


def loadData():
  newArtist = None
  newAlbum = None
  artistList = []

  with open('albums.txt', 'r') as albums:
    for line in albums:
      # data row should consist of (artist, album, year, song)
      artistField, albumField, yearField, songField = tuple(line.strip('\n').split('\t'))
      yearField = int(yearField)
      print('{}:{}:{}:{}'.format(artistField, albumField, yearField, songField))

      if newArtist is None:
        newArtist = Artist(artistField)
        artistList.append(newArtist)
      elif newArtist.name != artistField:
        # We've just read details for a new artist
        # retrieve the artist object if there is one,
        # otherwise create a new artist object and add it to the artist list.
        newArtist = findObject(artistField, artistList)
        if newArtist is None:
          newArtist = Artist(artistField)
          artistList.append(newArtist)
        newAlbum = None

      if newAlbum is None:
        newAlbum = Album(albumField, yearField, newArtist)
        newArtist.addAlbum(newAlbum)
      elif newAlbum.name != albumField:
        # We've just read a new album for the current artist
        # Retrieve the album object if there is one
        # otherwise create a new album object and store it in the artist collection
        newAlbum = findObject(albumField, newArtist.albums)
        if newAlbum is None:
          newAlbum = Album(albumField, yearField, newArtist)
          newArtist.addAlbum(newAlbum)

      # create a new song object and add it to the current album's collection
      newSong = Song(songField, newArtist)
      newAlbum.addSong(newSong)
    
  return artistList


def createCheckfile(artistList):
  """ Create a check file form the object data for comparison with the original file """
  with open('checkfile.txt', 'w') as checkfile:
    for newArtist in artistList:
      for newAlbum in newArtist.albums:
        for newSong in newAlbum.tracks:
          print('{0.name}\t{1.name}\t{1.year}\t{2.title}'.format(newArtist, newAlbum, newSong),
            file=checkfile)


if __name__ == '__main__':
  artists = loadData()
  print('There are {} artists'.format(len(artists)))

  createCheckfile(artists)
