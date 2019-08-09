@echo off
REM INVENTORY_REMOTE_CSV_3.4
REM By William Boy
REM wboyiv@alpinedistrict.org
REM THIS FILE PULLS NEEDED INVENTORY INFORMATION FROM SYSTEM SETTINGS AND SAVES IT TO A REMOTE LOCATION
REM THIS FILE WILL ALSO CHECK EXISTING FILES TO SEE IF INVENTORY ALREADY HAS BEEN TAKEN AND COPY ASSET TAGE 
REM INFORMATIONS FROM THE FILE BEFORE UPDATING THE INFORMATION.

:: sett all variables HERE
:VARS
REM Complex verial set
for /f "skip=2 delims=" %%a in (
	'wmic csproduct get identifyingnumber /format:csv'
) do (
	for /f "tokens=2 delims=," %%b in ("%%a") do (
set _serial=%%b
	))

set _file=%_serial%
set _format=csv
REM leave blank to save file in same location as batch file.
REM File PATH CANNOT contain spaces, so if your path has spaces you will need to change the path 
set _PATH=\\10.72.4.12\TechDrive\InventoryFiles

:ASSETCHECK
if EXIST C:\Users\Public\ASSET.bat GOTO INVENTORY

:ASSETUPDATE
if EXIST "%_PATH%\%_file%.%_format%" FOR /f "skip=2 tokens=1-2 delims=," %%a in (
    %_PATH%\%_file%.%_format%
    ) do (if "%%a"=="asset_tag" (set _atag=%%b))
if EXIST "%_PATH%\%_file%.%_format%" echo set _ASSET=%_atag% > C:\Users\Public\ASSET.bat
if EXIST C:\Users\Public\ASSET.bat attrib +H C:\Users\Public\ASSET.bat

:INVENTORY
:: Pre Script
if EXIST "%_PATH%\%_file%.%_format%" del "%_PATH%\%_file%.%_format%"

:: GET Computer Name
echo computer name,%COMPUTERNAME% >> "%_PATH%\%_file%.%_format%"

:: GET Serial Number
for /f "skip=2 delims=" %%a in (
	'wmic csproduct get identifyingnumber /format:csv'
) do (
	for /f "tokens=2 delims=," %%b in ("%%a") do (
echo serialnumber,%%b
	)) >> "%_PATH%\%_file%.%_format%"

:: GET ASSETTAG (Avalable in v3.2+)
if EXIST "C:\Users\Public\ASSET.bat" call "C:\Users\Public\ASSET.bat"
if EXIST "C:\Users\Public\ASSET.bat" echo asset_tag,%_ASSET% >> "%_PATH%\%_file%.%_format%"
if NOT EXIST "C:\Users\Public\ASSET.bat" echo asset_tag,NO_ASSEST_TAG >> "%_PATH%\%_file%.%_format%"

:: GET Vendor Name
for /f "skip=2 delims=" %%a in (
	'wmic csproduct get Vendor /format:csv'
) do (
	for /f "tokens=2 delims=," %%b in ("%%a") do (
echo computermake,%%b
	)) >> "%_PATH%\%_file%.%_format%"

:: GET Computer Model
for /f "skip=2 delims=" %%a in (
	'wmic csproduct get Name /format:csv'
) do (
	for /f "tokens=2 delims=," %%b in ("%%a") do (
echo computermodel,%%b
	)) >> "%_PATH%\%_file%.%_format%"

:: GET Compuyter CPU
for /f "skip=2 delims=" %%a in (
	'wmic CPU get Name /format:csv'
) do (
	for /f "tokens=2 delims=," %%b in ("%%a") do (
echo CPU,%%b
	)) >> "%_PATH%\%_file%.%_format%"

:: GET OS
for /f "skip=2 delims=" %%a in (
	'wmic OS get Name /format:csv'
) do (
	for /f "tokens=2 delims=," %%b in (
		"%%a"
	) do (
		for /f "tokens=1-3 delims=|" %%c in (
			"%%b"
		) do (echo os,%%c)
	)) >> "%_PATH%\%_file%.%_format%"

:: GET RAM Amount
for /f "tokens=20-30 skip=1 delims=," %%a in ('systeminfo /fo csv') do ( set _ram= %%h,%%i)
echo ram,%_ram% >> "%_PATH%\%_file%.%_format%"

:: GET MANUFACTURING DATE
:: use systeminfo  and check the bios install date.

::Get Harddrive size
for /f "skip=2 delims=" %%a in (
	'wmic diskdrive get size /format:csv'
) do (
	for /f "tokens=2 delims=," %%b in ("%%a") do (
set _HDD=%%b
	))

set _HDD=%_HDD:~0,-9%
echo hdd,%_HDD% >> "%_PATH%\%_file%.%_format%"

:: get macc addressess
:MACADDRESS
for /f "skip=2 delims=" %%a in (
	'wmic nic GET NetConnectionID^,Macaddress^ /format:csv'
) do (
	for /f "tokens=2-4 delims=," %%b in ("%%a") do (
if not "%%c"=="" echo %%c,%%b
	)) >> "%_PATH%\%_file%.%_format%"
