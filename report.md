
# Table of Contents

1.  [Что было сделано](#orgb60dd50)
    1.  [Стиль ГОСТ](#org5e6263c)
    2.  [Стиль APA](#org393a9a3)



<a id="orgb60dd50"></a>

# Что было сделано

-   Оформлено цитирование ГОСТ для нормативного акта, диссертации, автореферата, статьи из журнала
-   Оформлено цитирование APA для книги, интернет-ресурса, сборника статей, нормативного акта, диссертации, автореферата, статьи из журнала
-   Добавлены тесты
-   Обновлена документация
```
    docker compose run --workdir / app /bin/bash -c "black src docs/source/*.py; isort src/*.py docs/source/*.py"
    docker compose run --workdir / app /bin/bash -c "pylint src; flake8 src; mypy src; black --check src"
    
    ------------------------------------
    Your code has been rated at 10.00/10
    
    Success: no issues found in 23 source files
    docker compose run app pytest --cov=/src --cov-report html:htmlcov --cov-report term --cov-config=/src/tests/.coveragerc -vv
    ============================= test session starts ==============================
    platform linux -- Python 3.10.8, pytest-7.1.3, pluggy-1.0.0 -- /usr/local/bin/python
    cachedir: .pytest_cache
    rootdir: /src
    plugins: cov-3.0.0
    collecting ... collected 29 items
    
    tests/test_main.py::test_get_formatted[gost-GOSTRenderer-GOSTCitationFormatter] PASSED [  3%]
    tests/test_main.py::test_get_formatted[apa-APARenderer-APACitationFormatter] PASSED [  6%]
    tests/test_main.py::test_get_formatted[abacaba-GOSTRenderer-GOSTCitationFormatter] PASSED [ 10%]
    tests/test_renderer.py::TestRenderer::test_gost_render PASSED            [ 13%]
    tests/test_renderer.py::TestRenderer::test_apa_render PASSED             [ 17%]
    tests/formatters/test_apa.py::TestAPA::test_book PASSED                  [ 20%]
    tests/formatters/test_apa.py::TestAPA::test_internet_resource PASSED     [ 24%]
    tests/formatters/test_apa.py::TestAPA::test_articles_collection PASSED   [ 27%]
    tests/formatters/test_apa.py::TestAPA::test_citation_formatter PASSED    [ 31%]
    tests/formatters/test_apa.py::TestAPA::test_dissertation PASSED          [ 34%]
    tests/formatters/test_apa.py::TestAPA::test_auto_report PASSED           [ 37%]
    tests/formatters/test_apa.py::TestAPA::test_journal_article PASSED       [ 41%]
    tests/formatters/test_apa.py::TestAPA::test_regulation_act PASSED        [ 44%]
    tests/formatters/test_gost.py::TestGOST::test_book PASSED                [ 48%]
    tests/formatters/test_gost.py::TestGOST::test_internet_resource PASSED   [ 51%]
    tests/formatters/test_gost.py::TestGOST::test_articles_collection PASSED [ 55%]
    tests/formatters/test_gost.py::TestGOST::test_citation_formatter PASSED  [ 58%]
    tests/formatters/test_gost.py::TestGOST::test_dissertation PASSED        [ 62%]
    tests/formatters/test_gost.py::TestGOST::test_auto_report PASSED         [ 65%]
    tests/formatters/test_gost.py::TestGOST::test_journal_article PASSED     [ 68%]
    tests/formatters/test_gost.py::TestGOST::test_regulation_act PASSED      [ 72%]
    tests/readers/test_readers.py::TestReaders::test_book PASSED             [ 75%]
    tests/readers/test_readers.py::TestReaders::test_internet_resource PASSED [ 79%]
    tests/readers/test_readers.py::TestReaders::test_articles_collection PASSED [ 82%]
    tests/readers/test_readers.py::TestReaders::test_sources_reader PASSED   [ 86%]
    tests/readers/test_readers.py::TestReaders::test_dissertation_reader PASSED [ 89%]
    tests/readers/test_readers.py::TestReaders::test_auto_report_reader PASSED [ 93%]
    tests/readers/test_readers.py::TestReaders::test_journal_article PASSED  [ 96%]
    tests/readers/test_readers.py::TestReaders::test_regulation_act_reader PASSED [100%]
    
    ---------- coverage: platform linux, python 3.10.8-final-0 -----------
    Name                            Stmts   Miss Branch BrPart  Cover
    -----------------------------------------------------------------
    formatters/__init__.py              0      0      0      0   100%
    formatters/base.py                 14      0      4      0   100%
    formatters/models.py               58      0      4      0   100%
    formatters/styles/__init__.py       0      0      0      0   100%
    formatters/styles/apa.py           68      0      0      0   100%
    formatters/styles/base.py          14      1      0      0    93%
    formatters/styles/gost.py          68      0      0      0   100%
    logger.py                          12      0      0      0   100%
    main.py                            35      7      8      0    79%
    readers/__init__.py                 0      0      0      0   100%
    readers/base.py                    25      0      6      0   100%
    readers/reader.py                  84      0      2      0   100%
    renderer.py                        37      0      2      0   100%
    settings.py                         7      0      0      0   100%
    tests/__init__.py                   2      0      0      0   100%
    tests/conftest.py                  24      0      0      0   100%
    tests/formatters/__init__.py        0      0      0      0   100%
    tests/formatters/test_apa.py       30      0      2      0   100%
    tests/formatters/test_gost.py      30      0      2      0   100%
    tests/readers/__init__.py           0      0      0      0   100%
    tests/readers/test_readers.py     113      0      2      0   100%
    tests/test_main.py                 11      0      0      0   100%
    tests/test_renderer.py             17      0      0      0   100%
    -----------------------------------------------------------------
    TOTAL                             649      8     32      0    99%
    Coverage HTML written to dir htmlcov
    
    
    ============================== 29 passed in 0.73s ==============================
```

<a id="org5e6263c"></a>

## Стиль ГОСТ

![img](docs/gost.png)


<a id="org393a9a3"></a>

## Стиль APA

![img](docs/apa.png)

