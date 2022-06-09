# groove-web
This is the web server (frontend and backend) allowing users to interact with the Groove Box (https://github.com/wang-edward/box).
This is a Flask server that takes a song (mp3/m4a/wav file) uploaded by the user and splits it into its 4 constituent tracks (bass, drums, vocals, other) using Deezer's Acoustic Classification library Spleeter.
The hardware and its software interface (created by @wang-edward) allow the user to manipulate different qualities of each track to mix the 4 tracks together.
