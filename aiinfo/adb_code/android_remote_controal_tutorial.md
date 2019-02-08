# tutorial

## 任务分解

* skill
	* android
		* ob
		* hellowrod
		* shell
		* grep
		* sed
		* uiautomator
	* page
		* adb

* 市面上的产品分析
	* 黑豹
		* 客服系统
			* 语音
			* 图片
			* 文字
		* 电脑控制屏幕，可输入
		* 自动化工作
		* 二维码扫描
		* 批量导入好友
		* 定时任务
		* 定制脚本
	* 侠客
		* 功能
			* 微信多开批量管理
			* 机器人自动回复
			* 聊天记录保存
			* 客户CRM信息记录
			* 批量微信群发
			* 客户微信好友标签
			* 微信一键建群拉人
			* 自动通过好友申请
			* 智能嗅探高级提醒
			* 红包提醒转帐提醒
			* 红包提醒转帐提醒
			* 自动任务
			* 一键朋友圈
		* 定位
		* 屏幕0延时
	* 奥创
	* 聚播
		* 给第三方代加工	
	
	
	
# android remote tutorial
	
## open-stf 控制组件

* [openstf](https://openstf.io/) - [github-stf](https://github.com/openstf/stf)

* what? stf
Smartphone Test Farm 小机器测试框架 - 控制与管理你的真机，在你的浏览器

* 远程控制
* 管理详细目录

![open-stf官网图](https://github.com/openstf/stf/raw/master/doc/7s_usage.gif?raw=true)

* android支持
    * 版本 2.3.3 (SDK level 10) to 9.0 (SDK level 28)
    * wear5.1
    * Fire OS, CyanogenMod, and other heavily Android
* 远程网页控制设备fps30-50[minicap](https://github.com/openstf/minicap)
* 支持在线输入你的键盘
    * 支持元件
    * 复制和黏贴（老设备长按复制到新设备）
* 按键支持[minitouch](https://github.com/openstf/minitouch)
    * 按alt可以做手势动作
    * 支持缩放、旋转
    * 拖放安装**.apk**
* [反向端口映射minirev](https://github.com/openstf/minirev)
    * 直接从设备访问本地服务器，即使它不在同一网络上
* 通过网页，在任何网络中
* 执行指令，实时操作
* 使用adb connect链接android手机
* 通过设备浏览文件
* 支持VNC
* 管理你的设备目录
    * 查看设备是否链接
    * 看谁在试用设备
    * 搜索设备 通过「 phone number, IMEI, ICCID, Android version, operator, product name 」与简单的电源问题
    * 显示闪亮的红屏与标志信息在你需要的机器上
    * 获取电源数据
    * 基本Play商店帐户管理
    * 显示硬件规格
    * 简单的[api](https://github.com/openstf/stf/blob/master/doc/API.md)

# minicap 

提供一个socket接口流，实时屏幕录像数据，输出android驱动。

他是使用道具在大量的程序中，
他试用在STF远程控制中

Minicap 工作在root如果开始adb（sdk28 和android 9.0）

sdk我们构建在9，minicap工作在android开发预览是在一般支持google源码释放，emulator支持

去capturescreen我们当前使用2个方法，来自于android版本我们试用屏幕客户端，提供APi在AOSP，来自于更新版本，试用虚拟显示，选择同样的请求通过提供API这个框架当关闭使用SIMD-enabled [libjpeg-turbo](https://libjpeg-turbo.org/) 和 设置关闭socket 接口，一个计划功能增加允许高级FPSquier试用MediaRecorder和朋友去获取高级的硬件encoding

在原则，任何驱动可能工作，不管到什么程度，实发minicap信赖提供私人的APIs，同样可以不，如果有问题创建github提问给驱动

这个项目内容在两章节他们主要二元这个能构建试用NDK，其他章节共享库这个构建选择SDK等级和选择构建实例在AOSP源码中。
我们要预编译库在回购，但是任何的改变去代码试用这个共享库，
请求一个再编译一次，这个AOSP分支

## 功能

* ANDROID FPS：android老版本能使用FPS android 10-20fps，新系统可以使用30-40 FPS的，但是我们建议水平的试用fps
* 体现和可用但非零延迟。依赖在编码权利和USB转换速度上，他可以最小 他可以使用物理机器最后面的几帧
* 在android 4.2+框架是唯一发布当任何改变时在屏幕，在老的版本框架是发布一个始终的框架，是否改变与框架。

## 要求

* [NDK](https://developer.android.com/tools/sdk/ndk/index.html) Revision 10e（may 2015）
* [MAKE](http://www.gnu.org/software/make/)

## 构建

我们包含了[android-libjpeg-turbo](https://github.com/openstf/android-libjpeg-turbo) 第一个工作是下载它

### LIBJPEG-TURBO FOR android

 [LIBJPEG-TURBO FOR android](https://github.com/openstf/android-libjpeg-turbo)

构建构建NDK和工作与最后版本 NDK版本10e。老版本不能工作，支持X86_64, 主要的内容，NDK15不能支持android 平台SDK版本要高于14.如果NDK平台高于android2.3

提供个工作Android构建libpeg-turbo，他们
是提供个工作android.mk 构建配置在libjpeg-turbo，选择构建你的app与ndk-build而不是诉诸工具链欺骗，马上加入这个仓库

文本：这个仓库是原本创建的一个简单的目的，
去解码jpg文件在不通的NDK项目中。因此JNI绑定不能提供，但是拉请求是欢迎的，任何libjpeg-turbo特性请求作者是定义是支持pull的。

* 定义支持
    * armeabi
    * armeabi-v7a
    * armeabi-v7a-hard
    * arm64-v8a
    * x86
    * x86_64, requires Android NDK Revision 10e (May 2015) or later

* 要求：
    * [Android NDK 10e](https://developer.android.com/ndk/)

### 使用方法

## minicamp 构建

**ndk-build版本：android-ndk-r15c**

下载地址：[ndk-build](https://developer.android.google.cn/ndk/)

1. 下载minicamp源码

```
git clone https://github.com/openstf/minicap.git

```

与minicap项目依赖于libjpeg-turbo

```
git submodule init

git submodule update
```

用ndk-bulid构建

```
ndk-build
```

### 运行

要运行这一步，先完成上面的构建步骤

这个脚本会启动 系统配置，如果有多个设备，请设置android版本，最好打开**run.sh**看看里面的脚本

```
# 运行测试是否可工作
./run.sh autosize -t
# 运行测试
./run.sh autosize -h
# 启动 minicap
./run.sh autosize
```


这个autosize指令是选择指定的屏幕尺寸自动调节。完成后而不是二进制本身。理解他很有必要，下面是手册


判断设备CPU的ABI

```
ABI=$(adb shell getprop ro.product.cpu.abi|tr -d'\r')
```
$ABI是对应的版本

推送
```
adb push libs/$ABI/minicap /data/local/tmp/
```

获取SDK对应的版本

```
SDK=$(adb shell getprop ro.build.version.sdk|tr -d'\r')
```

推送minicap.so文件

```
adb push jni/minicap-shared/aosp/libs/android-$SDK/$ABI/minicap.so /data/local/tmp/

adb push jni/minicap-shared/aosp/libs/android-19/armeabi-v7a/minicap.so /data/local/tmp/
```

每次启动minicap我们需要设置LD_LIBRARY_PATH，不然会提醒找不到公共库的参数：

-p参数：

{RealWidth}x{RealHeight}@{VirtualWidth}x{VirtualHeight}/{Orientation}

可以指定采集的实际大小、虚拟大小以及屏幕方向，实际大小一般设置成设备物理分辨率大小，虚拟大小是通过socket接口发送的大小，屏幕实际窗口大小我们可以通过adb命令获取；

```
adb shell dumpsys window | grep -Eo 'init=\d+x\d+' | head -1 | cut -d= -f 2
```

启动minicap，下面获取实际大小是1080x1920，需要发送窗口大小是540*960 采用纵向屏幕

```
adb shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1080x1920@1080x1920/0

```

端口转发，通过adb forward命令，可以把minicap端口映射到我们PC指定的端口，localabstract:minicap是UNIX域名的SOCKET名称，把minicap的socket端口映射到PC的1313端口，这样我们就可以在PC通过连接1313端口获取到设备的实时视频流；

```
adb forward tcp:1313 localabstract:minicap
```

现在你可以用本地socket使用本地local端口,测试一次链接，

```
nc localhost 1313
```

### 运行web

进入example中运行 node .app.js

```
cd example
node app.js
```


打开

```
localhost:9002
```

### minicap协议解析

minicap启动并用adb forward命令映射端口后，我们就可以通过socket与minicap建立连接。

#### Global header

minicap协议是二进制流推送流协议

一旦与minicap建立连接，minicap首先会推送长度24字节的global header，global header只会推送一次，后续推送的数据不会再报考global header，而是不断推送图片流数据。直到socket连接关闭

![](http://xccimg.zhess.com/20190121211547_OWCJRW_Screenshot.jpeg)


* Global header说包含信息
    * Minicap 版本信息
    * 头长度
    * 实际大小
    * 虚拟大小
    * 设备方向


下面是python代码

```python
def parse_hearder(self):
    header = None
    if len(self.framearray)> self.GLOBAL_HEADER_SIZE:
        header = self.framearray[0:self.GLOBAL_HEADER_SIZE]
        del self.framearray[0:self.GLOBAL_HEADER_SIZE]
    return header
```

* Frame binary format

每帧图片流包含2部分信息 0-3字节表示图片长度n，
4个字节的32位整数小端格式存储；4-(n+4)字节，是具体的图片数据，由JPG格式存储，

关键数据：

![](http://xccimg.zhess.com/20190121212132_iunKCm_Screenshot.jpeg)


python 代码

```python
def parse_frameheader(self):
    frameheader = None
    if len(self.framearray)>self.FRAME_HEADER_SIZE:
        frameheader = self.framearray[0:self.FRAME_HEADER_SIZE]
        del self.framearray[0:self.FRAME_HEADER_SIZE]
    return frameheader

def parse_frame(self, framesize):
    frame = None
    if len(self.framearray) > framesize:
        frame = self.framearray[0:framesize]
        del self.framearray[0:framesize]
    return frame
```


### 图片大小

至此，我们完成minicap协议的解析，并获取到minicap推送过来的每一帧图片。需要注意的是，由于minicap是实时推送流，因此流的数据可能会比较大，客户端获取的buffer需要尽可能的大，不然我们在渲染每一帧的时候，可能会出现卡顿的现象，具体多大合适，我们可以稍微推算一下，一张由minicap推送过来的1080x1920大小的png图片，大概是100-200KB，minicap宣称帧率可以达到20 FPS左右，因此我们的buffer可以设置为：200KB * 20 = 4096000字节，每隔一秒recv()一次；

## PYQT渲染

获取图片后，
使用PyQt中的paintEvent进行渲染，
refreshFrame()方法，关联获取图片线程中的一个信号槽，一旦获取图片线程从minicap解析到每一帧的图片，会通知refreshFrame()中的self.update()方法，selfupdate()方法则会掉调用painEvent进行页面刷新

```python
def paintEvent(self, event):
    if self.frame is not None :
        painter = QPainter(self)
        pixmap = QPixmap()
        pixmap.loadFromData(self.frame)
        painter.drawPixmap(0,0,Pixmap.scaled(270, 480, QT.IgnoreAspectRatio, QtSemoothTransformation))

def refreshFrame(self, frame):
    self.frame = frame
    self.update()

```


## minitouch

原理：

点击时=发生指令：

```
d <contact> <x> <y> <pressure>
```

压力值

```
m <contact> <x> <y> <pressure>
```

minitouch提供socket接口，实现可以点击与手势，他的工作是在root中执行的，

要求：

* sdk>25
* android>2.33

他可以工作在html5按键事件，和android monkey库。允许你通过屏幕按键


### 构建

需要用到 NDK

我们包含[libevdev](http://www.freedesktop.org/wiki/Software/libevdev/) 因此首先做确认链接他

```
git submodule init
git submodule update
```


然后用ndk-build

```
ndk-build
```

在子目录会出现./libs


### 运行

完成构建后，你试用run.sh脚本运行你的驱动。如果你有很多的设备的话

如果有很多设备 记得加**-s 设备名**

```
ABI=$(adb shell getprop ro.product.cpu.abi | tr -d '\r')
adb push libs/$ABI/minitouch /data/local/tmp/
adb shell /data/local/tmp/minitouch -h
```

你可以看见下面的内容

```
Usage: /data/local/tmp/minitouch [-h] [-d <device>] [-n <name>] [-v] [-i] [-f <file>]
  -d <device>: Use the given touch device. Otherwise autodetect.
  -n <name>:   Change the name of of the abtract unix domain socket. (minitouch)
  -v:          Verbose output.
  -i:          Uses STDIN and doesn't start socket.
  -f <file>:   Runs a file with a list of commands, doesn't start socket.
  -h:          Show help.
```

运行代码 minitouch

```
adb shell /data/local/tmp/minitouch
```

映射端口

```
adb forward tcp:1111 localabstract:minitouch
```


测试端口

```
nc localhost 1111
```

测试脚本是python做的。

```python
import socket
BUF_SIZE = 1024
server_addr = ('127.0.0.1', 1111)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_addr)
data = '''
d 0 150 150 50\n
'''
datas = data.encode()
client.sendall(datas)
```




