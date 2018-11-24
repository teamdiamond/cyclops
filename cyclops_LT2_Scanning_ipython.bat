:: cyclops_example.bat
:: runs and example cyclops configuration on windows


:: SET PATH=%CD%\..\qtlab\3rd_party\Console2\;%PATH%
SET PATH=C:\Console2\;%PATH%

SET QT_API=pyqt
:: SET PATH=C:\Qt\2010.02.1\qt\bin;C:\Qt\2010.02.1\bin;C:\Qt\2010.02.1\mingw\bin;%PATH%

:: use this for python 2.6/ipython 0.10
:: start Console -w "Cyclops" -r "/k c:\python27\python c:\python27\scripts\ipython-script.py --q4thread -p sh source/start_cyclops.py scan_example.py"


::SET PYTHON_PATH=C:\DOCUME~1\localadmin\LOCALS~1\APPLIC~1\Enthought\Canopy32\User\Scripts
SET PYTHON_PATH=C:\Canopy\User\scripts
:: use this for python27 with ipython 0.11
start Console -w "Cyclops::LT2 Scanning" -r "/k %PYTHON_PATH%\python.exe %PYTHON_PATH%\ipython-script.py -i source/start_cyclops.py lt2_scanning.py"

:: c:\python27\python.exe source/start_cyclops.py scan_example.py
exit
