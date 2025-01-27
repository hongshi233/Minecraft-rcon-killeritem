from configparser import ConfigParser   # Python2中是from ConfigParser import ConfigParser
conf = ConfigParser()  # 需要实例化一个ConfigParser对象

conf.read('config.ini') #设置配置文件
HOST = conf['conf']['host'] #读取配置文件
PORT = conf['conf'].getint('port') #读取配置文件

print("ip",HOST) #输出ip
str;ml = 'tellraw @a "即将清理凋落物"' #下方client.run命令输入""冲突 故使用变量输入，原版命令聊天消息
str;ml1 = 'tellraw @a "30秒后清理凋落物"' #下方client.run命令输入""冲突 故使用变量输入，原版命令聊天消息
str;ml2 = 'tellraw @a "20秒后清理凋落物"' #下方client.run命令输入""冲突 故使用变量输入，原版命令聊天消息
str;ml3 = 'tellraw @a "10秒后清理凋落物"' #下方client.run命令输入""冲突 故使用变量输入，原版命令聊天消息
str;ml4 = 'tellraw @a "5秒后清理凋落物"' #下方client.run命令输入""冲突 故使用变量输入，原版命令聊天消息
str;ml5 = 'tellraw @a "正在清理清理凋落物"' #下方client.run命令输入""冲突 故使用变量输入，原版命令聊天消息
import time
import re
while True: #循环体
 from rcon.source import Client #入口

 with Client(HOST, PORT, passwd=conf['conf']['passwd']) as client: #链接 （ip，端口，密码）
  response = client.run(ml) #执行体
  time.sleep(1)
  print(response)
  response = client.run(ml1) #执行体
  time.sleep(10)
  print(response)
  response = client.run(ml2) #执行体
  time.sleep(10)
  print(response)
  response = client.run(ml3) #执行体
  time.sleep(5)
  print(response)
  response = client.run(ml4) #执行体
  time.sleep(5)
  print(response)
  response = client.run(ml5) #执行体
  print(response)
  kill = client.run('kill @e[type=item]') #执行体
 def extract_numbers(s):
  return re.findall(r'\d+', s)   # 提取数字
 nb = extract_numbers(kill)
 str;m18= ""
 str;ml6 = 'tellraw @a "清理了',nb and '个凋落物"' #下方client.run命令输入""冲突 故使用变量输入，原版命令聊天消息
 response = client.run(m16)
 
 #response = client.run(ml6) #执行体
 print(nb)
 time.sleep(1)
 print(response)
 time.sleep(50) #延时循环
