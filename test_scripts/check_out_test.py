from pages_methods.base_page import *
from pages_methods.check_out_page import CheckOut
import pytest


@pytest.mark.order
@pytest.mark.parametrize("country", ["de", "fr", "ru", "it", "us"])
def test_order_to_pvz(base, auth, catalog, checkout, country):
    base.change_country(country)
    base.accept_cookie()
    auth.login(auth.logpass)
    base.open(base.sku_url("180324"))
    catalog.from_card_to_cart()
    checkout.delivery_type("pvz")
    checkout.click_to_continue_button()
    checkout.change_payment_type("postpayment")
    checkout.click_to_continue_button()
    assert checkout.check_order_sucsess() == True

@pytest.mark.order       
def test_order_to_delivery(base, auth, catalog, checkout):
    base.open(base.sku_url("180324"))
    base.accept_cookie()
    auth.login(auth.logpass)
    catalog.from_card_to_cart()
    checkout.choose_delivery("address")
    checkout.choose_payment_type("Postpayment")
    checkout.confirm_order()
    assert checkout.check_order_sucsess() == True

@pytest.mark.order
@pytest.mark.parametrize("product", ["712332", "533445", "415775", "243435", "929475"])
def test_order_international(base, catalog, checkout, product):
    base.open(base.url)
    base.accept_cookie()
    base.change_country("de")
    base.open(base.sku_url(product))
    catalog.from_card_to_cart()
    checkout.filling_personal_data("first_name", "last_name", "email", "phone")
    checkout.order_international("address")
    checkout.confirm_order()
    assert checkout.check_order_sucsess() == True

@pytest.mark.order
@pytest.mark.parametrize("country", ["de", "fr", "ru", "it", "us"])
def test_order_international_auth(base, auth, catalog, checkout, country):
    base.open(base.url)
    base.accept_cookie()
    base.change_country(country)
    auth.login(auth.logpass)
    base.open(base.sku_url("1058134"))
    catalog.from_card_to_cart()
    checkout.order_international("address")
    checkout.confirm_order()
    assert checkout.check_order_sucsess() == True


