from logging import (
    basicConfig,
    INFO,
    info
)


def set_log(msg: str):
    basicConfig(
        level=INFO,
        filename='log/application.log',
        filemode='w'
    )
    return info(msg)
