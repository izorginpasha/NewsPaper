# NewsPaper
## Фаил команд DjangoShell rez.txt
## Объяснение настроек log:
### Форматеры (formatters):

console: Форматирует сообщения для вывода в консоль уровня DEBUG и выше.

console_warning: Добавляет путь к источнику для сообщений уровня WARNING и выше.

console_error: Включает путь и стэк ошибки для сообщений уровня ERROR и CRITICAL.

file_general: Форматирует сообщения для записи в файл general.log.

file_error: Форматирует сообщения для записи в файл errors.log, включая путь и стэк ошибки.

security: Форматирует сообщения для файла security.log.

mail: Форматирует сообщения для отправки по email.
### Фильтры (filters):

require_debug_true: Отправляет сообщения в консоль только при DEBUG = True.
require_debug_false: Отправляет сообщения в файл и на email только при DEBUG = False.
### Обработчики (handlers):

console_debug, console_warning, console_error: Обработчики для вывода сообщений в консоль в зависимости от уровня логирования.

file_general: Записывает сообщения уровня INFO и выше в файл general.log.

file_error: Записывает сообщения уровня ERROR и выше в файл errors.log.

file_security: Записывает сообщения безопасности в файл security.log.

mail_admins: Отправляет сообщения уровня ERROR и выше на email администраторов.
### Логгеры (loggers):

django: Основной логгер для всего проекта, использует несколько обработчиков.

django.request, django.server, django.template, django.db.backends: Логгеры для записи ошибок в файл errors.log и отправки на email.

django.security: Логгер для записи сообщений безопасности в security.log.
## Важные моменты:
В консоль выводятся сообщения только при DEBUG = True.

В файл и на email сообщения отправляются только при DEBUG = False.

Используются различные форматы для сообщений в зависимости от их уровня и источника.

Логгеры настроены таким образом, чтобы правильно фильтровать и отправлять сообщения в разные места.






