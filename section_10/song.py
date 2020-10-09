class Song:
  """ Class to represent a song

  Attributes:
    title (str): The title of the song
    artist (Artist): An Artist object representing the creator of the song
    duration (int): The duration of the song in seconds. May be zero
  """

  def __init__(self, title, artist, duration=0):
    self._title = title
    self._artists = artist
    self._duration = duration

class Album:
  """ Class to represent an Album, using its track list

  Attributes:
    albumName (str): The name of the album
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
