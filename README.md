# renamer
Command line python script to rename TV shows' episodes in bulk.

## Description
Currently, the script supports renaming of files whose name is something like this:
```
Dragon Ball 1x001 Goku Conosce Bulma ITA.JPN 1080p H265 sub ita EncoderName-Source.mkv
```

where ```1x001``` denotes the season and episode numbers (season 1, episode 1), and what comes after is the episode name or at least contains the episode name (in the above example, episode name is ```Goku Conosce Bulma``` and all the rest is garbage).

The output will be a file with a media-server-friendly name (e.g. [Plex](https://www.plex.tv/), [Emby](https://emby.media/)) to allow for easy and quick organization of your media library:
```
Dragon Ball - S01e001 - Goku Conosce Bulma.mkv
```

## Usage
As with any python program, you should be using python virtual environments.\
To set up one, navigate to the folder and run the command:
```
python -m venv venv
```
Activate virtual env:
```
source venv/bin/activate
```

Install all dependencies:
```
pip install -r requirements.txt
```
Now you're all set to use the script to rename your files.
To rename files in a given folder, run:
```
python renamer.py --folder "FOLDER_PATH" --show "SHOW_TITLE" --remove-after "CUSTOM_STRING"
```
where:
- ```FOLDER_PATH``` is the path to your folder containing the files to rename

- ```SHOW_TITLE``` is the title of the show that will be prepended to all episodes

- ```CUSTOM_STRING``` is a custom string after which to remove garbage content from filenames (e.g. if your episode name is followed by garbage like\
```...Your episode name ENG.JAP.BDRip.1080p.x265.sub.ENG.mkv```\
you can pass the string "ENG" as your ```CUSTOM_STRING``` to remove everything from that string onwards from your episode name)