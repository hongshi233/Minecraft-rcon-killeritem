# Minecraft RCON 凋落物清理脚本
### 说明
本项目使用原版提供的RCON(远程控制台协议),在1.9	pre4	加入了RCON\
为解决无法使用插件的服务器提供帮助
### 使用方法
请将服务的文件夹下的server.properties中的enable-rcon=false 设为true
```
enable-rcon=true
```
并配置\
rcon.port=[您所想使用的RCON端口]\
rcon.password= [RCON服务密码] 强烈建议使用强密码，防止被爆破破坏服务器造成损失\
\
示例：
```
rcon.port=25577
rcon.password=114514
```
