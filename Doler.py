# YouTube video downloader project....
>>> from pytube import YouTube
 
   print('     #########   ##          ##  ##########   ##        ')
   print('     ##      ##   ##        ##       ##       ##        ')
   print('     ##      ##    ##      ##        ##       ##        ')
   print('     ##      ##     ##    ##         ##       ##        ')
   print('     ##      ##      ##  ##          ##       ##        ')
   print('     #########         ##        ##########   ######### ')
  
   print(' This code is create by:--WHITEHAT-DEVIL/video-downloder/github.com ')
 
 >>> from pytube import YouTube
 >>> YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
 >>> yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
 >>> yt.streams
  ... .filter(progressive=True, file_extension='mp4')
  ... .order_by('resolution')
  ... .desc()
  ... .first()
  ... .download()
 
  
