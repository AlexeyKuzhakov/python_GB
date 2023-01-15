from pytube import YouTube

file_name = input('Введите URL скачиваемого видео: ')

def format_resilution():
    while True:
        try:
            reso = int(input('Введите качество видео (1 - 360p, 2 - 720p, 3 - 1080p): '))
            match reso:
                case 1:
                    return '360p'
                case 2:
                    return '720p'
                case 3:
                    return '1080p'
                case _:
                    print('Выберете один из параметров')
                    continue
        except:
            print('Введите число от 1 до 3')

reso = format_resilution()

yt_video = YouTube(file_name)

yt_video.streams.filter(resolution=reso, file_extension='mp4').first().download(r'C:\Users\kuzha\Desktop')