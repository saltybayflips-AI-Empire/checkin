"""Copy the canonical check-in page from team-hq into this repo.

ONE canonical file (team-hq/static/checkin.html) serves both roads — the
Team HQ route and this GitHub Pages front door. This script is the only way
index.html here gets updated, so the two can never drift (drift between two
copies of one file is how the 8/10 Slack-lane comment bug happened).

⛔ PUBLISHING IS KHALIL'S GATE. This repo deploys to a PUBLIC GitHub Pages
site under the saltybayflips-ai-empire org (same class as charla) — commit
freely, but `git push` waits for his explicit OK, every time.
"""
import pathlib
import shutil

SRC = pathlib.Path(r"C:\Users\khali\Projects\team-hq\static\checkin.html")
DST = pathlib.Path(__file__).parent / "index.html"

shutil.copy2(SRC, DST)
print(f"copied {SRC.name} -> {DST} ({DST.stat().st_size} bytes)")
print("commit, then WAIT FOR KHALIL before pushing (public Pages site).")
