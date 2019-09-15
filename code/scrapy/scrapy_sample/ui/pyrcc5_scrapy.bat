pushd %~dp0
pyrcc5  pyscr.qrc -o  pyscr_rc.py
echo "pyrcc5 finished"
pause
pyuic5 mainwindow.ui -o ui_mainwidow.py
echo "finished"
pause
popd
