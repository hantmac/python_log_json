# 测试用例，你可以把get_logger()封装成一个模块，from xxx import get_logger
from python_log_json import get_logger
logger1 = get_logger()
def test():
    try:
        a = 1 / 0
    except Exception as e:
        logger1.error(e)  # 写入错误日志
        #如果需要添加额外的信息，使用extra关键字即可
        logger1.error(e, extra={key1: value1, key2:value2})
        # 其他错误处理代码
        pass
test()
