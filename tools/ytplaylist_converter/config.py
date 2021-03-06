import os

from dotenv import load_dotenv

load_dotenv()

YT_API_KEY = os.getenv("YT_API_KEY")
YT_CHANNEL_ID = "UCxboW7x0jZqFdvMdCFKTMsQ"
YT_MAX_RESULTS = 50

DIR = "playlists"
DIR_CHAPTER = "chapter"
INDEX = "_index.md"

_SERIES = '''
+++
author = "nathan"
title = "{title}"
description = "{description}"
date = "{date}"

difficulty = "beginner"

keywords = []

type = "course"

[[resources]]
src = "banner.png"
name = "banner"

playlistId = "{playlist_id}"
+++

'''

_CHAPTER = """
+++
author = "nathan"
title = "Title"
description = ""

type = "course_chapter"

weight = 1
+++

"""

_VIDEO = '''
+++
author = "nathan"
date = "{date}"
title = "{title}"
description = "{description}"
weight = {weight}

type = "video"

videoId = "{video_id}"
videoDuration = {video_duration}
+++

'''


FRONTMATTER = {
    "series": _SERIES.lstrip(),
    "chapter": _CHAPTER.lstrip(),
    "video": _VIDEO.lstrip(),
}
