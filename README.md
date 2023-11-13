## Программа для создания изображения пути муравья на плоскости и для подсчета количества черных клеток на этом изображении.

### Задача
- На белом поле размером 1024x1024 клеток, в позиции 512,512 находится “муравей”
- Муравей двигается по следующим правилам:
  - На белой клетке - поворачивает на 90° по часовой стрелке, инвертирует пиксель и пермещается вперед на одну клетку
  - На черной клетке - поворачиват на 90° против часовой стрелки, инвертирует пиксель и перемещается вперед на одну клетку
- Изачально муравей находится на белой клетке и смотрит вверх.
- Создайте изображение пути муравья до границы поля в виде BMP или PNG файла глубиной цвета 1 бит и укажите число черных клеток на нем.
- Программа должна минимизировать использование RAM

### Установка
Требуется Python 3.10+
Создайте виртуальное окружение командой:
```
python -m venv venv
```
Установите зависимости выполнив команду:
```
pip install -r requirements.txt
```
Запустите файл main.py (конфигурация указывается в функции def main)