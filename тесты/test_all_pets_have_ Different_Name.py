импортировать  pytest
из  селена . вебдрайвер . поддержка  импорта  ожидаемых_условий  как  EC
из  селена . вебдрайвер . общий . по  импорту  по
из  селена . вебдрайвер . поддержка . Пользовательский интерфейс  импорта  WebDriverWait

def  test_all_pets_have_разные_имена ( go_to_my_pets ):
   '''Поверяем, что на странице со множеством питомцев, у всех питомцев разные имена'''

   element  =  WebDriverWait ( pytest . драйвер , 10 ). пока (
      ЕС . присутствия_of_element_located (( By . CSS_SELECTOR , ".table.table-hover tbody tr" )))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   pet_data  =  pytest . водитель . find_elements_by_css_selector ( '.table.table-hover tbody tr' )

   # Перебираем данные из pet_data, оставляем имя, возраст, и порождаем остальное меняем на пустую строку
   # и разделяем по пробелу.Выбираем имена и объединяем их в список pets_name.
   имя_питомца  = []
   для  i  в  диапазоне ( len ( pet_data )):
      data_pet  =  pet_data [ i ]. текст . заменить ( ' \n ' , '' ). заменить ( '×' , '' )
      split_data_pet  =  data_pet . разделить ( '' )
      имя_питомца . добавить ( split_data_pet [ 0 ])

   # Перебираем имя и если имя повторяется то прибавляем к счетчику rединицу.
   # Проверяем, если r == 0 то повторяющихся имен нет.
   г  =  0
   для  i  в  диапазоне ( len ( pets_name )):
      если  имя_питомцев . количество ( pets_name [ i ]) >  1 :
         г  +=  1
   утверждать  г  ==  0
   печать ( р )
   распечатать ( pets_name )

# python -m pytest -v --driver Chrome --driver-path /tests_drivers/chromedriver.exe tests/test_all_pets_have_ Different_name.py
