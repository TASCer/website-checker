cd /D "D:\PycharmProjects\Selenium\src"
echo %cd%
call conda activate Selenium
python.exe "main.py" %1
if NOT ["%errorlevel%"] == ["0"] pause