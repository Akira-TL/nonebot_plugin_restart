import json

from nonebot.log import logger

def debug(text:str):
    '''
    @说明:
        对官方debug方法的扩写,将文件地址写入debug消息方便查看日志
    @返回:
        none
    '''
    logger.debug('\033[95m' + __name__[12:] + '\033[0m | ' + str(text))