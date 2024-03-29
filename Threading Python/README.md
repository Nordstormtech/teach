# GLOBAL INTERPRETER LOCK - GIL
https://www.youtube.com/playlist?list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz

Все операции можно разделить на 2 типа CPU и I/O:
- I/O bound - операции ввода/вывода — данные операции ожидают действий от пользователя или базы
- CPU bound - логические операции (вычислительные)

Python хорошо работает с много поточностью для I/O, но плохо для CPU bound
Для CPU bound используют или multiprocessing (GIL - контролирует только потоки внутри одного процесса) или C библиотеки

Если все токи многопоточность использовать для CPU зависимостей, то между потоками будет происходить переход через 100 тиков

Для чего нужен GIL - для безопасности данных. Под каждый процесс выделяется свой массив данных и если в одном процессе один процесс удалит/изменит данные то второй поток не будет об этом знать

# Многопоточность и Многопроцесинг 

- Внутри одного процесса может быть много потоков. 

# Урок 1

- Создание потоков
- Общая информация о потоках

# Урок 2

- Потоки демоны, как они работают и где стоит применять
- Поток демон - это такой поток который завершает свою работу когда завершил работу основной поток

# Урок 3

- Отличие Lock и RLock
- Синхронизация потоков Python
- locker.acquire() - блокирование потоков ( то есть стальные потоки не получат доступ к остальному коду)
- locker.release() - разблокирование (работает только в методе Lock())
- RLock - при блокирование RLock только поток который заблокировал может разблокировать

# Урок 4

- Класс Timer в потоках - позволяет запускать потоки через какое-то время
- Хранилище Local

# Урок 5

- Семафоры - позволяет установить лимит на количество конекшенов к базе
- Барьеры - позволяет останавливать все потоки пока не наберется определенное количество потоков 
  (можно использовать при подгрузке какой-то информации)
  
# Урок 6

- Многопроцессорность
- is_alive - проверка жив ли процесс
- pid - получение id процесса
- terminate - убивает процесс
- join - ожидание завершение процесса
- ps aux | grep python - просмотр всех процессов запущенных нами

# Урок 7

- Синхронизация процессов
- Lock - урок 3
- RLock
- Array
- Queue - очередь

# Урок 8

- multiprocessing python pool
- callback - с помощью данной функции можно получить результат работы всех потоков
