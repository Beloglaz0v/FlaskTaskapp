<h3>Оглавление</h3>

1.[Регистрация](#Регистрация)

2.[Авторизация](#Авторизация)

3.[Список задач](#Список_задач)

4.[Добавление задачи](#Добавление_задачи)

5.[Изменение задачи](#Изменение_задачи)

6.[Удаление задачи](#Удаление_задачи)


<h2>Работа с API</h2>
Процесс работы с API возможен при наличии персонального ключа (токена), которым в дальнейшем должен быть подписан каждый запрос к API.

Код ключа (токен) передается в заголовке любого запроса (в "headers") кроме случаев получения самого токена, когда этот код не требуется.

Процесс получения персонального ключа описан в разделах: [Регистрация](#Регистрация) и [Авторизация](#Авторизация)

__Пример передаваемого заголовка__

headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOVuIn0.n9j8mxoOTM1cJNysy3_6cA_yCQA8tH_Pryc9YbQZsb8'}



<a name="Регистрация"></a> 
<h1>Регистриация</h1>

Для регистрации нового пользователя отправляется POST запрос по ссылке:

.../register

<h3>Параметры запроса</h3>

| Параметр | Описание |
|----:|:----|
| login | Логин нового пользователя  |
| password | Пароль нового пользователя |

<h3>Ответ</h3>

В качестве ответа будет получен access_token

__Пример ответа__

{'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOVuIn0.n9j8mxoOTM1cJNysy3_6cA_yCQA8tH_Pryc9YbQZsb8'}

__Возможные ошибки:__

...

<a name="Авторизация"></a> 
<h1>Авторизация</h1>

Для авторизации пользователя отправляется POST запрос по ссылке:

.../login

<h3>Параметры запроса</h3>

| Параметр | Описание |
|----:|:----|
| login | Логин пользователя  |
| password | Пароль пользователя |

<h3>Ответ</h3>

В качестве ответа будет получен access_token

__Пример ответа__

{'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOVuIn0.n9j8mxoOTM1cJNysy3_6cA_yCQA8tH_Pryc9YbQZsb8'}

__Возможные ошибки:__

...


<a name="Список_задач"></a> 
<h1>Список задач</h1>

Для получения списка задач пользователя, отправляется GET запрос c токеном пользователя в заголовке запроса (в "headers") по ссылке:

.../tasks

<h3>Параметры ответа</h3>

| Параметр | Описание |
|:----|:----|
| id | ID задачи  |
| title | Название задачи |
| description | Описание задачи |
| date | Дата создания |
| status | Статус задачи |
| deadline | Планируемая дата завершения |

В качестве ответа будет получен список задач

__Пример ответа__

[

{

    'id': 1, 

    'title': 'Сходить в магазин',

    'description': 'Сахар и молоко', 

    'date': '07.10.2020 13:39:38',

    'deadline': None, 

    'status': 'Новая', 

}

]

__Возможные ошибки:__

...


<a name="Добавление_задачи"></a> 
<h1>Добавление задачи</h1>

Для добавления задачи пользователю, отправляется POST запрос c токеном пользователя в заголовке запроса (в "headers") по ссылке:

.../new_task

<h3>Параметры запроса</h3>

| Параметр |Может быть пустым| Описание |
|:----|:----:|:----|
| title | - | Название задачи |
| description | + | Описание задачи |
| status |-| Статус задачи |
| deadline |+| Планируемая дата завершения |

В качестве ответа будет получен словарь с данными добавленной задачи.

<h3>Параметры ответа</h3>

| Параметр | Описание |
|:----|:----|
| id | ID задачи  |
| title | Название задачи |
| description | Описание задачи |
| date | Дата создания |
| status | Статус задачи |
| deadline | Планируемая дата завершения |


__Пример ответа__

{

    'id': 1, 

    'title': 'Сходить в магазин',

    'description': 'Сахар и молоко', 

    'date': '07.10.2020 13:39:38',

    'deadline': None, 

    'status': 'Новая', 
}


__Возможные ошибки:__

...



<a name="Изменение_задачи"></a> 
<h1>Изменение задачи</h1>

Для изменения задачи пользователя, отправляется PUT запрос c токеном пользователя в заголовке запроса (в "headers") по ссылке:

.../update_task/\<id\>

<h3>Параметры запроса</h3>

| Параметр | Описание |
|:----|:----|
| title | Название задачи |
| description | Описание задачи |
| status |Статус задачи |
| deadline |Планируемая дата завершения |

В качестве ответа будет получен словарь с измененными данными.

<h3>Параметры ответа</h3>

| Параметр | Описание |
|:----|:----|
| id | ID задачи  |
| title | Название задачи |
| description | Описание задачи |
| date | Дата создания |
| status | Статус задачи |
| deadline | Планируемая дата завершения |


__Пример ответа__

{

    'id': 1, 

    'title': 'Сходить в магазин',

    'description': 'Сахар и молоко', 

    'date': '07.10.2020 13:39:38',

    'deadline': None, 

    'status': 'Новая', 
}


__Возможные ошибки:__

...


<a name="Удаление_задачи"></a> 
<h1>Удаление задачи</h1>

Для удаления задачи пользователя, отправляется DELETE запрос c токеном пользователя в заголовке запроса (в "headers") по ссылке:

.../delete_task/\<id\>


__Возможные ошибки:__

...
