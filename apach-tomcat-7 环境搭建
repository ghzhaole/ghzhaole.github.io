# 环境

### JDK 1.7
**下载地址**：链接：[https://pan.baidu.com/s/1npzuJSLc8BRg-KUL2HqyuA](https://pan.baidu.com/s/1npzuJSLc8BRg-KUL2HqyuA) 提取码：5bzq 

**安装（linux）**：

1. 直接解压（`tar -zxvf jdk7u79linuxx64.tar.gz`）
2. 添加环境变量：
```
export JAVA_HOME=/java/jdk7
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
```
3. 验证jdk是否安装成功

### apach tomcat 7.0
**下载地址**：[https://tomcat.apache.org/download-70.cgi](https://tomcat.apache.org/download-70.cgi)，下载Core下的安装文件
windows下载对应的版本（32-bit/64-bit Windows Service Installer），linux下载tar打包文件（tar.gz）

**安装（linux）**：

1. 直接解压（`tar -zxvf apache-tomcat-7.0.93.tar.gz`）
2. 打开 /bin/startup.sh，添加java环境
```
export JAVA_HOME=/java/jdk7
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
export TOMCAT_HOME=/opt/apache-tomcat-7.0.93
```
3. 打开 shutdown.sh，添加java环境
```
export JAVA_HOME=/java/jdk7
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
export TOMCAT_HOME=/opt/apache-tomcat-7.0.93
```
4. 开启tomcat
```
cd bin
./startup.sh
```
提示开启成功后，打开浏览器，输入：`http://localhost:8080/`，出现tomcat页面即安装并启动成功。

5. 网站都存放在 webapps 目录下
