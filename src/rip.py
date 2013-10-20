"""
MakeMKV Auto Ripper

Uses MakeMKV to watch for movies inserted into DVD/BD Drives
Looks up movie title on IMDb for saving into seperate directory

Automaticly checks for existing directory/movie and will NOT overwrite existing
files or folders
Checks minimum length of video to ensure movie is ripped not previews or other
junk that happens to be on the DVD


This script can be run with a simple cron, every 5 minutes or so

DVD goes in > MakeMKV checks IMDb and gets a proper DVD name > MakeMKV Rips
DVD does not get ejected, maybe it will get added to later versions

Released under the MIT license
Copyright (c) 2012, Jason Millward

@category   misc
@version    $Id: 1.4, 2013-04-03 09:41:53 CST $;
@author     Jason Millward <jason@jcode.me>
@license    http://opensource.org/licenses/MIT

Enough with these comments, on to the code
"""

import os
import sys
import ConfigParser
from makemkv import makeMKV
from timer import Timer

DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE = "%s/../settings.cfg" % DIR


def read_value(key):
    """
    read_value temp docstring
    """
    config = ConfigParser.RawConfigParser()
    config.read(CONFIG_FILE)
    to_return = config.get('MAKEMKV', key)
    config = None
    return to_return


def rip():
    """
    rip temp docstring
    """
    mkv_save_path = read_value('save_path')
    mkv_min_length = int(read_value('min_length'))
    mkv_cache_size = int(read_value('cache_MB'))
    mkv_tmp_output = read_value('temp_output')
    use_handbrake = bool(read_value('handbrake'))

    mkv_api = makeMKV()

    dvds = mkv_api.findDisc(mkv_tmp_output)

    if (len(dvds) > 0):
        # Best naming convention ever
        for dvd in dvds:
            disc_index = dvd["discIndex"]
            disc_title = dvd["discTitle"]

            movie_title = mkv_api.getTitle(disc_title)

            print movie_title


    else:
        print "Could not find any DVDs in drive list"

if __name__ == '__main__':
    rip()
