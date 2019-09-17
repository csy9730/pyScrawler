import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    # '-F'  单文件打包 ,'-w'
    opts=['ePyqtScrapy.py','--onedir', '--clean', '--hidden-import=queue', "--distpath=dist"
        , '--exclude-module=scikit-learn', '--exclude-module=PySide' , '--exclude-module=win32com'
        , '--exclude-module=pandas', '--exclude-module=PIL', '--exclude-module=matplotlib'
        ,  '--exclude-module=PyQt4'
        ,'--hidden-import=pkg_resources'
        ]
          # '--icon=./qml/zlg.ico', ,'--add-data=qml/zlg.ico;qml','--add-data=smogFakeData.txt;.' '--exclude-module=enum34',
    run(opts)

