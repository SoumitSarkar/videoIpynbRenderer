import pytest

from videoIpynbRenderer import get_time_info

from videoIpynbRenderer import InvalidUrlException

good_URL_data = [
    # as per get_time_info which will take URL as string and return an int val
    ("https://youtu.be/SrvN3CqTo0k?t=60", 60),
    ("https://www.youtube.com/watch?v=SrvN3CqTo0k", 0),
    ("https://www.youtube.com/watch?v=SrvN3CqTo0k&t=60s", 60),
]

URL_id_bad_data = [
    ("https://www.youtube.com/watch?v=roO5VGxOw2sahesbf"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t==22s"),  # exception
    ("https://www.youtube.com/watch?v==roO5VGxOw2s&t=22s"),
]


@pytest.mark.parametrize("url, response", good_URL_data)
def test_get_time_info(url, response):
    assert get_time_info(url) == response


@pytest.mark.parametrize("URL", URL_id_bad_data)
def test_get_time_info_failed(URL):
    with pytest.raises(InvalidUrlException):
        get_time_info(URL)
