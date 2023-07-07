# livp2png

.livp to .png file converter written in Python

The program will do the following:

livp -> Convert to HEIC + MOV -> Convert HEIC to PNG -> Remove the HEIC and MOV files

To convert HEIC to PNG, I'm using a slightly modded version of [heic_image_converter](https://github.com/XDwightsBeetsX/heic-image-converter) by [XDwightsBeetsX](https://github.com/XDwightsBeetsX).
## Demonstration
![](https://too.lewd.se/14d7fa09a7f1_firefox_bWWk5vsfi5.gif)

## Usage
### Windows executable file
First of all, you should have any program which can run the command ```tar -xf {filename}``` (such as WinRar), as livp files are basically zips containing HEIC and MOV files.

Then, simply put the .livp files in the same folder which you decided to put livp2png.exe file and open it.

Heres the direct [Download link](https://github.com/alessio-ds/livp2png/releases/download/v1.0/livp2png.exe).
### Python
First of all, you should have any program which can run the command ```tar -xf {filename}``` (such as WinRar), as livp files are basically zips containing HEIC and MOV files.

NOTE: on linux you need ```unzip```

Then, simply install Pillow (PIL) and pillow_heif
```
pip install pillow
```
and
```
pip install pillow-heif
```
Then, put the .livp files in the same repo folder and run
```
python livp2png.py
```

