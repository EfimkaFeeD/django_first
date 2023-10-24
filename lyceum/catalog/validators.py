import re

import django
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateMustContain:
    def __init__(self, *args):
        self.args = args

    def __call__(self, value):
        regex = re.findall(r"\w+[А-я]+\w+", value.lower())
        for i in self.args:
            if i in regex:
                return
        words = "или".join([f"`{i}`" for i in self.args])
        raise (
            django.core.exceptions.ValidationError(
                f"В тексте должны быть слова {words}"
            )
        )
