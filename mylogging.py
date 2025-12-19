import logging
import time
# logging.basicConfig(level=logging.DEBUG)


# logger = logging.getLogger("mohamed ramadan ")
# # logger.info("you have 3 girls ringing on your phone ")
# # logger.critical("watch out you gonna die ")
# # logger.log(logging.ERROR,"this not your business ")
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler("mylogfile.log")
# formatter = logging.Formatter("%(levelname)s - %(asctime)s : %(message)s")
# handler.setFormatter(formatter)
# handler.setLevel(logging.INFO)
# logger.addHandler(handler)
# logger.debug("this for you ")
# logger.info("this from me ")


# logging.basicConfig(level=logging.INFO,filename="log.log",filemode="w",
# format="%(asctime)s - %(levelname)s - %(message)s" )
# logger = logging.getLogger(__name__)
# handler = logging.FileHandler("mylog.log",mode="w")
# formatter = logging.Formatter("%(asctime)s -%(name)s - %(levelname)s - %(message)s")
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.info("press like button")
# logging.debug("debug ")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
# logging.basicConfig(level=logging.DEBUG,filename="mohamed.log",filemode="w",format="%(asctime)s - %(levelname)s - %(message)s ")
logging.info("hello mohamed")
# logging.debug("hello yousseff")
# logging.warning("that's enough")
# logging.error("that's my error ")


logging.critical("that's my critical ")
logger = logging.getLogger("romio")
logger.setLevel(logging.DEBUG)
conssolehandler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ",datefmt="%D-%M-%Y %H:%M:%S")
conssolehandler.setFormatter(formatter)
try:
    x = 1 //0 
except ZeroDivisionError as e : 
    logger.error("this error occured ",exc_info=e)
print("hello world ")