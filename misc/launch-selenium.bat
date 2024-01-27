cd /D "D:\PycharmProjects\Selenium\src"
echo %cd%
call conda activate Selenium
python.exe "main.py"
if NOT ["%errorlevel%"] == ["0"] pause