* My Yt-dlp top commands
make sure your yt-dlp config dosen't have arguments that may break with this
** For Downloading sereval musics in youtube bound by one video, for example a full album video with each chapter being a seperate music title (it still has a bug for me where it dosen't delete the old unchopped music)
```sh
yt-dlp -x --audio-format mp3 -f bestaudio --embed-thumbnail --external-downloader aria2c --external-downloader-args '-c -j 3 -x 3 -s 3 -k 1M' --split-chapters -o "chapter:%(section_number)s-%(section_title)s.%(ext)s" --parse-metadata "title:%(section_title)s - %(artist)s" [VIDEO]
```

** For Downloading a playlist containing seperate music videos
```sh
yt-dlp -x --audio-format mp3 -f bestaudio --add-metadata --embed-thumbnail --external-downloader aria2c --external-downloader-args '-c -j 3 -x 3 -s 3 -k 1M' --ignore-errors --continue --no-overwrites --download-archive progress.txt -o "%(playlist_index)s-%(title)s.%(ext)s" --parse-metadata "title:%(title)s - %(artist)s" --embed-metadata [VIDEO]
```
