#!/usr/bin/python3

"""
plexPlaylist.py:  This python script creates a Plex
playlist from the server API.  It takes one or more
m3u files as input.  A section and token ID are also
required.

To get these items, go to the "three dots" to the right
of a song already in the system (it may or may not
be a song in the desired playlist).  Click on 'Get Info'.
At the bottom click on the [View XML] button.  The
librarySectionID is in the XML and should be a small
integer number.  The X-Plex-Token is in the URL (typically
at the end) and is a string of about 20 random characters.
Use these as command line parameters for this script.

Note that the m3u files must be described as full paths
visible to the server.

Much of this info is taken from the Reddit post:
https://www.reddit.com/r/PleX/comments/ecirqa/how_to_manually_import_an_m3u_playlist_into_plex/
"""

__author__    = "Steven A. Guccione"
__date__      = "May 21, 2020"
__copyright__ = "Copyright (c) 2020 by Steven A. Guccione"

import argparse
import requests

if __name__ == '__main__':

   # Parse command line parameters
   parser = argparse.ArgumentParser()
   parser.add_argument("m3uFiles", nargs='+', type=str, help="m3u files (full path)")
   parser.add_argument("--section", type=int, help="librarySectionID from XML", required=True)
   parser.add_argument("--token", type=str, help="X-Plex-Token string from URL", required=True)
   parser.add_argument("--server", type=str, help="server name (default: http://127.0.0.1:32400)",
                       default='http://127.0.0.1:32400')
   parser.add_argument("--verbose", help="verbose flag", action='store_true')
   parser.add_argument("--debug", help="debug flag", action='store_true')
   args = parser.parse_args()

   for m3uFile in args.m3uFiles:

      # Create the request string
      url =  args.server + "/playlists/upload?sectionID=" +\
             str(args.section) + "&path=" + m3uFile +\
             "&X-Plex-Token=" + args.token
      if args.debug:
         print("url: " + url)

      # Make the request
      try:
         response = requests.post(url)
      except requests.exceptions.RequestException as err:
         raise SystemExit(err)
   
      if args.debug:
         print(response)

      if response.status_code == requests.codes.ok:
         if args.verbose:
            print(m3uFile, " done.")
      else:
         print("ERROR: HTTP server response code " + str(response.status_code))

   SystemExit(0)
   
