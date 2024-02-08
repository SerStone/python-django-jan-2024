from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProfileDataClass:
    id: int
    first_name: str
    last_name: str
    age: int
    gender: str
    created_at: datetime
    updated_at: datetime


@dataclass
class UserDataClass:
    id: int
    email: str
    password: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    last_login: datetime
    created_at: datetime
    updated_at: datetime
    profile: ProfileDataClass
