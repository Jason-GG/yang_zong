#!/usr/bin/env python3
import sys

from instagram_user_info import main as instagram_main


# COOKIE = 'datr=mE9RaCQ_gzRvnsofR9NFD-w4; ig_did=DE72CBB3-64DE-4566-9414-53E1503C2A72; mid=aFFPmAAEAAFjt-5W5PhYiJD7jTTF; ig_nrcb=1; ps_l=1; ps_n=1; csrftoken=1Y5SrUw9NunThE6IgzGQ6UoOqNa6anCq; ds_user_id=46337139866; wd=1920x1055; sessionid=46337139866%3AstP0cnIJmasRnN%3A9%3AAYjBgW_JW59nzEGPnMxJCLRvc304ZhEyEYMf3tyoT0Y; rur="CCO\05446337139866\0541803848869:01febeb857fb9e8e81cf6d10611a9587eac3057683dbd75663c3f635e999b50e667e8f64"'
COOKIE = 'datr=mE9RaCQ_gzRvnsofR9NFD-w4; ig_did=DE72CBB3-64DE-4566-9414-53E1503C2A72; mid=aFFPmAAEAAFjt-5W5PhYiJD7jTTF; ig_nrcb=1; ps_l=1; ps_n=1; csrftoken=1Y5SrUw9NunThE6IgzGQ6UoOqNa6anCq; ds_user_id=46337139866; sessionid=46337139866%3AstP0cnIJmasRnN%3A9%3AAYjBgW_JW59nzEGPnMxJCLRvc304ZhEyEYMf3tyoT0Y; wd=1920x1055; rur="NHA\05446337139866\0541803868963:01fe1034f16c31848a59c41cf9c45cc2e208a0e5d29e03e65143bac387187b265df79ead"'
X_IG_APP_ID = "936619743392459"
X_ASBD_ID = "198387"
USER_ID = "4013697812"

SLEEP_SECONDS = 1
# QUERY_HASH = "58712303d941c6855d4e888c5f0cd22f"
QUERY_HASH = "37479f2b8209594dde7facb0d904896a"
# EDGE_FIELD = "edge_follow"
EDGE_FIELD = "edge_followed_by"
# EXCEL_PATH = "following_4013697812.xlsx"
EXCEL_PATH = "follower_4013697812.xlsx"

def build_argv() -> list[str]:
    argv = [
        "main.py",
        "--user-id",
        USER_ID,
    ]

    if COOKIE and COOKIE != "PASTE_YOUR_COOKIE_HERE":
        argv.extend(["--cookie", COOKIE])
    if X_IG_APP_ID:
        argv.extend(["--x-ig-app-id", X_IG_APP_ID])
    if X_ASBD_ID:
        argv.extend(["--x-asbd-id", X_ASBD_ID])
    if EXCEL_PATH:
        argv.extend(["--excel-path", EXCEL_PATH])
    if SLEEP_SECONDS is not None:
        argv.extend(["--sleep", str(SLEEP_SECONDS)])
    if QUERY_HASH is not None:
        argv.extend(["--query-hash", str(QUERY_HASH)])
    if EDGE_FIELD:
        argv.extend(["--edge-field", EDGE_FIELD])
    return argv


if __name__ == "__main__":
    sys.argv = build_argv()
    sys.exit(instagram_main())
