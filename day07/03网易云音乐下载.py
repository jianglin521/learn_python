import cloudmusic

def getPlaylist(id):
  playlist = cloudmusic.getPlaylist(id)
  for music in playlist:
    print(music.name)
    music.download('./cloudmusic', "lossless")

if __name__ == '__main__':
  getPlaylist(489634244) # 列表id