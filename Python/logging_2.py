import logging

logger = logging.getLogger('main')
stream_hand = logging.StreamHandler()
logger.addHandler(stream_hand)

logger.setLevel(logging.INFO)
logger.debug('틀렸음!!')
logger.info('확인!!')
logger.warning('경고!!')
logger.error('에러!!')
logger.critical('치명!!')