# 专为公司开发的自动化测试平台，用于车载娱乐系统的测试
## 介绍
测试工具客户端  
提供界面方便测试人员选择步骤来组织测试场景，并选择要运行的测试场景进行测试，测试结束可直接查看测试报告  

测试工具服务端  
向客户端提供测试用例编写需要的测试步骤信息，保存测试场景到数据库等  

测试脚本工程  
测试场景执行的胶水代码，采用BDD框架

## 采用语言和工具
python3.4  
behave  
pyqt5.5.1  
uiautomator(python版)  
flask  

##服务端部署
###环境准备
####所需软件
* python3.4+
* > flask
* > flask-sqlalchemy
* > sqlalchemy-migrate
* > flask-whooshalchemy
###部署步骤
#### 创建虚拟环境
> mkdir atps  
> python -m venv flask
#### 安装环境所需要的库  

##### windows用户执行以下命令  
> $flask\Scripts\pip.exe install flask  
> $flask\Scripts\pip.exe install flask-sqlalchemy  
> $flask\Scripts\pip.exe install sqlalchemy-migrate  
> $flask\Scripts\pip.exe install flask-whooshalchemy  

##### linux用户执行以下命令
> $flask\bin\pip install flask  
> $flask\bin\pip install flask-sqlalchemy  
> $flask\bin\pip install sqlalchemy-migrate  
> $flask\bin\pip install flask-whooshalchemy  

##### 启动服务端
> 复制服务端工程(flask目录不复制)到atps目录下  
> 修改run.py文件中的ip地址配置
> 在atps目录下运行 $flask\Scripts\python.exe run.py
##客户端部署
###环境准备
####所需软件
* python3.4+
* > requests
* > behave
* > pillow
* > pyserial
* > uiautomator
* pyqt5
* jdk
###部署步骤(以上软件都均已正确安装)
> 新建文件夹atp  
> 将atpc和autotestproject放在atp目录下  
> 打开cmd窗口并进入atpc目录  
> 执行命令$ python run.py打开客户端应用  

## 截图
![mainWindow](http://f.hiphotos.baidu.com/image/pic/item/f703738da97739122eeed3c6f0198618377ae249.jpg)
![editWindow](http://a.hiphotos.baidu.com/image/pic/item/43a7d933c895d1432dbeb2847bf082025baf0748.jpg)
![viewResult](http://f.hiphotos.baidu.com/image/pic/item/6a63f6246b600c335a578f6f124c510fd9f9a16f.jpg)
![settings](http://f.hiphotos.baidu.com/image/pic/item/9922720e0cf3d7caaed86ed1fa1fbe096b63a96f.jpg)
![settings](http://e.hiphotos.baidu.com/image/pic/item/91529822720e0cf303d91f5c0246f21fbe09aa6f.jpg)
