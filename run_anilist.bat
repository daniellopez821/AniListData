@echo off
cd /d C:\Users\dl032\PyCharmMiscProject

call C:\Users\dl032\PyCharmMiscProject\.venv\Scripts\activate.bat

python anilist_top10.py >> script_log.txt 2>&1

exit