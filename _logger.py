import sys
import time
from loguru import logger
from pathlib import Path

class LogInitialization:
    def __init__(self):
        project_path = Path.cwd()
        log_path = Path(project_path, "log")
        t = time.strftime("%Y%m%d")

        logger.remove()
        logger.add(sys.stderr
                    ,format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> <level>[{level}] [{file.name}:{line}]: {message}</level>"
                    ,enqueue=True)

        logger.add("{}/record_{}.log".format(log_path,t)
                    ,format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> <level>[{level}] [{file.name}:{line}]: {message}</level>"
                    ,rotation="00:00"
                    ,encoding="utf-8"
                    ,enqueue=True)

# if __name__ == "__main__":
#     LogInitialization()
#     logger.info("info")
#     logger.debug("debug")
#     logger.warning("warning")
#     logger.error("error")