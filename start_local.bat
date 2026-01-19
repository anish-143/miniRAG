@echo off
cd /d "%~dp0"
echo Starting Mini RAG Application...
echo.
echo Server will be available at: http://localhost:8000
echo UI will be available at: http://localhost:8000/ui
echo.
echo Press Ctrl+C to stop the server
echo.

..\..\.venv\Scripts\python.exe -m backend.app
pause
