# AppleImgAutomate
[![Maintainability](https://api.codeclimate.com/v1/badges/5fcd1169197216f122c0/maintainability)](https://codeclimate.com/github/colcrunch/AppleImgAutomate/maintainability)
For resizing and renaming files in bulk for upload to website.

# Setup
* Download and install python (3.6.4)
  * How To: 
    * Go to https://www.python.org/downloads/release/python-364/ and scroll down to Files and click "Windows x86 executable installer" to download the installer.
    * Once it is finished downloading, open the installer by right clicking on it and selecting "Run as Administrator"
    * When the installer comes up you should see a window like this: ![img](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/images/python/pythonsetup.jpg)
    * Make sure that there are checks in the "Install launcher for all users" and "Add Python3.6 to PATH" boxes.
    * Click "Install Now"
    * At the end of the setup you should see a window like this: ![img](https://www.datasciencelearner.com/wp-content/uploads/2018/01/Python-3.6-Setup2.png)
    * Make sure to click the bit that is in the red box on that picture.
    * You are done! Check that it is installed correctly by opening command prompt and typing `python -V` and if you see `Python 3.6.4` you have installed it correctly.
* Download this script. You can do this by clicking the green "Clone or Download" button above and to the right of the list of files, and selecting "Download ZIP"
* In a location of your choosing, create a folder called "Images", in that folder create 3 more folders "movies", "Originals", and "screens"
* Unzip the zipfile you downloaded into the "Images" folder.
* Open command prompt again and run `python -m pip install -r requirements.txt`
* Right-Click proc.py and go to "Open With" and select "IDLE".
  * If IDLE is not in the "Open With" menu, go to the start menu and search for it. Once it opens click "File" then "Open" and navigate to your "Images" folder, then select "proc.py" and open it.
* Edit the `src` line replacing `RTS_SERVER_ID` with the IP address of your RTS server.
* You're done! Read the "Usage" section for how to use this script.

# Usage
Using this script is pretty easy. Simply download the posters for the movies, and place them in the "Images" folder, ensuring that their names match the name of the movie in RTS (including spaces, capitalization is not important), then once you have downloaded and renamed all of your images, douple click the script and let it do its work. When it is done, the sn (screen) files will be in screens, and the s (movie) files will be in movies. Now all you have to do is upload them to the site!
