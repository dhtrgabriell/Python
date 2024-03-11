from moviepy.editor import VideoFileClip, concatenate_videoclips

clipe1 = VideoFileClip("clip1.mp4")
clipe2 = VideoFileClip("clip2.mp4")
clipe3 = VideoFileClip("clip3.mp4")

video_completo = concatenate_videoclips([
    clipe1,
    clipe2,
    clipe3
])

video_completo.write_videofile('VideoCompleto.mp4')