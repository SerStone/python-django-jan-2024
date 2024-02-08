import os
from uuid import uuid1

from core.dataclasses.car_dataclass import CarDataclass


def upload_photo(instance: CarDataclass, filename: str):
    ext = filename.split('.')[-1]
    return os.path.join(instance.brand, 'avatars', f'{uuid1()}.{ext}')
