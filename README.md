﻿Данный пакет содержит основной математический и графический аппарат для
анализа и визуализации сейсмических данных

Структура пакета:
    - GeneralCalcFunctions (содержит общие функции для расчетов)
        - CheckingName.py - модуль с функцией проверки имен файлов и каталогов
        на корректность (допустима только латиница, цифры, _ и -)
        - NormingSignal.py - модуль с функцией нормировки сигнала с учетом
        коэф-тов сенсора и регистратора
    - HydroFracCore (содержит подпакеты для обработки только данных ГРП)
        - CalcFunctions (пакет содержит сугубо математически функции)
             - MomentsSelection.py - модуль для выборки номеров отсчетов
             сигналов с двух датчиков исходя из значения корреляции сигналов, а
             также разницы времени между событиями
    - MSICore (содежит подпакеты для обработки только данных МСИ)
        - CalcFunctions (пакет содержит сугубо математически функции)
            - AverSpectrum.py   - модуль для расчета осредненнего
            (кумулятивного спектра)
            - BandPassFilter.py - модуль для проведения полосовой фильтрации
            - EnergyCalc.py     - модуль для расчета энергии спектра
            - PureSignal.py     - модуль для выделения чистого участка сигнала
            - PureSignal_experiment.py - экспериментальный модуль выделения
            чистого участка сигнала
            - Spectrogram.py    - модуль для расчета 2D-спектрограммы
            - Spectrum.py       - модуль для расчета 1D спектра сигнала
            - Wavelett.py       - модуль для проведения wavelett-трансформаций
        - DrawingFunctions (пакет служит для визуализации данных)
            - Spector.py        - модуль для построения и сохранения спектров с
            классификацией энергий (как каротаж)
            - Spectrogram.py    - модуль для построения и сохранения 2D
            спектрограммы
    - VisualFunctions (пакет с общими модулями для визуализации)
        - Colors.py -модуль для работы с цветами (перевод из RGB в HEX-формат)

# Необходимые модули
    - numpy         version 1.13.3
    - scipy         version 1.0.0
    - pywavelets    version 0.5.2
    - matplotlib    version 2.1.0

# version 0.0.0
Первая версия пакета

# version 0.0.1
Добавлен подпакет с функциями расчета данных ГРП. НО ФУНКЦИИ еще не
оттестированы!!!

# version 0.0.2
Добавлена функция проверки имени файлов и папко на допустимые символы. Функции
ГРП еще не оттестированы

# version 0.0.3
Условно оттестированы функции расчета корреляции и фильтррации значений
корреляции для ГРП. Не оттестирована функция вычисления задержек по времени

# version 0.0.4
Изменена функция генерации узлов (nodes) в модуле ГРП MomentsSelection
Создан модуль PureSignal_experiment - экспериментальный модуль выделения
чистого участка сигнала

# version 0.0.5
Убрана зависимость от пакета SeisPars. Добавлены комментарии в модули CheckingName, NormingSignal.
Создан подпакет с общими функциями для визуализации данных (GeneralPlottingFunctions)
В подпапкете для вычислений ГРП модуль разделен на две части - выборка событий по
максимальным значениям квадратов коэф-та корреляции (MomentsSelection) и геометрическая выборка пар
датчиков (PointsSelection). В подпакет ГРП добавлен подпакет для визуализации данных (гистограммы углов и
 размахов задержек)

# version 0.0.6
Изменена функция pairs_points_filtration в ГРП - добавлена опция сохранения результатов расчетов задержек в файл
Начата работа над модулем MinimizationPrep.py

# version 0.0.7
Исправлена ошибка в функции reproject_coords (ГРП) - неверно вычислялась y-координата
Изменена функция pairs_points_filtration - добавлена опция сохранения результатов расчетов задержек в файл