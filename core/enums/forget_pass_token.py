from datetime import timedelta
from enum import Enum


class ForgetPassTokenEnum(Enum):
    ACTIVATE = (
        'activate',
        timedelta(minutes=10)
    )

    def __init__(self, token_type, lifetime):
        self.token_type = token_type
        self.lifetime = lifetime
