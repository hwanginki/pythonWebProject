# 파이썬/장고 웹서비스 (with 리액트)
- 파이썬/장고 웹서비스 개발 프로젝트 (with 리액트) - 인프런
- https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EC%9B%B9%EC%84%9C%EB%B9%84%EC%8A%A4/dashboard

# 12월 17일 웹서비스(인프라) 기반 파이썬 프로젝트 시작합니다! 같이 배웁니다! 👨‍🔧
- 황인기님께서 작성

# 🌎 자바스크립트 현황 경향 (구글트랜드)[https://trends.google.com/trends/explore?date=today%205-y&q=%2Fm%2F012l1vxv,%2Fg%2F11c0vmgx5d,%2Fg%2F11c6w0ddw9,%2Fm%2F0n50hxv,%2Fm%2F02p97]

![구글트랜드](https://user-images.githubusercontent.com/60806047/146487545-504c665c-d3e9-4fff-ba4f-4272a2c0236c.png)

# ☝ 개발 관련 필요한 기술
- 웹 서비스 및 API : Python django
- 웹 프론트엔드 : React.js jQuery
- 인프라 : PaaS(Platform as a Service) 또는 Serverless 플랫폼
- Python 3.8.x 🔺
- Visual Studio Code 툴

# ✌ 다양한 개발 파트가 있다?!
1. 웹 프론트엔드 개발 : 웹 브라우저에서 구동되느 애플리케이션은 개발. HTML/CSS/JavaScript를 기반으로 다수의 언어/라이브러리 ex) React.js, Vue.js, jQuery, Bootstrap 등 있습니다!!
2. 스마트폰 애플리케이션 개발 : Android/iOS 스마트폰/태블렛에서 구동되는 애플리케이션을 Java/Swift/Objective-c 언어로 개발하고요. 앱에 웹브라우저를 임베딩하여 웹 프론트엔드 기술로 앱을 개발하기도 합니다!!
3. 인프라 관리 : 자체 서버, 서버/웹 호스팅, AWS/Azure/Google/Heroku 클라우드 (laaS와 PaaS) 등 백엔드 개발 -> Django, Flask, Spring(JAVA), Ruby on Rails(Ruby) 등등!!

# 🎁 웹프레임워크가 왜? 필요한가요
- 우선 웹서비스가 왜 필요하는 이유는! 서버의 역할입니다. 모든 서비스의 근간!!! 어떤 서비스이든 웹서비스는 당연히~ 잘 해야하는 분야이기도 하고요. 덜 회자된다고 해서 지나간 유행이 아니다. 서버없이 머신러닝만 한다고 해서 서비스가 되겠는가요? 앱만 한다고 해서 서비스가 되겠는가요?! 카카오톡/트위터도 처음에는 Ruby on Rails로 웹베이스에서 API를 제공했었습니다!
- 만들 수 있는 것은? 웹서비스, 앱 서버, 챗봇 서비스 등등
- 웹서비스를 만들 때마다 반복되는 것들을 표준화해서 묶어놓습니다! 거의 모든 언어마다 웹프레임워크가 존재함!

# 🎨 다양한 파이썬 웹프레임워크
Django : The Web framework for perfectionists with deadlines.
백엔드 개발에 필요한 거의 모든 기능을 제공. 중복된 작업을 최대한 줄여주는 최고의 웹 프레임워크.
Flask : a micro framework for Python based on Werkzeug.
백엔드 개발에 필요한 일부분의 기능을 제공
ORM으로서 SQLAlchemy를 주로 사용
Sanic : Async Python 3.5+ web server/framework
Tornado : asynchronous networking library
등등 프레임워크 많습니다!    
👉 https://wiki.python.org/moin/WebFrameworks

# 🎗 Django(장고)의 강점은?!
1. Python 생태계
* 여러분의 크롤링, 자동화, 머신러닝 코드와 같은 언어 사용!
* 표현력이 좋고, 가독성 높은 코드!
2. 건강한 커뮤니티
3. 풀스택 웹프레임워크
* 백엔드 개발에 필요한 거의 모든 것을 Django에서 직접 지원함!
  * AIP 개발에 필요한 거의 모든 것을 django-rest-framework에서 지원합니다!
* 참고) 프론트엔드 개발에서의 요즘 트렌드는 React, Vue, Angular입니다!!
4. 10년이상의 동안 충분히 성숙
* 2008년에 1.0버전 공개했으며, 2019년 12월에선 3.0버전 공개를 했습니다!

# ⚽ Django 붙여진 이유가 있다?!
- 기타리스트 Django Reinhardt의 이름을 딴 작명입니다.
- Lawrence Journal-World 신문사에서 2003년부터 개발 시작했었고, 2005년에 세상에 널리 공개했습니다!
- 2008년에는 1.0 릴리즈 시작
- Django 3.x부터 비동기 지원

# 🎹 장고는 MTV 프레임워크
- 이름만 다를 뿐, MVC입니다.
* Model -> 장고의 Model
  * 데이터베이스 SQL 쿼리를 생성 또는 수행해요!!
* View -> 장고의 Template
  * 복잡한 문자열 조합을 도와줘요!!
* Controller -> 장고의 View
  * HTTP 클라이언트로부터의 요청을 처리하는 함수입니다!!

# ❤ 백엔드는 서비스의 중심입니다
- 보기 좋은 떡이 먹기에도 좋다고, 프론트에 대한 열망은 숨길 수 없습니다! 하지만, 일에도 순서가 있습니다. 백엔드는 서비스의 중심입니다.
- 백엔드 / 서비스운영을 먼저~~~ 탄탄하게 하시고 나서, 그 후엔 프론트/앱을 고민하시는 것이 순서에 맞아요!!!

# 🧡 Ask Company의 선택
- 웹 서비스 및 API : 파이썬, 장고
- 웹 프론트엔드 : React, jQuery
- 인프라 : PaaS(Platform as a Service) 혹은 Serverless 플랫폼

# ‼ 걱정하지마세요. 이제 위의 다운로드 하는 방법을 알려주시죠!
- [파이썬 설치](#파이썬-설치)
- [Visual Studio Code(툴, IDE) 설치](#Visual-Studio-Code-설치)
- [장고 설치](#장고-설치)

# 🥨 장고 프로젝트 생성하기!
(바탕화면에 생성하고 싶으면 먼저 cd Desktop 명령어 치고 진행해주세요)

- 윈도우키 누르고 cmd 입력하고나서 django-admin startproject askcompany(프로젝트명)하고 그 폴더가 보이면 생성되었음을 볼 수 있습니다.

![명령프롬프트에서 장고 프로젝트 생성](https://user-images.githubusercontent.com/60806047/146672582-993f3ddd-28b4-441b-a686-62bb30e94cf0.JPG)

![장고 프로젝트 폴터 생성](https://user-images.githubusercontent.com/60806047/146672552-0a27597b-69e3-4321-9607-c2cb3bf960f9.JPG)

# 💆‍♀️ 기본 생성된 파일/디렉토리 목록 생성
- cd askcompany
- python manage.py migrate
- python manage.py createsuperuser
  - 새로운 계정 생성하기 위해 ID, PASSWORD 입력주세요!
- python manage.py runserver

![sdfsdf](https://user-images.githubusercontent.com/60806047/146673057-bca83a31-c124-433d-8f67-117cd7fbeb1e.jpg)

http://127.0.0.1:8000/ <- 복사한 후, 크롬 브라우져에서 주소창에 넣고 실행해보세요.

![장고 서버](https://user-images.githubusercontent.com/60806047/146673194-d7ed799d-fd60-4273-b1eb-0119cae9c4da.JPG)

위의 사진처럼 잘뜨면 서버가 작동될 수 있음을 볼 수 있습니다!!

![장고 서버_2](https://user-images.githubusercontent.com/60806047/146673195-47c7b00e-de4b-4f39-b489-22315d0f29eb.JPG)

위의 사진처럼 주소창에 ../admin 입력하시고 자신이 만들었던 계정의 아이디, 비밀번호를 입력하시고

![장고 서버_3](https://user-images.githubusercontent.com/60806047/146673197-722afc53-352b-41c9-ace7-b51c15328c79.JPG)

위의 사진처럼 성공적으로 잘 된겁니다!

# 😳 비주얼 스튜디오 코드에서 파이썬 설치하기 및 편집기 명령 설정

- 파이썬 설치하기

![비주얼스튜디오에서 파이썬 설치하기](https://user-images.githubusercontent.com/60806047/146673369-ce9388d9-c2f3-49c8-b45a-b707fd43aaf3.jpg)

![비주얼스튜디오에서 파이썬 설치하기_2](https://user-images.githubusercontent.com/60806047/146673371-ea28c153-09ec-4118-9409-64e5ec9f1cad.JPG)

![비주얼스튜디오에서 파이썬 설치하기_3](https://user-images.githubusercontent.com/60806047/146673373-b30d105d-950c-4955-b82e-b8b11ae780da.JPG)

- 파이썬에서 편집기 명령 설정

![비주얼스튜디오에서 파이썬 설치하기_4](https://user-images.githubusercontent.com/60806047/146674314-bb0540f6-582e-435d-968d-0edcb50eec46.JPG)

![비주얼스튜디오에서 파이썬 설치하기_5](https://user-images.githubusercontent.com/60806047/146674317-3ba2774f-3b5a-4763-b961-d6b45e9c1fab.JPG)

![비주얼스튜디오에서 파이썬 설치하기_7](https://user-images.githubusercontent.com/60806047/146674724-fccdf288-ccc2-479f-8521-495be5e28145.JPG)

![비주얼스튜디오에서 파이썬 설치하기_8](https://user-images.githubusercontent.com/60806047/146674726-eb8d87fa-4101-42aa-b805-2b707c9ba4ea.JPG)

![비주얼스튜디오에서 파이썬 설치하기_9](https://user-images.githubusercontent.com/60806047/146674727-e096e234-c9d1-4ea2-9387-d5009ba468da.JPG)

![비주얼스튜디오에서 파이썬 설치하기_6](https://user-images.githubusercontent.com/60806047/146674729-02bb2852-1d06-4eed-8f11-0f5ec26d474a.jpg)

# 장고 주요 기능들_☝
- Functin based Views : 함수로 HTTP 요청 처리합니다!
- Models : 데이터베이스와의 인터페이스!
- Templates : 복잡한 문자열 조합을 보다 용이하게, 주로 HTML 문자열 조합 목적으로 사용하지만, 푸쉬 메세지나 이메일 만들 때에도 쓰면 편리하다는 점!
- Admin 기초 : 심플한 데이터베이스 레코드 관리하는 UI!
- Logging : 다양한 경로로 메시지 로깅!
- Static files : 개발 목적으로의 정적인 파일 관리!
- Messages framework : 유저에게 1회성 메세지 노출 목적!

# 장고 주요 기능들_✌
- Class Based Views : 클래스로 함수 기반 뷰 만들기
- Forms : 입력폼 생성, 입력값 유효성 검사 및 DB로의 저장
  - Validators & Fields & Widgets
- 테스팅
- 국제화 & 지역화
- 캐싱
- Geographic : DB의 Geo 기능 활용(PostareSQL 중심)
- Sending Emails
- Syndication Feeds(RSS/Atom)
- Sitemaps

# 🍒 장고 기본 앱
- admin
- admindocs
- auth
- contenttypes
- flatpages
- gis
- humanize
- messages
- postares
- redirects
- sessions
- sitemaps
- sites
- staticfiles
- sydication

# 😁 웹 애플리케이션 기본 구조는?!
- 웹브라우저 <-> 다양한 언어/프레임워크로 만드는 웹 서버(Django) <-> 1. 데이터베이스 서버(SQLite, MySQL, PostgreSQL 등) 2. 캐시 서버(Memcached, Redis)

# 💕 장고 기본 구조
- 웹브라우저
- URLConf : 미리 URL 별로 호출할 함수를 리스트에 등록한다.
- 뷰(View) : URL에 맞춰 호출된 함수
- 모델 : 파이썬 코드로 데이터베이스와 통신
- 햄플릿 엔진 : 복잡한 문자열을 손쉽게 조합하기 위한 문자열 렌더링 엔진
- 데이버베이스 서버 : SQLite, MySQL, PostgreSQL 등..
- 캐시서버 : Memcached, Redis

# 장고 모델(ORM_객체 관계 매핑_Object-relational mapping: 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법임!)
- 애플리케이션의 다양한 데이터 저장방법은?
 - 데이터베이스 : RDBMS, NoSQL 등
 - 파일 : 로컬, 외부 정적 스토리지
 - 캐시서버 : memcached, redis 등

# 데이터베이스와 SQL
- 데이터베이스의 종류
 - RDBMS(관계형 데이터베이스 관리 시스템)
  - 대표적으로 PostgreSQL, MySQL, SQLite, MS-SQL, Oracle 등..
 - NoSQL : MongoDB, Cassandra, CouchDB, Google BigTable 등..

- 데이터베이스에 쿼리하기 위한 언어 -> SQL !
 - 같은 작업을 하더라도, 보다 적은 수의 SQL, 보다 높은 성능의 SQL
 - 직접 SQL을 만들어내기도 하지만, ORM을 통해 SQL을 생성/실행하기도 합니다. = Not Magic.
 - 중요! ORM을 쓰더라도, 내가 작성된 ORM코드를 통해 어떤 SQL이 실행되기 있는지, 파악을 하고 이를 최적화할 수 있어야 합니다. -> Django-debug-toolbar 적극 활용

# 장고 ORM인 모델은 RDB만을 지원합니다
- 장고 3.0.2 기준으로 제공되는 backends
- https://github.com/django/django/tree/3.0.2/django/db/backends

# 다양한 파이썬 ORM(https://github.com/django/django/tree/3.0.2/django/db/backends)
- Relational Databases : Django Models, SQLAlchemy, Orator, Peewee, PonyORM 등
- NoSQL Databases : django-mongodb-engine, hot-redis, MongoEngine, PynamoDB 등

# 장고의 강점은 Model과 Form
- 물론, 장고에서도 다양한 ORM, 라이브러리 사용 가능합니다. 강력한 Model과 Form!
- 물론, 적절하게 섞어쓰실 수도 있습니다.
- https://docs.djangoproject.com/ko/2.1/topics/db/sql/
- 직접 SQL문자열을 조합하지마시고, 인자로 처리하세요! -> SQL Injection 방지
- from django.db import connection, connections
with connection.cursor() as cursor:
cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
row = cursor.fetchone()
print(row)

# 파이참에서 python manage.py runserver 명령어 후 에러 해결사항
- ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
- 파이참에서도 장고 설치되어 있지않기 때문에 -> pip install django
- 장고 업데이트 -> python -m pip install --upgrade pip

# Django Model(장고 내장 ORM)
- <데이터베이스 테이블>과 <파이썬 클래스>를 1:1로 매핑
- 모델 클래스명은 단수형으로 지정! ex) Posts(X), Post(O) : 클래스이기에 필히 첫 글자가 대문자인 PascalCase 네이밍
- 매핑되는 모델 클래스는 DB 테이블 필드 내역이 일치해야합니다.
- 모델을 만들기 전에, 서비스에 맞게 데이터베이스 설계가 필수.
- 이는 데이터베이스의 영역 -> 관계형 데이터베이스 학습도 필요.

<pre>
<code>
from django.db import models

class Post(models.Model):
title = models.CharField(max_length=100)
content = models.TextField()
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
</code>
</pre>

# 모델 활용 순서
- 장고 모델을 통해, 데이터베이스 형상을 관리할 경우
 1. 모델 클래스 작성
 2. 모델 클래스로부터 마이그레이션 파일 생성 -> makemigrations 명령
 3. 마이그레이션 파일을 데이터베이스에 적용 -> migrate 명령
 4. 모델 활용

- 장고 외부에서, 데이터베이스 형상을 관리할 경우
 - 데이터베이스로부터 모델 클래스 소스 생성 -> inspectdb 명령 모델 활용

# 모델명과 DB 테이블명
- DB 테이블명 : 디폴트 "앱이름_모델명"
blog앱
Post 모델 à "blog_post"
Comment 모델 à "blog_comment"
shop 앱
Item 모델 à "shop_item"
Review 모델 à "shop_review"
커스텀 지정
모델 Meta 클래스의 db_table 속성

https://docs.djangoproject.com/ko/3.0/ref/models/options/

# 새로운 모델을 만들어봅시다!
- shop/models.py 생성 후,
<pre>
<code>
from django.db import models

class Item(models.Model):
name = models.CharField(max_length=100)
desc = models.TextField(blank=True)
price = models.PositiveIntegerField()
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
</code>
</pre>

![비주얼스튜디오_1](https://user-images.githubusercontent.com/60806047/146732210-2bc03f04-dcb4-4e8a-9ebf-6cd2fe86458e.JPG)

<pre>
<code>
python manage.py startapp instagram
</code>
</pre>

- 위의 콘솔창에서 위의 프로젝트 생성하는 명령어를 입력해주시면

![비주얼스튜디오_2](https://user-images.githubusercontent.com/60806047/146732298-f7997c71-4e91-4ae7-8785-bfbac576b997.JPG)

- 위의 사진처럼 instagm 프로젝트 생성돼었음을 볼 수 있습니다!

![비주얼스튜디오_3](https://user-images.githubusercontent.com/60806047/146732589-c0131acc-f270-485e-943b-05d50a0678cf.JPG)

- askcompany -> "__pycache__" -> settings.py 들어가주시고

![비주얼스튜디오_4](https://user-images.githubusercontent.com/60806047/146732685-be422222-c041-4713-a10e-bf000a918a00.JPG)

- INSTALLED_APPS = [ ] 중에서 밑에 'instagram', 입력해주세요.

![비주얼스튜디오_5](https://user-images.githubusercontent.com/60806047/146732784-8efc6bbf-babc-4562-b71d-dfa9e03490a1.JPG)

- instagram -> migrations -> urls.py 이동

![비주얼스튜디오_6](https://user-images.githubusercontent.com/60806047/146732868-55a48f02-c2e0-4dcf-8075-90e449e96eed.JPG)

- 위의 사진처럼 똑같이 urlpatterns = [] 입력해주세요.

![비주얼스튜디오_7](https://user-images.githubusercontent.com/60806047/146732925-6fd1ff46-9fb2-4716-bdf9-aa84440311ab.JPG)

- askcompany -> __pycache__ -> urls.py 이동.

![비주얼스튜디오_8](https://user-images.githubusercontent.com/60806047/146732979-f8ea2022-ec9b-41bd-8a89-47e01cd83fc6.JPG)

<pre>
<code>
from django.urls.conf import include

path('instagram/', include('instagram.urls')),
</code>
</pre>

![비주얼스튜디오_9](https://user-images.githubusercontent.com/60806047/146732982-daddcaec-b15e-43be-b8cb-7b2b4290683c.JPG)

- models.py 이동

![비주얼스튜디오_11](https://user-images.githubusercontent.com/60806047/146732986-afc29943-62ca-476d-adcf-73b194930348.JPG)
<pre>
<code>
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now_add=True)
</code>
</pre>

- 입력해주세요.

![비주얼스튜디오_12](https://user-images.githubusercontent.com/60806047/146732987-97a9d4be-07dc-48be-9ad7-c0bc2d0854f8.JPG)
<pre>
<code>
python manage.py makemigrations instagram
</code>
</pre>

- 치고 나면 사진처럼 성공적으로 된겁니다!!

![비주얼스튜디오_13](https://user-images.githubusercontent.com/60806047/146732988-2b52cc3a-4b95-4489-aab3-e97a0309ceba.JPG)

- 다시
<pre>
<code>
python manage.py migrate instagram
</code>
</pre>

- OK라고 메시지 뜨면 성공적!

![비주얼스튜디오_14](https://user-images.githubusercontent.com/60806047/146732991-55c246c2-fe95-4b84-a848-bb940a84fe53.JPG)
<pre>
<code>
python manage.py sqlmigrate instagram 0001_initial
</code>
</pre>

![비주얼스튜디오_15](https://user-images.githubusercontent.com/60806047/146732994-7ee92605-fd7c-4afc-be7b-149f26c682c3.JPG)
<pre>
<code>
python manage.py dbshell
</code>
</pre>

- 쳐줍니다. 만약에 이렇게 sqlite3라고 에러 메시지가 뜨는 경우는 이와 관련 경로가 없다고 뜹니다. 이를 해결하기 위해서

https://www.sqlite.org/download.html

- 위의 링크를 눌러줍시다.

![비주얼스튜디오_16](https://user-images.githubusercontent.com/60806047/146732997-f06dcbb6-010f-41f6-a0dc-b6fcaf31cab1.JPG)

- 빨간 네모박스에 sqlite-dll-win32-x86-33700000.zip 라는 다운로드 받으시고 

![비주얼스튜디오_17](https://user-images.githubusercontent.com/60806047/146732999-c64766c3-6268-4fd2-b65c-946f075df79d.JPG)

- 사진처럼 압축 푸셔서 sqlite3라는 파일을 복사하셔서

![비주얼스튜디오_18](https://user-images.githubusercontent.com/60806047/146733003-d3fc4745-294f-4053-89ad-528b142c2d79.JPG)

- 자신이 생성했던 폴더에 붙어넣으면 됩니다!!

![비주얼스튜디오_19](https://user-images.githubusercontent.com/60806047/146733004-84d74206-9bdd-4c8d-afe3-2cdb29e97447.JPG)

- 다시

<pre>
<code>
python manage.py dbshell
</code>
</pre>

- 치면은 밑에 나오는 sqlite> 이가 나오면 성공입니다!

![비주얼스튜디오_20](https://user-images.githubusercontent.com/60806047/146733009-4315a54e-f092-42f7-8f8d-71325ac6d756.JPG)

- 사진처럼 해보시고,

![비주얼스튜디오_21](https://user-images.githubusercontent.com/60806047/146733013-8b89ea86-cef5-41cb-bdd2-ba3031c3d5ca.JPG)

- sql 종료 명령어는 .quit 입니다!

# 장고 모델 필드

- 기본 지원되는 모델필드 타입(1)
 - Primary Key: AutoField, BigAutoField
 - 문자열 : CharField, TextField, SlugField
 - 날짜/시간 : DateField, TimeField, DateTimeField, DurationField
 - 참/거짓 : BooleanField, NulLBooleanField
 - 숫자 : ItegerField, SmallIntegerField, PositivveIntegerField, PositiveSmallIntegerField, BigIntegerField, DecimalField, FloatField
 - 파일 : BinaryField, FileField, ImageField, FillePathField

https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types

- 기본 지원되는 모델필드 타입(2)
 - 이메일 : EmailField
 - URL : URLField
 - UUID : UUIDField
 - 아이피 : GenericlPAddressField
 - Relationship Types
   - ForeignKey
   - ManyToManyField
   - OneToOneField

다양한 커스텀 필드들 확인하고 싶으면 아래의 링크 클릭!
https://django-model-utils.readthedocs.io/en/latest/

# 모델필드들은 DB 필드타입을 반영
 - DB에서 지원하는 필드들을 반영
  - Varchar 필드타입 -> CharField, SlugField, URLField, EmilField 등
 - 파이썬 데이터타입과 데이터베이스 데이터타입을 매핑
  - AutoFiled -> int
  - BinaryField -> bytes
  - booleanField -> bool
  - CharField/SlugField/URLField/EmailField -> str : 디폴트 적용된 유효성 검사 등의 차이
 - 같은 모델필드라 할지라도, DB에 따라 다른 타입이 될 수도 있습니다.
  - DB에 따라 지원하는 기능이 모두 달라요.

# 자주 쓰는 필드 공통 옵션
 - blank : 장고 단에서 validation시에 empty 허용 여부(default : False)
 - null(DB 옵션) : null 허용 여부(default : False)
 - db_index(DB 옵션) : 인덱스 필드 여부(default : False)
 - default : 디폴트 값 지정, 혹은 값을 리턴해줄 함수 지정
  - 사용자에게 디폴트값을 제공코자 할 때
 - unique(DB 옵션) : 현재 테이블 내에서 유일성 여부(default : False)
 - choices : select 박스 소스로 사용
 - validators : validators를 수행할 함수를 다수 지정
  - 모델 필드에 따라 고유한 validators들이 등록(ex_이메일만 받기
 - verbose_name : 필드 레이블, 미지정시 필드명이 사용
 - help_text : 필드 입력 도움말
 
<pre>
<code>
from django.conf import settings
from django.db import models

class Profile(models.Model):
 user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 blog_url = models.URLField(blank=True)

class Post(models.Model):
 author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 title = models.CharField(max_length=100, db_index=True)
 slug = models.SlugField(allow_unicode=True, db_index=True) # ModelAdmin.prepopulated_fields 편리
 desc = models.TextField(blank=True)
 image = models.ImageField(blank=True) # Pillow 설치가 필요
 comment_count = models.PositiveIntegerField(default=0)
 tag_set = models.ManyToManyField('Tag', blank=True)
 is_publish = models.BooleanField(default=False)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
 author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 post = models.ForeignKey(Post, on_delete=models.CASCADE)
 message = models.TextField()
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
 name = models.CharField(max_length=50, unique=True)
</code>
</pre>

# 강력히 권고!!
- 설계한 데이터베이스 구조에 따라, 최대한 필드타입을 타이트하게 지정해주는 것이, 입력값 오류를 막을 수 있음.

<pre>
<code>
blank/null 지정은 최소화해주세요. -> manage.py inspect 명령을 통해 생성된 모델 코드는 초안입니다.
validators 들이 다양하게/타이트하게 지정됩니다.
필요하다면, validators들을 추가로 타이트하게 지정해주세요.
프론트엔드에서의 유효성 검사는 사용자 편의를 위해서 수행하며, 백엔드에서의 유효성 검사는 필수입니다.
직접 유효성 로직을 만들지 마세요. 이미 잘 구성된 Features들을 가져다 쓰세요. 장고의 Form/Model을 통해 지원되며,
django-rest-framework의 Serializer를 통해서도 지원됩니다.

ORM은 SQL 쿼리를 만들어주는 역할일 뿐, 보다 성능높은 애플리케이션을
위해서는, 사용하실려는 데이터베이스에 대한 깊은 이해가 필요합니다.
</code>
</pre>

# 장고 admin을 통한 데이터 관리(기초)
- django admin
 - django.contrib.admin 앱을 통해 제공
  - 디폴트 경로 : /admin/ -> 실제 서비스에서는 다른 주소로 변경 권장!! 혹은 django-admin-honeypot 앱을 통해, 가짜 admin 페이지 노출
 - 모델 클래스 등록을 통해, 조회/추가/수정/삭제 웹UI를 제공
  - 서비스 초기에, 관리도구로서 사용하기에 제격
  - 관리도구 만들 시간을 줄이고, End-User 서비스에 집중!
 - 내부적으로 Django Form을 적극적으로 사용

# 모델 클래스를 admin에 등록하기
<pre>
<code>
from django.contrib import admin
from .models import Item
# 등록법 #1
admin.site.register(Item) # 기본 ModelAdmin으로 동작
# 등록법 #2
class ItemAdmin(admin.ModelAdmin):
pass
admin.site.register(Item, ItemAdmin) # 지정한 ModelAdmin으로 동작
# 등록법 #3
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
pass
</code>
</pre>

- instargram -> models.py 이동
![비주얼스튜디오_model 생성_4](https://user-images.githubusercontent.com/60806047/146858546-8f1fc317-00f9-4871-bfc9-b869147ad7a1.JPG)

# 입력하기
![비주얼스튜디오_model 생성_6](https://user-images.githubusercontent.com/60806047/146858650-314820fd-c569-43ff-ae31-a629ffdfcd29.JPG)
![비주얼스튜디오_model 생성_7](https://user-images.githubusercontent.com/60806047/146858660-86a3a955-d76d-4d9c-a43a-8b84d61501bf.JPG)
![비주얼스튜디오_model 생성_8](https://user-images.githubusercontent.com/60806047/146858668-b788eafc-e465-4b48-8e2c-ebf9bb37c548.JPG)
![비주얼스튜디오_model 생성_9](https://user-images.githubusercontent.com/60806047/146858675-65dc93ab-742a-467b-8e01-8ff46cdc8c9e.JPG)

# 모델 클래스에 __str__구현(admin모델 리스트에서 "모델명 object"를 원하는 대로 변경하기 위해
- 객체를 출력할 때, 객체.__str__()의 리턴값을 활용
<pre>
<code>
from django.db import models
class Item(models.Model):
name = models.CharField(max_length=100)
desc = models.TextField(blank=True)
price = models.PositiveIntegerField()
is_publish = models.BooleanField(default=False)
def __str__(self):
return f'<{self.pk}> {self.name}'
</code>
</pre>

![비주얼스튜디오_model 생성_14](https://user-images.githubusercontent.com/60806047/146858851-74287dd2-3ff2-4588-8064-43d840ebf443.JPG)

- models.py
![비주얼스튜디오_model 생성_10](https://user-images.githubusercontent.com/60806047/146858892-edb192a1-d4d5-437b-85d8-cca17209d6ac.JPG)
- 9~10라인 작성하시면

<pre>
<code>
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
list_display = ['id', 'message', 'creadted_at', 'updated_at']
</code>
</pre>

![비주얼스튜디오_model 생성_11](https://user-images.githubusercontent.com/60806047/146858918-2b43b8ba-b70e-43a8-9609-64bf0e563acb.JPG)

- 이렇게 사진처럼 ID, MESSAGE, EREATED AT, UPDATED AT와 같은 표가 보입니다!

![비주얼스튜디오_model 생성_12](https://user-images.githubusercontent.com/60806047/146859067-701d6308-27a5-4627-ba89-cba209971d40.JPG)

<pre>
<code>
list_display_links = ['message']
</code>
</pre>

![비주얼스튜디오_model 생성_17](https://user-images.githubusercontent.com/60806047/146859214-3cf4887a-458e-440b-a599-5695d0701233.JPG)
- instargam -> models.py

<pre>
<code>
def message_length(self):
 return len(self.message)
message_length.short_description = "메시지 글자수"
</code>
</pre>

![비주얼스튜디오_model 생성_18](https://user-images.githubusercontent.com/60806047/146859291-270d65dd-3617-4d81-9814-59e45102d48b.JPG)

- 이렇게 열의 이름이 "메시지 글자수"로 바뀌는 점을 알 수 있습니다.

- instagram -> admin.py 이동

![비주얼스튜디오_model 생성_19](https://user-images.githubusercontent.com/60806047/146859344-0cffe0d5-65d8-4bed-807d-42d678359ffc.JPG)

<pre>
<code>
def message_length(self, post):
 return f"{len(post.message)} 글자"
</code>
</pre>

![비주얼스튜디오_model 생성_20](https://user-images.githubusercontent.com/60806047/146859535-228c5561-7fa7-41be-a2f3-31ee5337d1e3.JPG)
- 1 "글자", 3 "글자" / 옆에 글자가 붙인걸 확인할 수 있어요!

# shell로 명령어 확인해보세요!(선택사항)
- 콘솔창에서 Ctrl + c 누르면 종료됩니다.

![비주얼스튜디오_model 생성_21](https://user-images.githubusercontent.com/60806047/146859603-a1d0c131-d01f-4bed-bc1c-e04284e913f1.JPG)

<pre>
<code>
python manage.py shell
</code>
</pre>

![비주얼스튜디오_model 생성_22](https://user-images.githubusercontent.com/60806047/146859675-ed064ff5-634d-4863-bfc6-4f41c408be38.JPG)
![비주얼스튜디오_model 생성_23](https://user-images.githubusercontent.com/60806047/146859683-abc05eb0-e2fb-4e58-9e4b-4b009dcd60ca.JPG)
![비주얼스튜디오_model 생성_24](https://user-images.githubusercontent.com/60806047/146859704-af293283-5a8a-417b-98db-e26d9a511fad.JPG)

- 이렇게 값을 제대로 불러오는 걸을 확인할 수 있습니다!
- shell 종료명령어는 .exit() 입니다!

## 파이썬 설치
- 1. https://www.python.org/
- 2. ![python_install_1](https://user-images.githubusercontent.com/60806047/146522767-90b390a9-47dc-46e3-b350-61bb4f2ac68a.JPG)
- 3. ![python_install_2](https://user-images.githubusercontent.com/60806047/146522796-f4bdebc8-44f5-4511-a24a-bae0bab6373b.jpg)
- 4. Add Python 3.10 to PATH 체크한 다음에 [Install Now] 눌러야 설치 완료!!

## Visual Studio Code 설치
- https://code.visualstudio.com/
- 위의 링크 들어가셔서 빨간색 네모 누르면 다운로드 뜨면 설치하셔서 완료되면 끝입니다!
![VisualStudioCode_install](https://user-images.githubusercontent.com/60806047/146671957-78fb3e09-3905-46da-8280-ea27dee38780.jpg)

## 장고 설치
- https://github.com/django/django
- 윈도우키 누르고 검색창에 cmd 입력하시고나서, pip install django 입력하고 엔터치면 다운로드하는 모습을 볼 수 있습니다.(현재 버전 3.2.10 / 2021년 12월 19일 기준)입니다.

# 🥺 파이참 설치
https://wikidocs.net/21953

# 😡 아나콘다 설치(굳이 선택사항이고 안해도 되는 설치입니다)
https://wikidocs.net/22896

# 💩 파이참에서 모듈 설치하는 방법
https://appia.tistory.com/209
