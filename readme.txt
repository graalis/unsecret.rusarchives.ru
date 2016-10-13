1) POST-запрос "Где искать: Документы/Дела, Ключевые слова: *" на адрес http://unsecret.rusarchives.ru/search
2) текст внутри <span class="badge badge-info pull-right"> - "Найдено записей - 8990", оставить только цифры
3) <div class="pagination">
	<ul id="search-pager" class="yiiPager">
		<li class="last">
			<a href="/main/SearchPager/page/1798">Последняя >> </a>
Ссылка на последнюю страницу ( = кол-во страниц)
4) блоки с информацией:

<div id="search-results-data">
	<div class="container-fluid well">
		<div class="row-fluid">
			<div class="span12">
				<p class="mb0">
					здесь в тегах <b> характеристика информации ("Заголовок документа", "Дата документа", "Фонд"), а остальной текст - сама информация. В конце span class="italic" содержит текст: Рассекречено в ... году.

Структура набора данных 

1) дело или документ
2) заголовок
3) дата создания
4) фонд
5) в каком году рассекречено

Как перейти на следующую страницу:
POST-запрос
Host: unsecret.rusarchives.ru
Url: вида http://unsecret.rusarchives.ru/main/SearchPager/page/8
Content-type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: http://unsecret.rusarchives.ru/search
Cookie: Cookie=YII_CSRF_TOKEN=310692c4c70b0583d80012474c2f0534ee24d9de; PHPSESSID=p8dik196ivv8s82q174k167pj1; _ym_uid=14750723111001704560; _ym_isad=1; _ym_visorc_23456458=w 

Cookie=YII_CSRF_TOKEN=310692c4c70b0583d80012474c2f0534ee24d9de; PHPSESSID=p8dik196ivv8s82q174k167pj1; _ym_uid=14750723111001704560; _ym_isad=1; _ym_visorc_23456458=w