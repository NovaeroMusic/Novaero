from mutagen.id3 import ID3, APIC

def add_metadata(file_path, artist, album, title, track_number, year, genre, cover_path):
  """
  Adds metadata to an MP3 file.

  Args:
    file_path: Path to the MP3 file.
    artist: Artist name.
    album: Album name.
    title: Song title.
    track_number: Track number.
    year: Year of release.
    genre: Music genre.
    cover_path: Path to the cover art image.
  """
  try:
    audio = ID3(file_path)
  except:
    audio = ID3()

  audio['TIT2'] = mutagen.id3.TIT2(encoding=3, text=title)
  audio['TPE1'] = mutagen.id3.TPE1(encoding=3, text=artist)
  audio['TALB'] = mutagen.id3.TALB(encoding=3, text=album)
  audio['TRCK'] = mutagen.id3.TRCK(encoding=3, text=str(track_number))
  audio['TDRC'] = mutagen.id3.TDRC(encoding=3, text=year)
  audio['TCON'] = mutagen.id3.TCON(encoding=3, text=genre)

  # Add cover art
  with open(cover_path, 'rb') as f:
      audio.tags.add(
          APIC(
              encoding=3,  # 3 is for UTF-8
              mime='image/jpeg',  # Replace with the actual image format
              type=3,  # Front cover art
              desc=u'Cover',
              data=f.read()
          )
      )

  audio.save()

# Example usage:
file_path = "path/to/your/song.mp3" 
cover_path = "path/to/cover.jpg"
add_metadata(
    file_path,
    "Your Artist Name",
    "Your Album Name",
    "Your Song Title",
    "1", 
    "2024", 
    "Rock", 
    cover_path
)