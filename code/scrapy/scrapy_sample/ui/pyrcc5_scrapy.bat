pushd %~dp0
start /b pyuic5 mainwindow3.ui -o ui_mainwidow3.py
start /b pyuic5 formparam.ui -o ui_formparam.py
start /b pyuic5 formsubparam.ui -o ui_formsubparam.py
start /b pyuic5 formstart.ui -o ui_formstart.py
start /b pyuic5 mainwindow.ui -o ui_mainwidow.py
echo "pyuic5 finished"
pyrcc5  pyscr.qrc -o  pyscr_rc.py
echo "pyrcc5 finished"
echo "finished"
popd
