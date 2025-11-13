import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "login: Tests related to user login functionality"
    )
    config.addinivalue_line(
        "markers", "hospital_login: Tests related to hospital login functionality"
    )
    config.addinivalue_line(
        "markers", "patient_registration: Tests related to patient registration"
    )
    config.addinivalue_line(
        "markers", "hospital_management: Tests related to hospital management"
    )