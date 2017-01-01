# -*- coding: utf-8 -*-
import argparse
import urllib.request
import re
import os

USER_AGETNT = "Mozilla/5.0 (iPad)"
COOKIE_FORMAT = "sp_mbga_sid_12008305=%s"
MOBAGE_URL = "http://sp.pf.mbga.jp/12008305"
GALLERY_URL_FORMAT = "http://125.6.169.35/idolmaster/idol_gallery/idol_detail/%s"

def get_page_data(url, sid):
    req = urllib.request.build_opener()
    req.addheaders = [
        ("Cookie", COOKIE_FORMAT % sid),
        ("User-Agent", USER_AGETNT)
    ]
    res = req.open(MOBAGE_URL, urllib.parse.urlencode({'url': url}).encode("utf-8"))
    if res.info()["Server"] == "connect.mobage.jp":
        raise Exception("session error")
    return res.read().decode("utf-8")

def get_detail_list(hash_id, sid):
    url = GALLERY_URL_FORMAT % hash_id
    data = get_page_data(url, sid)

    result = re.search(r"^idol.detail_list = .*;$", data, re.MULTILINE)
    if not result:
        raise Exception("error")
    return result.group()[19:-1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("hash", help="target hash_id")
    parser.add_argument("-s", "--session_id", help="mobage session id")
    args = parser.parse_args()

    sid = os.environ.get("sid")
    if not args.session_id is None:
        sid = args.session_id

    print(get_detail_list(args.hash, sid))
