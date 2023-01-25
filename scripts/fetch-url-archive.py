#!/usr/bin/env python3

import re
import sys
import random
import string

import urllib.parse
import urllib.request

import archiveis

ua = 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'

def get_title(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', ua)
    f = urllib.request.urlopen(req)

    content = f.read().decode('utf-8')

    pattern = '<title.*?>(.+?)</title>'
    result = re.findall('<title.*?>(.+?)</title>', content)
    return "" if len(result) == 0 else result[0]

if len(sys.argv) < 2:
    print('usage: {} URL [TEXT]'.format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)

url = sys.argv[1]

title = get_title(url)
archive_url = archiveis.capture(url, user_agent=ua).replace('/wip/', '/')

note_id = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=6))

if len(sys.argv) > 2:
    # Print inline link + note
    print('[{}][{}_link][^{}]'.format(sys.argv[2], note_id, note_id))
else:
    # Print just the note reference
    print('[^{}]'.format(note_id))

print('-------------------')
if len(sys.argv) > 2:
    print('[{}_link]: {}'.format(note_id, url))
print('[^{}]: *{}* [[original]]({}) [[archived]]({})'.format(note_id, title, url, archive_url))
