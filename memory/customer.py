_FAKE_CUSTOMER = {
    "123": {
        "tier": "gold",
        "language": "en",
        "refund_eligible": True,
    }
}

def load_customer_profile(customer_id: str):
    return _FAKE_CUSTOMER.get(customer_id, {})