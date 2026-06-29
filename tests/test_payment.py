import pytest
import allure
from playwright.sync_api import Page, expect
from page.subscription_page import SubscriptionPage


@pytest.mark.parametrize(
    "card_number, cvv, expected_locator_name",
    [
        ("4111 1111 1111 1111", "254", "success_modal"),
        ("5555 5555 5555 4444", "675", "success_modal"),
        ("3782 822463 10005", "1764", "success_modal"),
        ("4000 0000 0000 0002", "765", "card_errors"),
        ("4000 0000 0000 9995", "896", "card_errors")

    ]
)
@allure.epic("Платформа подписок StreamVibe")
@allure.feature("Модуль оплаты")
@allure.story("Проверка валидации тестовых карт")
@allure.severity(allure.severity_level.CRITICAL)
def test_payment_cards(page: Page, card_number: str, cvv: str, expected_locator_name: str) -> None:
    page.set_viewport_size({"width": 1366, "height": 768})
    subscription_page = SubscriptionPage(page)
    subscription_page.open()
    subscription_page.fill_card(
        card_number=card_number, expiry="08/29", cvv=cvv)
    subscription_page.submit()
    locator = {"success_modal": subscription_page.success_modal,
               "card_errors": subscription_page.card_errors}
    expect(locator[expected_locator_name]).to_be_visible()
