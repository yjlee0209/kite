import logging

logger = logging.getLogger('phonebook')
hand = logging.FileHandler('phonebook_20200212.log')

                      #          생성시간     로그레벨      프로세스ID   메시지
formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')

# 파일핸들러에 문자열 포메터를 등록
hand.setFormatter(formatter)

logger.addHandler(hand)
logger.setLevel(logging.INFO)

logger.debug('틀렸음!!')
logger.info('확인!!')
logger.warning('경고!!')
logger.error('에러!!')
logger.critical('치명적!!')