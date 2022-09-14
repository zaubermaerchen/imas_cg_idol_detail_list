# -*- coding: utf-8 -*-
import argparse
import urllib.request
import re
import os
from idol_hash import IDOL_HASH

USER_AGETNT = "Mozilla/5.0 (iPad)"
COOKIE_FORMAT = "sp_mbga_sid_12008305=%s"
MOBAGE_URL = "http://sp.pf.mbga.jp/12008305/"
GALLERY_URL_FORMAT = "http://mobamas.net/idolmaster/idol_gallery/idol_detail/%s"

def get_page_data(url, sid):
    params = urllib.parse.urlencode({'url': url}).encode("utf-8")
    url = MOBAGE_URL + "?" + params.decode()
    req = urllib.request.build_opener()
    req.addheaders = [
        ("Cookie", COOKIE_FORMAT % sid),
        ("User-Agent", USER_AGETNT)
    ]
    res = req.open(url, timeout = 5)
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
    parser.add_argument("target", help="target idol")
    parser.add_argument("-n", "--name", action='store_true', help="enable name target mode")
    parser.add_argument("-s", "--session_id", help="mobage session id")
    args = parser.parse_args()

    sid = os.environ.get("sid")
    if not args.session_id is None:
        sid = args.session_id

    if args.name is True:
        hash_id = IDOL_HASH.get(args.target, None)
    else:
        hash_id = args.target

    print(get_detail_list(hash_id, sid))
