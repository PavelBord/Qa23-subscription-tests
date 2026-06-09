import pytest
from playwright.sync_api import Page
from page.subscription_page import SubscriptionPage


@pytest.mark.parametrize(
    "invalid_promo, expected_error", 
    [
        ("BASIC199", "Базовый"),
        ("WELCOME10", "Промокод истек"),
    ]
)
def test_invalid_promo_codes(page: Page, invalid_promo: str,expected_error:str) -> None:
    page.set_viewport_size({"width": 1366, "height": 768}) 

    subscription_page = SubscriptionPage(page)

    subscription_page.open()
    subscription_page.select_premium_tariff()
    subscription_page.apply_promo(invalid_promo)
    message_text = subscription_page.get_promo_massege()
    assert expected_error in message_text
