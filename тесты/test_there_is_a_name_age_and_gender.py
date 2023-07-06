импортировать  pytest
из  селена . вебдрайвер . поддержка . Пользовательский интерфейс  импорта  WebDriverWait
из  селена . вебдрайвер . поддержка  импорта  ожидаемых_условий  как  EC
из  селена . вебдрайвер . общий . по  импорту  по

def  test_there_is_a_name_age_and_gender ( go_to_my_pets ):
   '''Поверяем, что на странице со множеством питомцев, у всех питомцев есть имя, возраст и порода'''

   element  =  WebDriverWait ( pytest . драйвер , 10 ). пока ( EC . присутствия_элемента_расположенного (( By . CSS_SELECTOR , ".table.table-hover tbody tr" )))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   pet_data  =  pytest . водитель . find_elements_by_css_selector ( '.table.table-hover tbody tr' )

   # Перебираем данные из pet_data, оставляем имя, возраст, и порождаем остальное меняем на пустую строку
   # и разделяем через пробел. Находим количество элементов в полученном списке и сравниваем их
   # с готовым
   для  i  в  диапазоне ( len ( pet_data )):
      data_pet  =  pet_data [ i ]. текст . заменить ( ' \n ' , '' ). заменить ( '×' , '' )
      split_data_pet  =  data_pet . разделить ( '' )
      результат  =  длина ( split_data_pet )
      утверждать  результат  ==  3

# python -m pytest -v --driver Chrome --driver-path /tests_drivers/chromedriver.exe testings/test_there_is_a_name_age_and_gender.py
