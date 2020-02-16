import unittest


def extract_domain_from_www(url: str) -> str:
    return url.split('.')[1]


def extract_domain_from_http(url: str) -> str:
    return url.split(r'//')[1].split('.')[0]


def domain_name(url: str):
    if r'www' in url:
        return extract_domain_from_www(url)
    if r'http' in url:
        return extract_domain_from_http(url)
    return url.split(r'.')[0]


def domain_name_v2(url: str):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


class TestDomainNameExtractor(unittest.TestCase):

    def test_it_should_extract_the_domain_name(self):
        self.assertEqual("google", domain_name("http://google.com"))
        self.assertEqual("google", domain_name("http://google.co.jp"))
        self.assertEqual("xakep", domain_name("www.xakep.ru"))
        self.assertEqual("youtube", domain_name("https://youtube.com"))
