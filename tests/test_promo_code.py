import pytest
from playwright.sync_api import Page
from page.subscription_page import SubscriptionPage


@pytest.mark.parametrize("promo_code,expected_message",
                         [("ALWAYS", "Скидка 15%"),
                          ("BASIC199", "Специальная цена 199"),

                          ]
                         )
def test_valid_promo_codes(page: Page, promo_code: str, expected_message: str) -> None:
    subscription_page = SubscriptionPage(page)
    subscription_page.open()
    subscription_page.select_basic_tariff()
    subscription_page.apply_promo(promo_code)
    assert expected_message in (subscription_page.get_promo_massege())
