"""
Функции чтения исходного файла.
"""

from abc import ABC, abstractmethod
from typing import Type

from openpyxl.workbook import Workbook
from pydantic import BaseModel

from logger import get_logger

logger = get_logger(__name__)


class BaseReader(ABC):
    """
    Базовый класс читателя исходного файла.
    """

    def __init__(self, workbook: Workbook) -> None:
        """
        Конструктор.

        :param workbook: Рабочая книга Excel.
        """

        self.workbook = workbook

    @property
    @abstractmethod
    def model(self) -> Type[BaseModel]:
        """
        Получение модели объекта (строки).

        :return: Модель объекта (строки).
        """

    @property
    @abstractmethod
    def sheet(self) -> str:
        """
        Получение наименования листа рабочей книги.

        :return: Наименование листа рабочей книги.
        """

    @property
    @abstractmethod
    def attributes(self) -> dict:
        """
        Получение списка наименований атрибутов с информацией об индексе столбца и типе данных.

        .. code-block::

            {
                "authors": {0: str},
                "title": {1: str},
                "edition": {2: str},
                "city": {3: str},
                "publishing_house": {4: str},
                "year": {5: int},
                "pages": {6: int},
            }

        :return: Атрибуты с информацией об индексе столбца и типе данных
        """

    def read(self) -> list[BaseModel]:
        """
        Чтение исходного файла.

        :return: Список моделей строк в виде DTO (Data Transfer Objects).
        """

        models = []
        # чтение со второй строки таблицы (первая строка содержит заголовок)
        for row in self.workbook[self.sheet].iter_rows(min_row=2):
            # обработка строки идет только, если заполнены обязательные столбцы
            if not row[0].value:
                continue
            # обработка заданных в методе `attributes()` атрибутов
            attrs = {attr: row[index].value for attr, index in self.attributes.items()}

            # добавление считанной и обработанной строки в список моделей
            models.append(self.model(**attrs))

        return models
