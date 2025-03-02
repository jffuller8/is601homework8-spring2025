"""Pytest plugin configuration"""
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--num_records",
        action="store",
        type=int,
        default=1,
        help="number of records to generate"
    )

@pytest.fixture
def num_records(pytestconfig):
    return pytestconfig.getoption("num_records")