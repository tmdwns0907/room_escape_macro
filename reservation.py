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

        self.page.locator("#dp1790484921795").click()
        for i in range(months_diff):
                    self.page.get_by_title("Next").click()
        self.page.get_by_role("link", name=day).click() 

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
