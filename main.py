from browser import create_browser
from reservation import Reservation
from notifier import Notifier
from datetime import datetime

import time
import config
import config_local
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def send_message(notifier, results):
    try:
        now = datetime.now().strftime("%H:%M:%S")
        message = f"🚌 좌석 발견!\n확인 시간: {now}\n"

        for result in results:
            message += f"{result['time']} - {result['remain']}\n"

        logger.info(message)
        notifier.send(message)
    except Exception as e:
        logger.error(f"메시지 전송 실패: {e}")

def main():
    notifier = Notifier("escape_alerts")

    playwright, browser, page = create_browser()

    reservation = Reservation(page)

    reservation.open()

    reservation.select_date(config.DATE)
    #reservation.select_theme(config.THEME_NAME)

    #result = reservation.check_time(config.TARGET_TIME)
    result = reservation.search_time(config.THEME_NAME, config.START_TIME, config.END_TIME)

    for item in result:
        print(item)

    flag = reservation.click_reservation(config.THEME_NAME, result[0]["time"])
    if flag:
        reservation.fill_reservation_form(
            config_local.NAME,
            config_local.PHONE_NUMBER,
            config_local.EMAIL
        )
    '''
    sleep_time = 2  # 2초 대기
    while(True):
        results = reservation.check_time(config.TARGET_TIME)
        if results:
            send_message(notifier, results)
            sleep_time = 10  # 좌석 발견 시 대기 시간 증가
        else:
            sleep_time = 2  # 좌석 미발견 시 대기 시간 초기화
            now = datetime.now().strftime("%H:%M:%S")
            message = f"🚌 좌석 미발견!\n확인 시간: {now}\n"
            logger.info(message)
        time.sleep(sleep_time)  # 지정된 시간 대기
        reservation.refresh()
    '''

    input("예매 과정을 확인한 후 Enter를 누르세요.")

    browser.close()
    playwright.stop()


if __name__ == "__main__":
    main()