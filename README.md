# PlexPlaylist
The Plex server supports playlist in its API, but there isn't
direct support in the UI.  This simple Python script takes
m3u files and creates playlists in Plex.

# Help

```bash
$ ./plexPlaylist.py --help
usage: plexPlaylist.py [-h] --section SECTION --token TOKEN [--server SERVER] [--verbose]
                       [--debug]
                       m3uFiles [m3uFiles ...]

positional arguments:
  m3uFiles           m3u files (full path)

optional arguments:
  -h, --help         show this help message and exit
  --section SECTION  librarySectionID from XML
  --token TOKEN      X-Plex-Token string from URL
  --server SERVER    server name (default: http://127.0.0.1:32400)
  --verbose          verbose flag
  --debug            debug flag
```

# Sample Run

```bash
$ ./plexPlaylist.py --server=http://192.168.1.152:32400 --section=3 --token=GFfUQoaB9MKixjMRcdU6 /Archive/Media/Music/My\ Playlists/*.m3u --verbose
/Archive/Media/Music/My Playlists/80sPlus.m3u  done.
/Archive/Media/Music/My Playlists/America.m3u  done.
/Archive/Media/Music/My Playlists/BauhausAndBeyond.m3u  done.
/Archive/Media/Music/My Playlists/Bowie.m3u  done.
/Archive/Media/Music/My Playlists/BritPop.m3u  done.
/Archive/Media/Music/My Playlists/Buffett.m3u  done.
/Archive/Media/Music/My Playlists/Diane2010.m3u  done.
/Archive/Media/Music/My Playlists/Dylan II.m3u  done.
/Archive/Media/Music/My Playlists/Dylan.m3u  done.
/Archive/Media/Music/My Playlists/Elton John.m3u  done.
/Archive/Media/Music/My Playlists/Grateful Dead.m3u  done.
/Archive/Media/Music/My Playlists/Joni Mitchell.m3u  done.
/Archive/Media/Music/My Playlists/June 2003.m3u  done.
/Archive/Media/Music/My Playlists/March 2010.m3u  done.
/Archive/Media/Music/My Playlists/New Orleans II.m3u  done.
/Archive/Media/Music/My Playlists/New Orleans.m3u  done.
/Archive/Media/Music/My Playlists/REM.m3u  done.
/Archive/Media/Music/My Playlists/Rebels.m3u  done.
/Archive/Media/Music/My Playlists/Sarah's Bat Mitzvah.m3u  done.
/Archive/Media/Music/My Playlists/Soul II.m3u  done.
/Archive/Media/Music/My Playlists/Steely Dan.m3u  done.
/Archive/Media/Music/My Playlists/Summer 2009.m3u  done.
/Archive/Media/Music/My Playlists/Texas.m3u  done.
/Archive/Media/Music/My Playlists/Trip 80s.m3u  done.
/Archive/Media/Music/My Playlists/Xilinx Music.m3u  done.
/Archive/Media/Music/My Playlists/Zappa.m3u  done.
```

# Screenshot

![Plex Screenshot] (https://github.com/steven-guccione/PlexPlaylist/blob/master/PlexScreenshot.png)
