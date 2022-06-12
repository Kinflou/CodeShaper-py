## System Imports
import logging
from logging import Handler


## Application Imports


## Library Imports
from events import Events


class TailLogHandlerEvents(Events):
    
    __events__ = ('on_emit',)


class TailLogHandler(Handler):
    
    def __init__(self):
        super().__init__()
        
        self.events = TailLogHandlerEvents()

    def emit(self, record):
        self.events.on_emit(self.format(record))


def Initialize():
    logger = logging.getLogger('applog')
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s\n')
    
    log_handler = TailLogHandler()
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)
