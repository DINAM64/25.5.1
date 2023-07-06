импортировать  pytest
из  настроек  импортировать  valid_email , valid_password
из  селена . вебдрайвер . поддержка . Пользовательский интерфейс  импорта  WebDriverWait
из  селена . вебдрайвер . поддержка  импорта  ожидаемых_условий  как  EC
из  селена . вебдрайвер . общий . по  импорту  по

защита  test_show_my_pets ():
   '''Проверяем, что мы произошли на странице "Мои питомцы"'''

   # Устанавливаем явное ожидание
   element  =  WebDriverWait ( pytest . драйвер , 10 ). пока ( EC . присутствие_элемента_расположено (( По . ID , "email" )))
   # Вводим электронную почту
   тест . водитель . find_element_by_id ( 'электронная почта' ). send_keys ( действительный_адрес электронной почты )

   element  =  WebDriverWait ( pytest . драйвер , 10 ). пока ( EC . наличие_элемента_находится (( По . ID , "пройти" )))
   # Вводим пароль
   тест . водитель . find_element_by_id ( "пропустить" ). send_keys ( действительный_пароль )

   element  =  WebDriverWait ( pytest . драйвер , 10 ). пока ( EC . присутствия_элемента_расположенного (( By . CSS_SELECTOR , "button[type='submit']" )))
   # Нажимаем на вход в аккаунт
   тест . водитель . find_element_by_css_selector ( 'кнопка[type="submit"]' ). нажмите ()

   element  =  WebDriverWait ( pytest . драйвер , 10 ). пока ( ЕС . наличие_элемента_расположено (( По . LINK_TEXT , "Мои питомцы" )))
   # Нажимаем на посилання "Мои питомцы"
   тест . водитель . find_element_by_link_text ( "Мои питомцы" ). нажмите ()


   # Проверяем, что мы обнаружили на странице "Мои питомцы"
   утверждать  pytest . водитель . current_url  ==  'http://petfriends1.herokuapp.com/my_pets'

# python -m pytest -v --driver Chrome --driver-path /tests_drivers/chromedriver.exe tests/test_show_my_pets.py
