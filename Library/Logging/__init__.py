## System Imports
import logging
import collections


## Application Imports


## Library Imports

class TailLogHandler(logging.Handler):

    def __init__(self, log_queue):
        logging.Handler.__init__(self)
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.append(self.format(record))


class TailLogger(object):

    def __init__(self, maxlen):
        self._log_queue = collections.deque(maxlen=maxlen)
        self._log_handler = TailLogHandler(self._log_queue)

    def contents(self):
        return '\n'.join(self._log_queue)

    @property
    def log_handler(self):
        return self._log_handler


def Initialize():
    logger = logging.getLogger(__name__)
    
    tail = TailLogger(10)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    log_handler = tail.log_handler
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    
    logger.setLevel(logging.DEBUG)

