# Website and Backend for the Groove Box
This is the web server (frontend and backend) allowing users to interact with the Groove Box (https://github.com/wang-edward/box).

This is a Flask server that takes a song (mp3/m4a/wav file) uploaded by the user and splits it into its 4 constituent tracks (bass, drums, vocals, other) using Deezer's Acoustic Classification library Spleeter.
The hardware and its software interface (created by @wang-edward) allow the user to manipulate different qualities of each track to mix the 4 tracks together.

# Learnings
I used the Flask documentation as well as https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask to:
- understand the basics of the web (protocols, communication, HTML/CSS/JS basics, error codes/messages, etc.),
- how to setup and connect a backend (with Flask, I'll be moving to Django for my next project) and a frontend (with basic HTML, I'll be moving to Vanilla JS and Vue/ReactJS next),
- how to manage and process uploads to my website (learned Flask and used Spleeter, Deezer's ML-based Audio Classification library),
- as well as the Version Control Systems "Git" and how to use it with Github (learned from The Odin Project). I look forward to learning more Git stuff and would love to see just how useful these can be in a collaborative work environment on-the-job.

Seeing as I've already done stuff in Python, I decided it would be nice to have a Python backend and a basic HTML frontend (I'm learning Git, JS/CSS, and Vue/ReactJS/other JS frameworks through The Odin Project (TOP) among other resources to improve the frontend). I've learned how to implement and host a web server, how to manage file uploads on a web server's backend, and how to process these uploads to extract meaningful information. I used Spleeter, Deezer's Audio Classification library for the processing part of it and I plan to use similar software in a future project that would distinguish and subsequently remove your pets' noises from your own during your online meetings/video calls (using a web app made with Vue/ReactJS and a Django backend that utilizes Audio Classification). In any case, I hope to implement my web dev learnings in the latter and other projects I'll be doing alongside those from TOP. Shoutouts to Edward for the opportunity.

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

# Dependencies
Install the dependencies for this project by typing the below code in Terminal (learn to install pip as a prereq):
```sh
pip3 install XXX
```
And replacing the XXX above with each of:
- flask
- imghdr
- spleeter