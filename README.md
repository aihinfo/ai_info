# about ai_info

* ai_info最初是为了测试想法：
  * 如何以api的形式与其他群好友协作完成目标任务。
  * 记录自己的思考、记录、行动


* 语言：
    * js electron

* 核心流程

* [ ] gui 
    * [ ] 左侧树型结构 **treejs(可拖拽)**
        * [ ] 如果有新设备，自动添加（有检测循环语句）if have new devices ，auto add devices（check loop）
        * [ ] 「双击」后打开设备打开独立窗口显示页面 doubel click open new view  show devices 
    * [ ] 右侧显示listview用<canvas>加socket读取渲染图片
        * [ ] 右键 - 选择「打开手机」，后打开设备打开独立窗口独立窗口显示页面 click open new view  show devices 
    * [ ] 检测新设备的方法：bash shell adb检测是否有新的设备，如果有执行代码（代码开启设备上的websocket端口）
    * [ ] 开个线程检测shell线程（指令端）。
    * [ ] 左侧的tree（用刚给你的代码）
    * [ ] 右侧的view（栅格化）
		* [ ] （链接 刚给的html和js代码websocket代码）
		* [ ] 如果shell有新设备，加一个栅格并渲染上去
 
 
 
 ## gui
 
![](http://xccimg.zhess.com/20190207205348_yMPmOl_Screenshot.jpeg)
 
[参考视频教材](http://www.hb-qk.com/video.html)


### 双击后打开设备打开独立窗口显示页面 doubel click open new view  show devices 

![](https://github.com/openstf/stf/raw/master/doc/7s_usage.gif)
 

![](http://xccimg.zhess.com/20190207210700_50hpGe_Screenshot.jpeg)
