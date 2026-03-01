# Instagram User Export Tool

This project fetches Instagram followers/following via GraphQL, enriches each user with detail info, and stores results in an Excel file (`.xlsx`).

## Files

- `main.py`: quick launcher with hardcoded config values.
- `instagram_user_info.py`: main script with CLI arguments.

## Requirements

- Python 3.9+
- Python packages:
  - `requests`
  - `openpyxl`

## Install Dependencies

Using your project virtualenv:

```bash
cd /Users/jianshun/Documents/projects/yang_zong
source .venv/bin/activate
pip install requests openpyxl
```

## Quick Start (using `main.py`)

1. Open `main.py` and set your values:
   - `COOKIE`
   - `X_IG_APP_ID`
   - `X_ASBD_ID`
   - `USER_ID`
   - `QUERY_HASH`
   - `EDGE_FIELD` (`edge_followed_by` for followers, `edge_follow` for following)
   - `SLEEP_SECONDS` (e.g. `4`)
   - `EXCEL_PATH`

2. Run:

```bash
/Users/jianshun/Documents/projects/yang_zong/.venv/bin/python /Users/jianshun/Documents/projects/yang_zong/main.py
```

## CLI Usage (direct)

```bash
/Users/jianshun/Documents/projects/yang_zong/.venv/bin/python /Users/jianshun/Documents/projects/yang_zong/instagram_user_info.py \
  --user-id 4013697812 \
  --cookie 'YOUR_COOKIE' \
  --x-ig-app-id 936619743392459 \
  --x-asbd-id 198387 \
  --query-hash 37479f2b8209594dde7facb0d904896a \
  --edge-field edge_followed_by \
  --sleep 4 \
  --excel-path follower_4013697812.xlsx
```

For following list, use:
- `--query-hash 58712303d941c6855d4e888c5f0cd22f`
- `--edge-field edge_follow`

## Output Columns

The Excel sheet (`users`) contains:

- `id`
- `username`
- `instagram_url` (`https://www.instagram.com/{username}`)
- `full_name`
- `is_private`
- `is_verified`
- `profile_pic_url`
- `followed_by_viewer`
- `requested_by_viewer`
- `biography`
- `category`

## Notes

- The script writes rows incrementally to Excel in write-only mode to reduce memory usage.
- `--sleep` helps reduce rate-limit risk by waiting between per-user detail requests.
- If you hit `401/403/429`, refresh your cookie/session and retry.
