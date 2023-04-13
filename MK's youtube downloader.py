from pytube import YouTube
yt = YouTube
link = input("please enter the video url: ")
video = YouTube(link)

print(f"the video title is:\n{video.title} \n-------------")
print(f"the video description is:\n{video.description} \n-------------")
print(f"the video views is:\n{video.views} \n-------------")
print(f"the video rating is:\n{video.rating} \n-------------")
print(f"the video duration is:\n{video.length} seconds \n-------------")
print(f"the video duration is:\n{video.length/60} minutes \n-------------")

def finish():
    print("download done")

# for stream in video.streams.filter(progressive=True, res="720"):
  # print (stream)


for stream in video.streams.filter(subtype='mp4'):
    print(stream)
video.streams.get_highest_resolution().download(output_path='D:\py')
# video.streams.get_lowest_resolution().download(output_path='D:\py')
video.streams.get_audio_only().download(output_path='D:\py')
video.register_on_complete_callback(finish())
