@echo off
:: DO NOT RUN SCRIPT VIA GPO!!!

set /p _ASSET=Asset Tag#:
echo set _ASSET=%_ASSET% > C:\Users\Public\ASSET.bat
if exist C:\Users\Public\ASSET.bat attrib +H C:\Users\Public\ASSET.bat
