импортировать  pytest
из  настроек  импортировать  valid_email , valid_password

защита  test_show_pet_friends ():
   '''Проверка карточек питомцев'''

   # Устанавливаем неявное ожидание
   тест . водитель . неявно_ожидание ( 10 )

   # Вводим электронную почту
   тест . водитель . find_element_by_id ( 'электронная почта' ). send_keys ( действительный_адрес электронной почты )

   # Вводим пароль
   тест . водитель . find_element_by_id ( "пропустить" ). send_keys ( действительный_пароль )

   # Нажимаем на вход в аккаунт
   тест . водитель . find_element_by_css_selector ( 'кнопка[type="submit"]' ). нажмите ()

   # Проверяем, что мы произошло на главной странице пользователя
   утверждать  pytest . водитель . current_url  ==  'http://petfriends1.herokuapp.com/all_pets'

   изображения  =  pytest . водитель . find_elements_by_css_selector ( '.card-deck.card-img-top' )
   имена  =  pytest . водитель . find_elements_by_css_selector ( '.card-deck .card-title' )
   описания  =  pytest . водитель . find_elements_by_css_selector ( '.card-deck.card-text' )

   утверждать  имена [ 0 ]. текст  !=  ''

   для  i  в  диапазоне ( len ( имена )):
      утверждать  изображения [ i ]. get_attribute ( 'источник' ) !=  ''
      утверждать  имена [ i ]. текст  !=  ''
      утверждают  описания [ i ]. текст  !=  ''
      утверждать  ','  в  описаниях [ i ]. текст
      части  =  описания [ i ]. текст . разделить ( "," )
      утверждать  len ( части [ 0 ]) >  0
      утверждать  len ( части [ 1 ]) >  0

# python -m pytest -v --driver Chrome --driver-path /tests_drivers/chromedriver.exe тесты/test_show_pet_friends.py
