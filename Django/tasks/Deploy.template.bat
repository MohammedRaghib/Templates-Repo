@echo off
REM ================================
REM  Deploy Django
REM ================================

set "PROJECT_DIR=D:\"
set "VENV_DIR=%PROJECT_DIR%\env"
set "PORT="
set FOR_DISABLE_CONSOLE_CTRL_HANDLER=T

cd /d "%PROJECT_DIR%"

REM Activate venv
call "%VENV_DIR%\Scripts\activate.bat"

REM Use venv python explicitly
"%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade pip
if exist requirements.txt (
    "%VENV_DIR%\Scripts\python.exe" -m pip install -r requirements.txt
)

"%VENV_DIR%\Scripts\python.exe" manage.py migrate --noinput
"%VENV_DIR%\Scripts\python.exe" manage.py collectstatic --noinput

REM Start Waitress and log output
"%VENV_DIR%\Scripts\python.exe" -u -m waitress --listen=127.0.0.1:%PORT% --threads=24 proj.wsgi:application > logs/server.log 2>&1