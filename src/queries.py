import requests
import urls


class Queries:
    @classmethod
    def get_annotations(cls, pdbid):
        responses = []
        for url in urls.ALL_URLS:
            responses.append(requests.get(url + pdbid).json())
        return responses
