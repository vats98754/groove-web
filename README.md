# groove-web
This is the web server (frontend and backend) allowing users to interact with the Groove Box (https://github.com/wang-edward/box).
This is a Flask server that takes a song (mp3/m4a/wav file) uploaded by the user and splits it into its 4 constituent tracks (bass, drums, vocals, other) using Deezer's Acoustic Classification library Spleeter.
The hardware and its software interface (created by @wang-edward) allow the user to manipulate different qualities of each track to mix the 4 tracks together.

# Instructions
After downloading this repo, navigate to this directory and run the following command:
```sh
python3 server.py
```

Next, go to your web browser of choice (e.g. Google Chrome) and type the following (if you choose to host the website locally):
```sh
http://127.0.0.1:5000/
```

Replace the above with the domain or IP address of the web server you've hosted the website on.

You may upload an audio file, which will then download the 4 stem files (bass, drums, vocals, other) to the web server.
These 4 files will be downloaded onto the computer system hosting the web server.