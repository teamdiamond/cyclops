:: cyclops_cav1.bat
:: runs and example cyclops configuration on windows


SET PATH=%CD%\..\qtlab\3rd_party\Console2\;%PATH%
SET PATH=C:\Console\
SET QT_API=pyqt
:: SET PATH=C:\Qt\2010.02.1\qt\bin;C:\Qt\2010.02.1\bin;C:\Qt\2010.02.1\mingw\bin;%PATH%


:: Check for version of python
IF EXIST c:\python27\python.exe (
    SET PYTHON_PATH=c:\python27
    GOTO mark1
)
IF EXIST c:\python26\python.exe (
    SET PYTHON_PATH=c:\python26
    GOTO mark1
)
IF EXIST C:\Canopy\User\Scripts\python.exe (
    echo found python
    SET PYTHON_PATH=C:\Canopy\User\scripts
    GOTO mark1
)
:mark1

:: Run Cyclops
:: check if version >= 0.11

IF EXIST "%PYTHON_PATH%\ipython-script.py" (
    start Console -w "Cyclops" -r "/k %PYTHON_PATH%\python.exe %PYTHON_PATH%\ipython-script.py --gui=gtk -i source/start_cyclops.py cav1_scanning.py"
    GOTO EOF
)

IF EXIST "%PYTHON_PATH%\scripts\ipython-script.py" (
    start Console -w "Cyclops" -r "/k %PYTHON_PATH%\python.exe %PYTHON_PATH%\scripts\ipython-script.py --gui=gtk -i source/start_cyclops.py cav1_scanning.py"
    GOTO EOF
)

:: check if version < 0.11
IF EXIST "%PYTHON_PATH%\scripts\ipython.py" (
    start Console -w "Cyclops" -r "/k %PYTHON_PATH%\python.exe %PYTHON_PATH%\scripts\ipython.py -gthread -p sh source/start_cyclops.py cav1_scanning.py "
    GOTO EOF
)

echo Failed to run cyclops_cav1.bat
pause
:EOF


:: use this for python 2.6/ipython 0.10
:: start Console -w "Cyclops" -r "/k c:\python27\python c:\python27\scripts\ipython-script.py --q4thread -p sh source/start_cyclops.py scan_example.py"

::start Console -w "Cyclops" -r "/k c:\python27\python c:\python27\scripts\ipython-script.py -i source/start_cyclops.py scan_example.py"

:: c:\python27\python.exe source/start_cyclops.py scan_example.py
::exit
