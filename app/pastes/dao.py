from app.dao.base import BaseDAO
from app.pastes.models import Pastes


class PastesDAO(BaseDAO):
    model = Pastes

    # @classmethod
    # async def add(cls):
