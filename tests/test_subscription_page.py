from playwright.sync_api import expect
from page.subscription_page import SubscriptionPage


def test_subscription_page_open(page) -> None:
    page.set_viewport_size({"width": 1366, "height": 768})
    subscription_page = SubscriptionPage(page)

    subscription_page.open()

    expect(page).to_have_url("/automation-lab/subscription")

    expect(subscription_page.basic_tariff).to_be_visible()
    expect(subscription_page.premium_tariff).to_be_visible()
    expect(subscription_page.familly_tariff).to_be_visible()

    expect(subscription_page.promo_input).to_be_visible
    expect(subscription_page.card_number).to_be_visible
    expect(subscription_page.card_expiry).to_be_visible
    expect(subscription_page.card_cvv).to_be_visible

    expect(subscription_page.submit_btn).to_be_visible
