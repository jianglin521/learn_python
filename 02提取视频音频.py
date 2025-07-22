from moviepy import VideoFileClip

video = VideoFileClip('7454592452767386915.mp4')
audio = video.audio
# 有损格式
audio.write_audiofile('7454592452767386915.mp3')
# 无损格式
# audio.write_audiofile('有点甜.wav')
