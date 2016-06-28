:: cyclops_example.bat
:: runs and example cyclops configuration on windows

SET PATH=C:\Console\;%PATH%
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

IF EXIST "%PYTHON_PATH%\ipython-script.py" (
    start Console -w "Cyclops" -r "/k %PYTHON_PATH%\python.exe %PYTHON_PATH%\ipython-script.py -i source/start_cyclops.py cavity_scanning.py"
    GOTO EOF
)

:: use this for python27 with ipython 0.11
:: start Console -w "Cyclops" -r "/k c:\python27\python c:\python27\scripts\ipython-script.py -i source/start_cyclops.py cavity_scanning.py"

echo Failed to run Cyclops
pause
:EOF