import requests
import config
import config_local
from bs4 import BeautifulSoup

class ReservationAPI:
    BASE_URL = "https://showroom404.com"
    AJAX_URL = f"{BASE_URL}/wp-admin/admin-ajax.php"

    def __init__(self):
        self.session = requests.Session()

    def connect(self):
        """
        예약 페이지에 접속해서 PHP 세션을 생성한다.
        """
        response = self.session.get(
            f"{self.BASE_URL}/booking/",
            verify=False
        )
        response.raise_for_status()

    def search_time(
        self,
        selected_date,
        location_id="15",
        theme_id=""
    ):
        """
        특정 날짜의 예약 가능한 시간을 조회한다.
        """

        data = {
            "action": "filter_rooms",
            "location_id": location_id,
            "theme_id": theme_id,
            "currentDate": selected_date,
        }

        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Referer": f"{self.BASE_URL}/booking/",
        }

        response = self.session.post(
            self.AJAX_URL,
            data=data,
            headers=headers,
            verify=False
        )
        response.raise_for_status()

        return self._parse_time_response(response.text)

    def _parse_time_response(self, html):
        """
        시간 조회 API의 HTML 응답을 파싱한다.
        """

        soup = BeautifulSoup(html, "html.parser")

        result = []

        themes = soup.select(".theme1-detail-info")

        for theme in themes:
            name = theme.select_one("h2")

            if not name:
                continue

            name = name.get_text(strip=True)

            room_id = theme.select_one(
                'input[name="id"]'
            )

            if not room_id:
                continue

            room_id = room_id.get("value")

            slots = theme.select("a[data-time]")

            for slot in slots:
                time = slot.get("data-time")
                class_name = slot.get("class", [])

                result.append({
                    "name": name,
                    "id": room_id,
                    "time": time,
                    "available": "submit" in class_name,
                })

        return result

    def book(
        self,
        player_name,
        mobile_code,
        email,
        selected_date,
        time_slot,
        total_price,
        room_id,
        total_player,
        ph_code="+82",
    ):
        """
        예약을 생성한다.
        """

        data = {
            "action": "enter_details_save_form",
            "player_name": config_local.NAME,
            "mobile_code": config_local.PHONE_NUMBER,
            "email": config_local.EMAIL,
            "selectedDate": config.DATE,
            "time": "60",
            "time_slot": "10:00",
            "total_price": "58000",
            "location_id": "15",
            "theme_id": "",
            "room_id": "653",
            "total_player": "2",
            "ph_code": "+82",
        }

        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Referer": f"{self.BASE_URL}/booking/?step=step2",
        }

        response = self.session.post(
            self.AJAX_URL,
            data=data,
            headers=headers,
            verify=False
        )
        response.raise_for_status()

        result = response.json()

        if not result.get("success"):
            raise RuntimeError(
                f"예약 실패: {result}"
            )

        return result


def main():
    api = ReservationAPI()
    api.connect()

    result = api.search_time("2026-10-21")

    for item in result:
        if item["name"] == "PIG":
            print(item)
    '''
    session = requests.Session()

    # 1. 예약 페이지 접속 → PHPSESSID 생성
    response = session.get(
        "https://showroom404.com/booking/?step=step2",
        verify=False
    )

    print("GET status:", response.status_code)
    print("cookies:", session.cookies.get_dict())

    # 2. 예약 API
    url = "https://showroom404.com/wp-admin/admin-ajax.php"

    data = {
        "action": "enter_details_save_form",
        "player_name": config_local.NAME,
        "mobile_code": config_local.PHONE_NUMBER,
        "email": config_local.EMAIL,
        "selectedDate": config.DATE,
        "time": "60",
        "time_slot": "10:00",
        "total_price": "58000",
        "location_id": "15",
        "theme_id": "",
        "room_id": "653",
        "total_player": "2",
        "ph_code": "+82",
    }

    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://showroom404.com",
        "Referer": "https://showroom404.com/booking/?step=step2",
    }

    response = session.post(
        url,
        headers=headers,
        data=data,
        verify=False
    )

    print("POST status:", response.status_code)
    print("response:", response.text)
    '''


if __name__ == "__main__":
    main()