import json
import requests
import urllib.parse as urlparse

ENDPOINT = (
    lambda x: f"https://www.youtube.com/get_video_info?video_id={x}&el=embedded&ps=default"
)


def metadata(id: str, scope: str) -> dict:
    response: dict = {}
    res = requests.get(ENDPOINT(id))
    decoded_res = res.content.decode("utf-8")
    parsed_res = urlparse.parse_qs(decoded_res)
    player_resp = parsed_res.get("player_response")
    player_resp: dict = json.loads(player_resp[0])

    if scope == "all":
        return player_resp

    # get all the formats
    f1 = player_resp.get("streamingData").get("adaptiveFormats", [])
    f2 = player_resp.get("streamingData").get("formats", [])

    response["formats"] = f1 + f2

    # get video details
    details: dict = player_resp.get("videoDetails")
    if details is not None:
        response["title"] = details.get("title")
        response["length"] = details.get("lengthSeconds")
        response["thumbnails"] = details.get("thumbnail")
        response["channel"] = details.get("author")

    return response