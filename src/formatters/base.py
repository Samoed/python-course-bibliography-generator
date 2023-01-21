"""
Базовые функции форматирования списка источников
"""
from typing import Type

from formatters.models import CiteModel
from formatters.styles.base import BaseCitationStyle
from logger import get_logger

logger = get_logger(__name__)


class BaseCitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map: dict[Type[CiteModel], Type[BaseCitationStyle]]

    def __init__(self, models: list[CiteModel]) -> None:
        """
        Конструктор.

        :param models: Список объектов для итогового форматирования
        """

        formatted_items = []
        for model in models:
            formatted_items.append(self.formatters_map[type(model)](model))

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.

        :return:
        """

        logger.info("Общее форматирование ...")

        return sorted(self.formatted_items, key=lambda item: item.formatted)
