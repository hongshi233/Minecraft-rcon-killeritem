from configparser import ConfigParser
from rcon.source import Client
import time
import re
from typing import List
import logging

# 配置日志
logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.INFO
)

def load_config(config_path: str = 'config.ini') -> dict:
    """加载配置文件"""
    conf = ConfigParser()
    conf.read(config_path)
    return {
        'host': conf['conf']['host'],
        'port': conf['conf'].getint('port'),
        'password': conf['conf']['passwd']
    }

def send_commands(client: Client, commands: List[tuple]) -> None:
    """发送命令序列"""
    for cmd, delay in commands:
        try:
            response = client.run(cmd)
            logging.info(f"Sent command: {cmd} | Response: {response}")
            time.sleep(delay)
        except Exception as e:
            logging.error(f"Command failed: {cmd} | Error: {str(e)}")

def extract_numbers(s: str) -> int:
    """从字符串中提取数字"""
    numbers = re.findall(r'\d+', s)
    return int(numbers[0]) if numbers else 0

def main_loop(config: dict) -> None:
    """主循环逻辑"""
    # 预定义命令序列
    announcement_commands = [
        ('tellraw @a "即将清理凋落物"', 1),
        ('tellraw @a "30秒后清理凋落物"', 10),
        ('tellraw @a "20秒后清理凋落物"', 10),
        ('tellraw @a "10秒后清理凋落物"', 5),
        ('tellraw @a "5秒后清理凋落物"', 5),
    ]

    while True:
        try:
            with Client(config['host'], config['port'], passwd=config['password']) as client:
                # 发送预公告
                send_commands(client, announcement_commands)

                # 执行清理命令
                kill_response = client.run('kill @e[type=item]')
                logging.info(f"清理命令响应: {kill_response}")

                # 发送清理结果
                count = extract_numbers(kill_response)
                result_cmd = f'tellraw @a "清理了 {count} 个凋落物"'
                client.run(result_cmd)
                logging.info(f"清理完成，数量: {count}")

                # 等待下一个周期（总间隔60秒）
                time.sleep(24)

        except Exception as e:
            logging.error(f"连接异常: {str(e)}")
            time.sleep(10)  # 异常后等待时间

if __name__ == "__main__":
    try:
        config = load_config()
        logging.info("RCON清理程序启动")
        logging.info(f"连接到 {config['host']}:{config['port']}")
        main_loop(config)
    except KeyboardInterrupt:
        logging.info("程序已手动终止")
    except Exception as e:
        logging.error(f"致命错误: {str(e)}")