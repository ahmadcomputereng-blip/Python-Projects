import seasons
import pytest
def test_season():
    assert seasons.text_date("2024-01-10") == "One million, fifty-two thousand, six hundred forty minutes"
    assert seasons.text_date("2025-01-10") == "Five hundred twenty-five thousand, six hundred minutes"
def test_errors():
    with pytest.raises(SystemExit):
        seasons.text_date("January 1, 1999")
