# video-downloder
from pytube import YouTube 
>> printf("     #########   ##          ##  ##########   ##       "\n)
   printf("     ##      ##   ##        ##       ##       ##       "\n)
   printf("     ##      ##    ##      ##        ##       ##       "\n)
   printf("     ##      ##     ##    ##         ##       ##        "\n)
   printf("     ##      ##      ##  ##          ##       ##        "\n)
   printf("     #########         ##        ##########   ######### "\n)
  
  printf(" This code is create by:--WHITEHAT-DEVIL/video-downloder/github.com ")
link = input("Enter the link:")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
