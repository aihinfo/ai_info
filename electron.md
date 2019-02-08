# think 

## learn weight

* electron-api-demos 入门框架代码
* electron项目
    * camera相机
    * 客户证书
    * cookies
    * 崩溃报告crash-report
    * 桌面获取desktop-capture
    * 文件浏览file-explorer
    * 框架窗口frameless-window
    * 菜单栏menus
    * mini-code-editor小型代码编辑器
    * MP3解码 mp3-encoder
    * 插件pepper-flash-plugin
    * 提醒notifications
    * 能量保存 power-save-blocker
    * 打印printing
    * 服务工作service-worker
    * spell-check拼音检查
    * tray托盘
    * webgl
    * 网页页面webview
    * 主动监控activity-monitor
    * electron-tray托盘
    * hash哈希
    * mirror镜子
    * prices价格
    * url网址

    



# 入门篇

## 第一个程序 


```
npm init
npm install --save-dev electron
```

创建 main.js

```
const { app, BrowserWindow } = require('electron')

// 保持对window对象的全局引用，如果不这么做的话，当JavaScript对象被
// 垃圾回收的时候，window对象将会自动的关闭
let win

function createWindow () {
  // 创建浏览器窗口。
  win = new BrowserWindow({ width: 800, height: 600 })

  // 然后加载应用的 index.html。
  win.loadFile('index.html')

  // 打开开发者工具
  win.webContents.openDevTools()

  // 当 window 被关闭，这个事件会被触发。
  win.on('closed', () => {
    // 取消引用 window 对象，如果你的应用支持多窗口的话，
    // 通常会把多个 window 对象存放在一个数组里面，
    // 与此同时，你应该删除相应的元素。
    win = null
  })
}

// Electron 会在初始化后并准备
// 创建浏览器窗口时，调用这个函数。
// 部分 API 在 ready 事件触发后才能使用。
app.on('ready', createWindow)

// 当全部窗口关闭时退出。
app.on('window-all-closed', () => {
  // 在 macOS 上，除非用户用 Cmd + Q 确定地退出，
  // 否则绝大部分应用及其菜单栏会保持激活。
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  // 在macOS上，当单击dock图标并且没有其他窗口打开时，
  // 通常在应用程序中重新创建一个窗口。
  if (win === null) {
    createWindow()
  }
})

// 在这个文件中，你可以续写应用剩下主进程代码。
// 也可以拆分成几个文件，然后用 require 导入。
```

创建index.html

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Hello World!</title>
  </head>
  <body>
    <h1>Hello World!</h1>
    We are using node <script>document.write(process.versions.node)</script>,
    Chrome <script>document.write(process.versions.chrome)</script>,
    and Electron <script>document.write(process.versions.electron)</script>.
  </body>
</html>
```

创建 package.json

```
{
  "name": "electron-quick-start",
  "version": "1.0.0",
  "description": "A minimal Electron application",
  "main": "main.js",
  "scripts": {
    "start": "electron ."
  },
  "repository": "https://github.com/electron/electron-quick-start",
  "keywords": [
    "Electron",
    "quick",
    "start",
    "tutorial",
    "demo"
  ],
  "author": "GitHub",
  "license": "CC0-1.0",
  "devDependencies": {
    "electron": "^4.0.3"
  }
}
```

## 阅读代码 Electron API Demos

[![](https://cloud.githubusercontent.com/assets/378023/15016148/ae06cc80-124a-11e6-80dd-076d83e492f6.png)](https://cloud.githubusercontent.com/assets/378023/15016148/ae06cc80-124a-11e6-80dd-076d83e492f6.png)

```
git clone https://github.com/electron/electron-api-demos
cd electron-api-demos
npm install
npm start
```

```
git clone https://github.com/hokein/electron-sample-apps
git clone https://github.com/electron/simple-samples

```

运行

```
npm install
npm start
```


示例代码

```
# 克隆这仓库
git clone https://github.com/electron/electron-quick-start
# 进入仓库
cd electron-quick-start
# 安装依赖库
npm install
# 运行应用
npm start
```


```
git clone https://github.com/hokein/electron-sample-apps
npm install -g electron
然后在每个系统中看代码
```

案例代码3
```
git clonehttps://github.com/electron/simple-samples
```


* 全部文档 electronjs.org/docs - all of Electron's documentation
* 创建简单的项目 electronjs.org/community#boilerplates 
* 快速入门 electron/electron-quick-start
* 简单的案例 electron/simple-samples
* 应用教你如何使用 electron/electron-api-demos
* APIs案例项目 hokein/electron-sample-apps 


# 1 教程

## 1.01 关于Electron
## 1.02 可到达Accessibility
## 1.03 Electron 程序反馈程序
## 1.04 Electron 应用架构
## 1.05 应用 Debugging
## 1.06 应用分配
## 1.07 应用分包
## 1.08 验证测试定义驱动
## 1.09 样本文件与CLIs
## 1.10 代码信号
## 1.11 Debugging主程序
## 1.12 Debugging主程序在VSCode
## 1.13 桌面环境整合
## 1.14 安装开发环境


mac、windows、linux 都用[Node.js](https://nodejs.org/en/)

```
# This command should print the version of Node.js
node -v

# This command should print the version of npm
npm -v
```


```
npm init
npm install --save-dev electron
```




## 1.15 DevTools插件
## 1.16 5.0.0 释放时间表
## 1.17 Electron 版本
## 1.18 写你第一个electron应用
## 1.19 发布到macos
## 1.20 安装Installation
## 1.21 快捷键 Keyboard Shortcuts
## 1.22 定制Linux 桌面启动程序
## 1.23 Mac App 商店 提交教程
## 1.24 MacOS Dock
## 1.25 Mojave 黑暗模式
## 1.26 多进程 Multithreading

与[Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
，他是运行JavaScript在底层线程

* Multi-threaded Node.js

使用Node.js在Electron的Web Workers,
webPreferences中nodeIntegrationInWorker设置为true。

```js
let win = new BrowserWindow({
  webPreferences: {
    nodeIntegrationInWorker: true
  }
})
```





## 1.27 本地文件的拖拽 Native File Drag & Drop


## 1.28 提醒功能Notifications (Windows, Linux, macOS)
## 1.29 屏幕外渲染Offscreen Rendering
## 1.30 在线/离线事件发觉 Online/Offline Event Detection
## 1.31 程序条在任务中 Progress Bar in Taskbar (Windows, macOS, Unity)
## 1.32 快速开始Quick Start
## 1.33 最近的文档 Recent Documents (Windows & macOS)
## 1.34 REPL（read读取、eval执行，print打印、loop循环）
## 1.35 获取文件 for macOS BrowserWindows
## 1.36 安全本地能力和你的责任Native Capabilities
## 1.37 责任
## 1.38 Snapcraft 指南 (Ubuntu Software Center & More)
## 1.39 Electron 支持
## 1.40 测试在无头CI系统中 (Travis CI, Jenkins)
## 1.41 测试Widevine CDM 
## 1.42 升级程序 Updating Applications
## 1.43 用本地node模型 Using Native Node Modules
## 1.44 用Pepper Flash 插件
## 1.45 使用Selenium 和 WebDriver
## 1.46 Windows 商店指南
## 1.47 Windows 任务条

# 2 API 参考
## 2.01 加速器Accelerator
## 2.02 应用app
## 2.03 自动升级autoUpdater
## 2.04 API协议
## 2.05 浏览页面 BrowserView
## 2.06 浏览窗口 BrowserWindow
## 2.07 浏览窗口代理 BrowserWindowProxy
## 2.08 支持chrome 指令切换 Supported Chrome Command Line Switches
## 2.09 客户端反馈 ClientRequest
## 2.10 粘贴板clipboard
## 2.11 内容追踪 content Tracing
## 2.12 Cookies
## 2.13 崩溃记录 crash Reporter
## 2.14 Debugger
## 2.15 桌面留场 desktop Capturer
## 2.16 对话 dialog
## 2.17 下载任务 DownloadItem
## 2.18 环境变量 Environment Variables
## 2.19 文件项目 File Object
## 2.20 无框窗口 Frameless Window
## 2.21 全局快捷键 globalShortcut
## 2.22 在应用中发布 inAppPurchase
## 2.23 到达信息IncomingMessage
## 2.24 ipc主要 ipcMain
## 2.25 ipc读取 ipcRenderer
## 2.26 本地Locales
## 2.27 菜单Menu
## 2.28 菜单项MenuItem
## 2.29 本地图片nativeImage
## 2.30 网络net
## 2.31 网络日志netLog
## 2.32 提醒信息Notification
## 2.33 能源监控powerMonitor
## 2.34 能源保存powerSaveBlocker
## 2.35 进程process
## 2.36 礼仪protocol
## 2.37 远程remote
## 2.38 沙盒选项sandbox Option
## 2.39 屏幕screen
## 2.40 会议session
## 2.41 指令shell
## 2.42 摘要Synopsis
## 2.43 系统权限systemPreferences
## 2.44 点击栏TouchBar
## 2.45 点击栏按钮TouchBarButton
## 2.46 点击栏颜色TouchBarColorPicker
## 2.47 点击栏组TouchBarGroup
## 2.48 点击栏标签TouchBarLabel
## 2.49 点击栏松饼TouchBarPopover
## 2.50 点击栏洗刷者TouchBarScrubber
## 2.51 点击栏段控制TouchBarSegmentedControl
## 2.52 点击栏滑动TouchBarSlider
## 2.53 点击栏空间TouchBarSpacer
## 2.54 托盘Tray
## 2.55 网络内容webContents
## 2.56 网络框架webFrame
## 2.57 网络反馈WebRequest
## 2.58 <webview> Tag
## 2.59 window.open打开方法window.open Function

# 3 API结构
## 3.01 蓝牙驱动项目BluetoothDevice Object
## 3.02 证书Certificate Object
## 3.03 证书负责CertificatePrincipal Object
## 3.04 Cookie Object
## 3.05 CPU使用CPUUsage Object
## 3.06 碰撞报告CrashReport Object
## 3.07 桌面场地源码DesktopCapturerSource Object
## 3.08 显示Display Object
## 3.09 文件检索FileFilter Object
## 3.10 GPU状态GPUFeatureStatus Object
## 3.11 IO计数器IOCounters Object
## 3.12 跳表分类 JumpListCategory Object
## 3.13 跳列项 JumpListItem Object
## 3.14 内存信息 MemoryInfo Object
## 3.15 内存使用详情 MemoryUsageDetails Object
## 3.16 mime类型缓冲 MimeTypedBuffer Object
## 3.17 提醒 NotificationAction Object
## 3.18 指针 Point Object
## 3.19 指针信息 PrinterInfo Object
## 3.20 项目公尺 ProcessMetric Object
## 3.21 生产项目 Product Object
## 3.22 矩形项目 Rectangle Object
## 3.23 介绍人项目 Referrer Object
## 3.24 远程客户端证书 RemoveClientCertificate Object
## 3.25 远程密码 RemovePassword Object
## 3.26 洗刷者组 ScrubberItem Object
## 3.27 信号控制 SegmentedControlSegment Object
## 3.28 快捷键详情 ShortcutDetails Object
## 3.29 大小 Size Object
## 3.30 流协议响应StreamProtocolResponse Object
## 3.31 项目Task Object
## 3.32 Thumbar 按钮 ThumbarButton Object
## 3.33 获取分类和设置 Trace Categories And Options Object
## 3.34 获取配置 TraceConfig Object
## 3.35 交易Transaction Object
## 3.36 升级Blob UploadBlob Object
## 3.37 升级数据 UploadData Object
## 3.38 升级文件 UploadFile Object
## 3.39 升级行数据 UploadRawData Object
## 3.40 网页源码 WebSource Object


# 4 高级功能
## 4.01 技术的区别Electron and NW.js (formerly node-webkit)
## 4.02 构建安装包Build Instructions
## 4.03 构建安装包Linux Build Instructions (Linux)
## 4.04 构建安装包macOS Build Instructions (macOS)
## 4.05 构建安装包Windows Build Instructions (Windows)
## 4.06 构建系统概述Build System Overview
## 4.07 Chromium开发 Chromium Development
## 4.08 使用c++代码 Using clang-format on C++ Code
## 4.09 代码风格Coding Style
## 4.10 Debugging on Windows
## 4.11 Debugging on macOS
## 4.12 Debugging with XCode
## 4.13 提问Issues In Electron
## 4.14 提交反馈Pull Requests
## 4.15 开发Electron Developing Electron
## 4.16 释放Releasing
## 4.17 设置系统在debugger Setting Up Symbol Server in Debugger
## 4.18 源码结构 Source Code Directory Structure
## 4.19 测试Testing
## 4.20 升级chromiumUpgrading Chromium
## 4.21 升级crashpad  Upgrading Crashpad
## 4.22 升级Node Upgrading Node
## 4.23 V8开发


# 参考

* 全部文档 electronjs.org/docs - all of Electron's documentation
* 创建简单的项目 electronjs.org/community#boilerplates 
* 快速入门 electron/electron-quick-start
* 简单的案例 electron/simple-samples
* 应用教你如何使用 electron/electron-api-demos
* APIs案例项目 hokein/electron-sample-apps 


