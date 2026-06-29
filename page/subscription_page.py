import allure


class SubscriptionPage():

    def __init__(self, page) -> None:
        self.page = page

        self.basic_tariff = page.get_by_test_id("tariff-basic")
        self.premium_tariff = page.get_by_test_id("tariff-premium")
        self.familly_tariff = page.get_by_test_id("tariff-family")

        self.promo_input = page.locator(".promo-input")
        self.promo_apply_btn = page.get_by_text("Применить")
        self.promo_massage = page.get_by_test_id("promo-message")

        self.card_number = page.locator("#card-number-input")
        self.card_expiry = page.locator("#card-expiry-input")
        self.card_cvv = page.locator("#card-cvv-input")

        self.summary_section = page.locator(".summary-section")

        self.submit_btn = page.get_by_role("button", name="Подключить за")

        self.success_modal = page.get_by_test_id("success-modal")
        self.card_errors = page.get_by_test_id("card-errors")

    @allure.step("Открыть страницу подписки")
    def open(self) -> None:
        self.page.goto("/automation-lab/subscription")

    @allure.step("Выбрать тариф 'Базовый'")
    def select_basic_tariff(self) -> None:
        self.basic_tariff.click()

    @allure.step("Выбрать тариф 'Премиум'")
    def select_premium_tariff(self) -> None:
        self.premium_tariff.click()

    @allure.step("Выбрать тариф 'Семейный'")
    def select_familly_tariff(self) -> None:
        self.familly_tariff.click()

    @allure.step("Применить промокод: {promo_code}")
    def apply_promo(self, promo_code) -> None:
        self.promo_input.fill(promo_code)
        self.promo_apply_btn.click()

    def get_promo_massege(self) -> str:
        return self.promo_massage.text_content()

    @allure.step("Заполнить данные карты")
    def fill_card(self, card_number: str, expiry: str, cvv: str) -> None:
        self.card_number.fill(card_number)
        self.card_expiry.fill(expiry)
        self.card_cvv.fill(cvv)

    @allure.step("Нажать кнопку 'Подключить'")
    def submit(self) -> None:
        self.submit_btn.click()
