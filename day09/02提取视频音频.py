from moviepy.editor import *

video = VideoFileClip('有点甜.mp4')
audio = video.audio
# 有损格式
audio.write_audiofile('有点甜.mp3')
# 无损格式
# audio.write_audiofile('有点甜.wav')
