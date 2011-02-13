:: cyclops_example.bat
:: runs and example cyclops configuration on windows

SET PATH=%CD%\..\3rd_party\gtk\bin;%CD%\..\3rd_party\gtk\lib;%PATH%
SET GTK_BASEPATH=%CD%\..\3rd_party\gtk
SET PATH=%CD%\..\3rd_party\Console2\;%PATH%
SET PATH=C:\Qt\2010.02.1\qt\bin;C:\Qt\2010.02.1\bin;C:\Qt\2010.02.1\mingw\bin;%PATH%

start Console -w "Cyclops" -r "/k c:\python26\python c:\python26\scripts\ipython.py -gthread -p sh source/cyclops.py scan_example.py"

:: c:\python26\python.exe source/cyclops.py scan_example.py
exit