# Appium



安装JDK

node 

安装Android SDK,

`${ANDROID_HOME}/tools；${ANDROID_HOME}/platform-tools`

``` bash
npm install -g appium

pip install Appium-Python-Client
npm install -g appium-doctor
```





``` bash
javac
node -V
appium
adb shell
```



运行appium-doctor，检测报告如下

![1567695659846](..\img\%5CUsers%5Ccsy_acer_win8%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5C1567695659846.png)

可以发现，报告了ANDROID_HOME和JAVA_HOME为设置，

``` bash
set ANDROID_HOME=C:\Users\admin\AppData\Local\Android\Sdk
set JAVA_HOME="C:\Program Files\Java\jdk1.8.0_171"
```
12

``` bash
WARN AppiumDoctor  ✖ opencv4nodejs cannot be found.
WARN AppiumDoctor  ✖ ffmpeg cannot be found
WARN AppiumDoctor  ✖ mjpeg-consumer cannot be found.
WARN AppiumDoctor  ✖ bundletool.jar cannot be found
```



``` bash
 npm install -g opencv4nodejs  # 注意 ，这里npm会调用msvc15和cmake编译opencv
```

