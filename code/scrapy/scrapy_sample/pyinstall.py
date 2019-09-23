import  os

"""
  mime.types 和VERSION 一般位于 C:\ProgramData\Anaconda3\Lib\site-packages\scrapy目录下
"""
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    # '-F'  单文件打包 ,'-w'
    opts=['crawl.py','--onedir', '--hidden-import=queue', "--distpath=dist"
        , '--exclude-module=scikit-learn', '--exclude-module=PySide' 
        , '--exclude-module=pandas', '--exclude-module=matplotlib', '--exclude-module=numpy', '--exclude-module=scipy'
        ,  '--exclude-module=PyQt4'
        ,'--hidden-import=pkg_resources','--add-data=ui/VERSION;scrapy','--add-data=scrapy.cfg;.'
,'--add-data=ui/mime.types;scrapy'
        ]
          # '--icon=./qml/zlg.ico', ,'--add-data=qml/zlg.ico;qml','--add-data=smogFakeData.txt;.' '--exclude-module=enum34',
          # '--clean', 
    run(opts)
