# YTMETA - An API to fetch YouTube video metadata

There are a lot of YouTube video downloaders out there. By making use of tools like `youtube-dl`, they get the job done. But `ytmeta` is different. It is an API that returns necessary data to create your own downloader. Now you can create beautiful frontends with your favourite tools like, Reactjs, Vuejs, Sveltejs and whatnot.

It returns data including `title`, `views`, `links to thumbnail` and `various formats along with links to them`. Just an API call and get all the data you need in quick time.

### Usage

`curl https://ytmeta.tk/api/{video_id}`

This should return all the necessary data required to create an app.

### Response Contents

| Name         | Key        | Description                                                          |
| ------------ | ---------- | -------------------------------------------------------------------- |
| Title        | title      | Title of the video                                                   |
| Channel Name | channel    | Channel the video belongs to                                         |
| Views        | views      | Total view count(when the API call was made)                         |
| Length       | length     | Duration of the video in seconds                                     |
| Thumbnails   | thumbnails | List of dictionary containing various thumbnail sizes and their URLs |
| Formats      | formats    | List of dictionary containing different video formats                |
