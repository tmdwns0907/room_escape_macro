import logging
from datetime import date

logger = logging.getLogger(__name__)

class Reservation:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://showroom404.com/booking/")
        
        self.page.get_by_role("button", name="Close").click()

    def select_date(self, start_date):
        year, month, day = start_date.split("-")
        today = date.today()
        months_diff = (int(year) - today.year) * 12 + (int(month) - today.month)

        self.page.locator("input.datepicker").click()
        for i in range(months_diff):
            self.page.get_by_title("Next").click()
        self.page.get_by_role("link", name=day, exact=True).click() 
        self.page.locator(".theme1-detail-info").first.wait_for()
        logger.debug(
            f"날짜 시간표 로딩 완료 / 테마 개수: "
            f"{self.page.locator('.theme1-detail-info').count()}"
        )

    def select_theme(self, theme_name):
        dropdown = self.page.locator(".theme-dropdown")
        dropdown.locator(".select-styled").click()

        option = dropdown.locator(
            ".select-options li",
            has_text=theme_name
        )
        option.click()

        logger.debug(f"selected theme: {theme_name}")

        self.page.locator(
            ".theme1-detail-info",
            has=self.page.locator("h2", has_text=theme_name)
        ).locator("a[data-time]").first.wait_for()
        logger.debug("테마 로딩 완료")
        
    def check_time(self, target_time):
        result = []

        themes = self.page.locator(".theme1-detail-info").all()

        for theme in themes:
            name = theme.locator("h2").inner_text().strip()
            theme_id = theme.locator('input[name="id"]').input_value()

            slot = theme.locator(f'a[data-time="{target_time}"]')

            if slot.count() == 0:
                continue

            class_name = slot.get_attribute("class") or ""

            result.append({
                "name": name,
                "id": theme_id,
                "time": target_time,
                "available": "submit" in class_name
            })

        return result

    def search_time(self, theme_name, start_time, end_time):
        result = []

        themes = self.page.locator(".theme1-detail-info")

        logger.debug(f"테마 개수: {themes.count()}")

        for i in range(themes.count()):
            theme = themes.nth(i)
            name = theme.locator("h2").inner_text().strip()

            logger.debug(f"테마: {name}")

            if name != theme_name:
                continue

            theme_id = theme.locator('input[name="id"]').input_value()

            slots = theme.locator("a[data-time]")

            logger.debug(f"{name} 슬롯 개수: {slots.count()}")

            for i in range(slots.count()):
                slot = slots.nth(i)

                time = slot.get_attribute("data-time")
                class_name = slot.get_attribute("class") or ""

                try:
                    time_num = int(time.replace(":", ""))
                except (ValueError, TypeError):
                    logger.debug(f"{time} 정수로 변환할 수 없습니다.")
                    continue

                if (
                    "submit" in class_name
                    and int(start_time) <= time_num <= int(end_time)
                ):
                    result.append({
                        "name": name,
                        "id": theme_id,
                        "time": time
                    })

            break

        return result

    def click_reservation(self, theme_name, target_time):
        theme = self.page.locator(
            ".theme1-detail-info",
            has=self.page.locator("h2", has_text=theme_name)
        )

        slot = theme.locator(f'a[data-time="{target_time}"]')

        class_name = slot.get_attribute("class") or ""

        if "submit" not in class_name:
            return False

        slot.click()
        return True

    def fill_reservation_form(self, name, phone_number, email, player):
        self.page.locator("#player_name").fill(name)

        phone = self.page.locator("#phone")

        phone.fill("")
        phone.press_sequentially(phone_number)

        self.page.wait_for_timeout(500)

        self.page.locator("#email").fill(email)

        dropdown = self.page.locator(".no_of_player")
        dropdown.locator(".select-styled").click()
        dropdown.locator(
            ".select-options li",
            has_text=player
        ).click()

        self.page.locator("#default-checkbox-checked").check()

        self.page.locator("#confirm_booking").click()