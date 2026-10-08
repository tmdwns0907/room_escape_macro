import requests
import config
import config_local

def main():
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


if __name__ == "__main__":
    main()