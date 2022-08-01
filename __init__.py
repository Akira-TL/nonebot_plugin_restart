import nonebot
from tomlkit import key
from .config import configs
from .utils import *
from nonebot.params import CommandArg,RawCommand
from nonebot import on_command,get_driver, on_message
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me
from nonebot.log import logger
import json
import re
from nonebot.adapters.onebot.v11 import (
    GROUP_ADMIN,
    GROUP_OWNER,
    Message,
    Event,
    )
def debug(text:str):
    '''
    @说明:
        对官方debug方法的扩写,将文件地址写入debug消息方便查看日志
    @返回:
        none
    '''
    logger.debug('\033[95m' + __name__[12:] + '\033[0m | ' + str(text))

restart = on_command('restart',block=True,permission=SUPERUSER)
@restart.handle()
async def _():
    path = __name__.split('.')
    txt = ''
    for i in path:
        txt += '/' + i
    path = txt + '/restart_file.py'
    debug(txt)
    f = open(path[1:],'w')
    f.close