from pydantic import BaseSettings

from nonebot import get_driver
global_config = get_driver().config.dict()
class Config(BaseSettings):
    nickname = global_config['nickname']
    pass
    # Your Config Here


configs = Config()