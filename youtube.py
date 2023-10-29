from pytube import YouTube


def YT_DownloadVideo(url: str, filename: str, path=r'C:\Users\honor\upsTGbot\youtubefiles'):
    try:
        stream = YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first()
    except:
        return 0  # если ссылка недействительна
    if stream.filesize_mb > 512:
        return -1  # если файл слишком большой
    stream.download(
        filename=filename,
        output_path=path,
    )
    return 1  # если файл успешно скачан

