@echo off
REM INVENTORY_Tag_CSV-3.6 - saving system info to Remote location and checking for exiting info.
REM By William Boy
REM wboyiv@alpinedistrict.org
REM THIS FILE PULLS NEEDED INVENTORY INFORMATION FROM SYSTEM SETTINGS AND SAVES IT TO A REMOTE LOCATION
REM THIS FILE WILL ALSO CHECK EXISTING FILES TO SEE IF INVENTORY ALREADY HAS BEEN TAKEN AND COPY ASSET TAGE 
REM INFORMATIONS FROM THE FILE BEFORE UPDATING THE INFORMATION.

:: set Global variables HERE
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
REM leave _PATH blank to save file in same location as batch file.
REM File PATH CANNOT contain spaces, so if your path has spaces you will need to change the path 
set _PATH=\\10.72.4.12\TechDrive\InventoryFiles

::Checking to see if netowrk location is avalable, and cool animation
:SERVERCHECK  
color 07
cls
echo Checking Connection to Server.
REM timeout 3 > NUL
REM cls
REM echo Checking Connection to Server..
REM timeout 2 > NUL
REM cls
REM echo Checking Connection to Server...
REM timeout 1 > NUL
ping -n 1 10.72.4.12 | find "Reply" > NUL
if not errorlevel 1 GOTO SERVERUP else GOTO SERVERDOWN

::Server is up and network location is avalable, checking if file exists.
:SERVERUP
timeout 3 > NUL
cls
color 0A
echo Connected to Server
cls
if NOT EXIST "%_PATH%\%_file%.%_format%" GOTO LSET
:: if file exits pull info from file and store as variables, otherwise ask user to input information.
:RSET
if EXIST "%_PATH%\%_file%.%_format%" FOR /f "tokens=1-2 delims=," %%a in (
    %_PATH%\%_file%.%_format%
    ) do (if "%%a"=="ASSET" (set _asset=%%b))
if EXIST "%_PATH%\%_file%.%_format%" FOR /f "tokens=1-2 delims=," %%a in (
    %_PATH%\%_file%.%_format%
    ) do (if "%%a"=="ROOM" (set _room=%%b))
if EXIST "%_PATH%\%_file%.%_format%" FOR /f "tokens=1-2 delims=," %%a in (
    %_PATH%\%_file%.%_format%
    ) do (if "%%a"=="OWNER" (set _owner=%%b))
if EXIST "%_PATH%\%_file%.%_format%" FOR /f "tokens=1-2 delims=," %%a in (
    %_PATH%\%_file%.%_format%
    ) do (if "%%a"=="INSTALLDATE" (set _installd=%%b))

cls
color 06
echo CAUTION: FILE ALREADY EXISTS.
echo Current information on computer.
echo Computer Name: 		%computername%
echo Asset tag Number:	%_asset%
echo Room Number/Name:	%_room%
echo Owner:			%_owner%
echo Install date:		%_installd%

set /p _updateinfo="do you what to update this information Y or n ? " 
if %_updateinfo% ==  n GOTO END

:: ask used information
:LSET
set /p _asset="Asset tag Number: "
set /p _room="Room Number/Name: "
echo "OWNER"
echo "1. CTE"
echo "2. Media"
echo "3. School/Department"
echo "4. Special Ed"
echo "5. Technology"
echo "6. Food Services"
echo "7, Ed Services"
set /p _ownermenu="Owner: "
echo  %_ownermenu%
if %_ownermenu% EQU 1 set _owner=CTE
if %_ownermenu% EQU 2 set _owner=Media
if %_ownermenu% EQU 3 set _owner=School/Department
if %_ownermenu% EQU 4 set _owner=Special Education
if %_ownermenu% EQU 5 set _owner=Technology
if %_ownermenu% EQU 6 set _owner=Food Services
if %_ownermenu% EQU 7 set _owner=Ed Services
if %_ownermenu% GEQ 7 GOTO LSET
if %_ownermenu% LEQ 1 GOTO LSET
set /p _installd="Installed Date(MM/DD/YYY): "

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
echo ASSET,%_asset% >> "%_PATH%\%_file%.%_format%"
::GET ROOM NUMBER/NAME (Avalible in v 3.6+)
echo ROOM,%_room% >> "%_PATH%\%_file%.%_format%"
::GET Owner (Avalible in v 3.6+)
echo OWNER,%_owner% >> "%_PATH%\%_file%.%_format%"
::GET Install Date (Avalible in v 3.6+)
 echo INSTALLDATE,%_installd% >> "%_PATH%\%_file%.%_format%"

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


GOTO END
:: Server was down do not continue until server is back up.
:SERVERDOWN
cls
color 0C
echo Unable to Connect to server.
echo Check Connection and try again.
pause

:END
color 07
exit