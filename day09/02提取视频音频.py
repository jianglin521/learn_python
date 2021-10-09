from moviepy.editor import *

video = VideoFileClip('假面舞会-很美味.mkv')
audio = video.audio
# 有损格式
audio.write_audiofile('假面舞会-很美味.mp3')
# 无损格式
# audio.write_audiofile('有点甜.wav')
