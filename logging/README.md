# Logging
```
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Start reading database')
# read database here
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here
logger.info('Finish updating records')
```

Appendix
* https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/