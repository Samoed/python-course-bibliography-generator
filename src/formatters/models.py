"""
Описание схем объектов (DTO).
"""
from datetime import date
from typing import Any

from pydantic import BaseModel, Field


class CiteModel(BaseModel):
    def dict(self, **kwargs: Any) -> dict[str, Any]:
        values = super().dict(**kwargs)
        for key, val in values.items():
            if isinstance(val, date):
                values[key] = val.strftime("%d.%m.%Y")
        return values


class BookModel(CiteModel):
    """
    Модель книги:

    .. code-block::

        BookModel(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            edition="3-е",
            city="СПб.",
            publishing_house="Просвещение",
            year=2020,
            pages=999,
        )
    """

    authors: str
    title: str
    edition: str | None
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class InternetResourceModel(CiteModel):
    """
    Модель интернет ресурса:

    .. code-block::

        InternetResourceModel(
            article="Наука как искусство",
            website="Ведомости",
            link="https://www.vedomosti.ru/",
            access_date=date(2021, 01, 01),
        )
    """

    article: str
    website: str
    link: str
    access_date: date


class ArticlesCollectionModel(CiteModel):
    """
    Модель сборника статей:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            collection_title="Сборник научных трудов",
            city="СПб.",
            publishing_house="АСТ",
            year=2020,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    collection_title: str
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: str


class DissertationModel(CiteModel):
    """
    Модель диссертации:

    .. code-block::

        DissertationModel(
            author="Иванов И.М.",
            title="Наука как искусство",
            author_title="д-р. / канд.",
            speciality_field="экон.",
            speciality_code="01.01.01",
            city="СПб.",
            year=2020,
            pages=999,
        )
    """

    author: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    author_title: str = Field(..., min_length=1)
    speciality_field: str = Field(..., min_length=1)
    speciality_code: str = Field(..., min_length=1, regex=r"^\d{2}\.\d{2}\.\d{2}$")
    city: str = Field(..., min_length=1)
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class AutoReportModel(DissertationModel):
    """
    Модель автореферета:

    .. code-block::

        AutoReportModel(
            author="Иванов И.М.",
            title="Наука как искусство",
            author_title="д-р. / канд.",
            speciality_field="экон.",
            speciality_code="01.01.01",
            city="СПб.",
            year=2020,
            pages=999,
        )
    """


class JournalArticleModel(CiteModel):
    """
    Модель статьи:

    .. code-block::

        ArticleClass(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            journal="Ведомости",
            year=2020,
            volume=1,
            pages="25-30",
        )
    """

    authors: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    journal: str = Field(..., min_length=1)
    year: int = Field(..., gt=0)
    volume: int = Field(..., gt=0)
    pages: str = Field(..., min_length=1)


class RegulationActModel(CiteModel):
    """
    Модель нормативного акта:

    .. code-block::

        RegulationActModel(
            act_type="Федеральный закон",
            title="Наука как искусство",
            accept_date=date(2021, 01, 01),
            act_number="123",
            official_source="Ведомости",
            publication_year=2020,
            version=1,
            article_number=2,
            edition=date(2021, 1, 1),
        )
    """

    act_type: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    accept_date: date
    act_number: str = Field(..., min_length=1)
    official_source: str = Field(..., min_length=1)
    publication_year: int = Field(..., gt=1900)
    version: int = Field(..., gt=0)
    article_number: int = Field(..., gt=1)
    edition: date
