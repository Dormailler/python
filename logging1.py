import logging

if __name__ == '__main__':
    logger = logging.getLogger("main")
    logging.basicConfig(level=logging.ERROR)

    steam_handler = logging.FileHandler(
        "my.log", mode = "w", encoding="utf-8")
    logger.addHandler(steam_handler)

    logging.debug("디버그")
    logging.info("인포")
    logging.warning("워닝")
    logging.error("에러")
    logging.critical("치명")