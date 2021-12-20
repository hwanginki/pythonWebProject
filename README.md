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
</pre>
</code>

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
