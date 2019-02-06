for /f "tokens=20-30 skip=1 delims=," %%a in ('systeminfo /fo csv') do ( set _mdate= %%a)
echo Manufacturing,%_mdate:~0,-1%