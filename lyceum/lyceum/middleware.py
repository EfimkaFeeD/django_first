import re

from django.conf import settings

request_number = 0


class SimpleLyceumMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        global request_number
        request_number += 1
        response = self.get_response(request)
        if settings.ALLOW_REVERSE and request_number % 10 == 0:
            have_body = False
            russian = re.compile("^[?!,.а-яА-ЯёЁ0-9\\s]+$")
            content = response.content.decode()
            if russian.match(content):
                if "<body>" in content:
                    have_body = True
                    content = content.replace("<body>", "")
                    content = content.replace("</body>", "")
                tmp_content = content.split(" ")
                reversed_content = []
                for i in tmp_content:
                    reversed_content.append(i[::-1])
                new_content = " ".join(reversed_content)
                if have_body:
                    new_content = f"<body> {new_content} </body>"
                response.content = new_content.encode()
                return response
            return response
        return response
