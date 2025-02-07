cd /D "D:\PycharmProjects\website-checker\src"
echo %cd%
call conda activate website-checker311
python.exe "main.py" %1
if NOT ["%errorlevel%"] == ["0"] pause