# Функционал кода
Данный код реализует функциональность для визуализации зависимостей пакета, находящегося в репозитории GitHub. Он извлекает данные из файла package.json, который обычно используется в проектах на Node.js для указания зависимостей и их версий. Давайте рассмотрим каждую часть кода более подробно:



## Функция fetch_dependencies(repo_url):

- Принимает URL репозитория GitHub.
- Заменяет github.com на raw.githubusercontent.com, чтобы получить доступ к файлу package.json.
- Отправляет GET-запрос на package.json и загружает данные.
- Извлекает зависимости из dependencies или devDependencies, возвращая их в виде словаря.

## Функция build_graph(dependencies, graph, parent=None):

- Принимает зависимости, граф и родительский узел.

- Для каждой зависимости создает узел и устанавливает ребро от родительского узла к зависимостям, что позволяет построить иерархию зависимостей.

## Функция visualize_graph(package_name, repo_url):

- Вызывает fetch_dependencies() для получения зависимостей.
- Создает новый граф с помощью graphviz.Digraph().
- Добавляет узел для основного пакета и строит граф зависимостей, используя build_graph().
- Рисует граф и сохраняет в формате PNG, очищая временные файлы после рендеринга.

## Главный блок программы:

- Принимает параметры из командной строки: путь к Graphviz, имя пакета и URL репозитория.
- Вызывает visualize_graph(), чтобы создать и сохранить граф зависимостей..