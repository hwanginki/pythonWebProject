# medai 파일을 다루는 방법

Static & Media 파일

- Static 파일
  - 개발 리소스로서의 정적인 파일 (js, css, image 등)
  - 앱 / 프로젝트 단위로 저장/서빙
- Media 파일
  - FileField/ImageField를 통해 저장한 모든 파일
  - DB필드에는 저장경로를 저장하며, 파일은 파일 스토리지에 저장
    - 실제로 문자열을 저장하는 필드 (중요)
  - 프로젝트 단위로 저장/서빙
  
# Mdeia 파일 처리 순서
1. HttpRequest.FILES를 통해 파일이 전달
2. 뷰 로직이나 폼 로직을 통해, 유효성 검증을 수행하고,
3. FileField/ImageField 필드에 ”경로(문자열)”를 저장하고,
4. settings.MEDIA_ROOT 경로에 파일을 저장합니다.
  
# Media 파일, 관련 settings 예시
- 각 설정의 디폴트 값
  - MEDIA_URL = ""
    - 각 media 파일에 대한 URL Prefix
    - 필드명.url 속성에 의해서 참조되는 설정
  - MEDIA_ROOT = ""
    - 파일필드를 통한 저장 시에, 실제 파일을 저장할 ROOT 경로

# 이미지 추가 설치하기 위한 설정

- models.py 이동
  
![장고_1](https://user-images.githubusercontent.com/60806047/147026650-3f0849b4-71d5-4d41-97af-0925ce3958be.JPG)
  
- 콘솔창에서

![장고_2](https://user-images.githubusercontent.com/60806047/147026792-0d1750a9-d2e9-4fc8-970d-ad989d236f31.JPG)
  
<pre>
<code>
pip install pillow
</code>
</pre>

![장고_3](https://user-images.githubusercontent.com/60806047/147026843-64da494d-a19b-4555-825d-70d5b33ba2cd.JPG)

- 다운로드 되셨으면

![장고_5](https://user-images.githubusercontent.com/60806047/147026919-038c3caa-999e-4015-a2e7-41b808a113ce.JPG)
  
<pre>
<code>
pip install -r requirements.txt
</code>
</pre>
  
- 입력해주세요.
  
![장고_4](https://user-images.githubusercontent.com/60806047/147026997-b379690d-3bf9-4dd8-89a6-f4db29aaea54.JPG)

- 사진처럼 requirement.txt이라는 txt파일을 생성되었음을 볼 수 있습니다!!

![장고_6](https://user-images.githubusercontent.com/60806047/147027061-46e5d50e-8524-4ee6-939b-6d5b91275022.JPG)

![장고_9](https://user-images.githubusercontent.com/60806047/147027165-be523d62-d7ee-42d4-b711-fa8485729dcc.JPG)

![장고_7](https://user-images.githubusercontent.com/60806047/147027074-1a0eb5d2-f068-452e-ac0a-0e63636762a8.JPG)

![장고_7_1](https://user-images.githubusercontent.com/60806047/147027102-c59178dd-c7fa-4605-8b0a-d58142b2b486.JPG)

- settings.py 이동

![장고_11](https://user-images.githubusercontent.com/60806047/147027337-a4d54270-bd32-4a52-a03e-764355bc7f52.JPG)

- urls.py 이동

![장고_12](https://user-images.githubusercontent.com/60806047/147027437-a979f343-1f20-44b5-9991-0a9ff34c8c62.JPG)

- 28~29라인 작성

- admin.py 이동

![장고_13](https://user-images.githubusercontent.com/60806047/147027475-fa74408e-673a-4574-8585-1b958d4871f7.JPG)

- 15~18라인 작성

![장고_14](https://user-images.githubusercontent.com/60806047/147027503-63bf5d6c-29fc-4ee3-ae0a-bd4476ddb1c0.JPG)

- 이렇게 볼 수 있어요

- urls.py 이동

![장고_15](https://user-images.githubusercontent.com/60806047/147027538-8fe2eeba-1ce7-44fd-b0b5-233b17748eb3.JPG)

- 이렇게 작성하세요.

- 새로고침 하시면

![장고_16](https://user-images.githubusercontent.com/60806047/147027616-63f77924-3a45-41eb-bd65-13fc691edc02.JPG)

- 사진처럼 뜰 수 가 있어요!

![장고_17](https://user-images.githubusercontent.com/60806047/147027654-31d17fbb-1de3-40a4-a373-e37581b3518e.JPG)

- 6라인은 이미지 수정할 때 바뀐 이미지로 처리해주는 부분입니다.

# 주피터 활용하기
- 기본 파이썬 쉘로는 바로 장고 프로젝트의 리소스(모델, 템플릿 등)를 활용하실 수 없습니다! 이유는 장고 로딩 과정을 거치지 않았기 때문에 장고 프로젝트가 로딩된 쉘을 획득하는 방법에 대해서 살펴봅시다!

- 주피터 노트북 실행하기 위해서 아나콘다(Python 3.9 지원) 설치가 필요합니다.

- https://www.anaconda.com/products/individual

- 비주얼스튜디오 코드에서 jupyter notebook(주피터 노트북) 실행하는 방법

![주피터1](https://user-images.githubusercontent.com/60806047/147179943-76a570b2-bf8e-4d61-ba94-90e7c4f85c42.JPG)

- 우선 콘솔창에서 pip install jupyter 명령어 치구요

![주피터2](https://user-images.githubusercontent.com/60806047/147179948-30cd0676-8c55-45a6-88db-bc144b39bc76.JPG)
- pip install ipykernel

![주피터3](https://user-images.githubusercontent.com/60806047/147179949-ffbeaf59-dbbd-4e9f-a9b0-27cb7ab93ada.JPG)
- python -m ipykernel install --user --name conda --display-name conda

![주피터4](https://user-images.githubusercontent.com/60806047/147179951-8526b0dd-1f5b-4a9b-a4c2-072763b4d229.JPG)
- jupyter notebok

![주피터5](https://user-images.githubusercontent.com/60806047/147179953-0df4e322-1787-47b7-adfc-53a24b1436bb.JPG)
- 주피터라는 브라우저가 자동 불러지면 성공입니다.

![주피터6](https://user-images.githubusercontent.com/60806047/147179960-198395d9-129d-4b8c-948e-96db38660ca2.JPG)
- New 클릭하셔서 Python 3 나오면 클릭해주세요. 옆에는 이름입니다.

![주피터7](https://user-images.githubusercontent.com/60806047/147179961-2cd7d2f2-729b-4b1a-83a9-58ee7f4d2acb.JPG)

- 빨간색 네모표시보시면 Python 3(이름) 보여주시고요.
- 여기서 입력창에 일단 이렇게 입력합시다.

<pre>
<code>
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'askcompany.settings'
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = "true"
</code>
</pre>

- 입력하고나서 "Ctrl + Enter" 누르면 실행됩니다.

- 그리고

![주피터8](https://user-images.githubusercontent.com/60806047/147179963-17ebda07-9fcd-4f9d-a3af-da7c72d3433e.JPG)
- "B" 버튼 누르시면 새로운 입력창이 생성됩니다. 거기서 입력하시면 되구요.

<pre>
<code>
import os
import django
django.setup()
</code>
</pre>

- Ctrl + Enter 눌렀는데 갑자기 사진처럼 에러가 떴다?
- 이유는 장고(django)이라는 모듈 설치되어있지 않기 때문입니다.

![주피터9](https://user-images.githubusercontent.com/60806047/147179964-6d156634-acfb-4b0e-b2bd-e0de7f6c9058.JPG)
- pip list
- 입력해서 설치관련 리스트가 나오는데 거기서 검색해도 django라는 글이 없겠죠.

![주피터10](https://user-images.githubusercontent.com/60806047/147179965-3317be59-7cb0-46ad-b808-b0383509be78.JPG)
- pip install django 입력해서 [*]는 설치중이라고 기다리시면

![주피터11](https://user-images.githubusercontent.com/60806047/147179967-4d0e42e6-a232-4bec-adc5-cb8ec982ea24.JPG)
- 갑자기 설치하는 도중에 이렇게 에러가 떴다면? 이유는 pip 버전이 낮기 때문에 업그레이드 해야됩니다.

![주피터12](https://user-images.githubusercontent.com/60806047/147179968-eb211e04-fff4-49d9-b500-2db7a6d098d2.JPG)
- pip install --upgrade pip
- 명령어 친 후 기다리면

![주피터13](https://user-images.githubusercontent.com/60806047/147179970-bc4f73ca-111e-4791-be3a-568a00b4d518.JPG)
- 이렇게 pip의 버전이 업그레이드가 성공적으로 메시지가 나오면 완료 된겁니다.

![주피터14](https://user-images.githubusercontent.com/60806047/147179972-afecc66f-5ab0-4c96-b0f1-89263e230ee4.JPG)
- 다시 이렇게 입력하시구요. 기다리고 되면

![주피터15](https://user-images.githubusercontent.com/60806047/147179973-4076ac70-1123-4bc0-ad5d-1bbb0aa0edde.JPG)
- 이렇게 치면 될겁니다. 아마도

![주피터16](https://user-images.githubusercontent.com/60806047/147179977-0bab8a54-747a-4f09-9261-eac762c1a7bb.JPG)

<pre>
<code>
from instagram.models import Post
</code>
</pre>
- 이렇게 실행하고

<pre>
<code>
qs = Post.objects.all()
print(qs.query)
</code>
</pre>
- 실행하고나서 이렇게 나오면 성공적으로 된겁니다!!!

# 모델을 통한 조회(기초)
- Model Manager
  - 데이터베이스 질의 인터페이스를 제공합니다. 디폴트 Manager로서 ModelCls.objects가 제공합니다.

생성되는 대강의 SQL 윤곽 -> SELECT * FROM app_model;
- ModelCls.objects.all()

![주피터를 이용한 모델 활용_1](https://user-images.githubusercontent.com/60806047/147302035-bf9c8a78-86ae-4427-a321-ad2687954564.JPG)

생성되는 대강의 SQL 윤곽 à SELECT * FROM app_model ORDER BY id DESC LIMIT 10;
- ModelCls.objects.all().order_by('-id')[:10]

![주피터를 이용한 모델 활용_2](https://user-images.githubusercontent.com/60806047/147302040-afecfb66-2034-4508-8231-517b23347fad.JPG)
![주피터를 이용한 모델 활용_3](https://user-images.githubusercontent.com/60806047/147302045-131f09dd-88d9-424b-a13e-4bf928802b7d.JPG)
![주피터를 이용한 모델 활용_4](https://user-images.githubusercontent.com/60806047/147302070-3465caf9-c3e8-4ff2-b30a-7718b6b24509.JPG)

생성되는 대강의 SQL 윤곽 à INSERT INTO app_model (title) VALUES (“New Title”);
- ModelCls.objects.create(title="New Title")

# QuerySet
- SQL을 생성해주는 인터페이스!! 순회가능한 객체임
- Model Manager를 통해, 해당 Model에 대한 QuerySet을 획득!
<pre>
<code>
Post.objects.all() 코드는 "SELECT * FROM post ...;"
Post.objects.create(…) 코드는 "INSERT INTO …...;"
</code>
</pre>

# QuerySet은 Chaining을 지원
- Post.objects.all().filter(...).exclude(...).filter(...) -> QuerySet
- QuerySet은 Lazy한 특성
  - QuerySet을 만드는 동안에는 DB접근을 하지 않습니다.
  - 실제로 데이터가 필요한 시점에 접근을 합니다.
- 데이터가 필요한 시점은 언제인가?
  - qryset
  - print(queryset)
  - list(queryset)
  - for instance in queryset: print(instance)

# 다양한 조회요청 방법
- 조건을 추가한 Queryset, 획득할 준비
  - queryset.filter(...) -> qeuryset
  - queryset.exclude(...) -> querryset
 
![주피터를 이용한 모델 활용_5](https://user-images.githubusercontent.com/60806047/147302083-24b1f4ab-ce57-4f80-adc4-7ca1c83a4909.JPG)
![주피터를 이용한 모델 활용_6](https://user-images.githubusercontent.com/60806047/147302093-8fa8ad86-4833-4a94-955e-4d5c500c84bf.JPG)

- 특정 모델객체 1개 획득을 시도
  - queryset[숫자인덱스]
    - 모델객체 혹은 예외발생(IndexError)
  - queryset.get(...)
    - 모델객체 혹은 예외발생(DoesNotExisst, MultipleObjectsReturned
  - queryset.first() -> 모델객체 혹은 None
  - queryset.last() -> 모델객체 혹은 None

![주피터를 이용한 모델 활용_7](https://user-images.githubusercontent.com/60806047/147302120-6d5367b6-5d09-4628-a241-2d085cce972e.JPG)
![주피터를 이용한 모델 활용_8](https://user-images.githubusercontent.com/60806047/147302124-0abb5028-08af-4e8a-b0cb-cf7b3eabedeb.JPG)
![주피터를 이용한 모델 활용_9](https://user-images.githubusercontent.com/60806047/147302126-d43362a5-b3af-4d8e-b095-8c48bd06f43a.JPG)
![주피터를 이용한 모델 활용_10](https://user-images.githubusercontent.com/60806047/147302132-1cd273ad-c9a6-4fca-8991-80c1b6f9a2a2.JPG)

# 필드 타입별 다양한 조건 매칭
 - 주의) 데이터베이스에 따라 생성되는 SQL이 다릅니다.
  - 숫자/날짜/시간 필드
  <pre>
  <code>
    필드명__lt = 조건값 è 필드명 < 조건값
    필드명__lte = 조건값 è 필드명 <= 조건값
    필드명__gt = 조건값 è 필드명 > 조건값
    필드명__gte = 조건값 è 필드명 >= 조건값  
  </code>
  </pre>

  - 문자열 필드
  <pre>
  <code>
    필드명__startswith = 조건값 è 필드명 LIKE “조건값%”
    필드명__istartswith = 조건값 è 필드명 ILIKE “조건값%”
    필드명__endswith = 조건값 è 필드명 LIKE “%조건값”
    필드명__iendswith = 조건값 è 필드명 ILIKE “%조건값”
    필드명__contains = 조건값 è 필드명 LIKE “%조건값%”
    필드명__icontains = 조건값 è 필드명 ILIKE “%조건값%”
  </code>
  </pre>

# 실전예제) Item 목록/간단검색 페이지

- instagram > views.py 이동

![비주얼스튜디오_Queryset을 통한 검색구현_1](https://user-images.githubusercontent.com/60806047/147305735-f9dc5b91-abfd-4126-a65d-0e9440360151.JPG)

<pre>
<code>
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
    })
</code>
</pre>

![비주얼스튜디오_Queryset을 통한 검색구현_2](https://user-images.githubusercontent.com/60806047/147305799-1b31e86d-d658-4662-b3b4-95b1da23c2bd.JPG)

- instagram 폴더에서 templates 폴더 생성하고 intagram 폴더 생성해주세요. 사진처럼
- 그리고나서 post_list.html 파일 생성해주세요.

- instagram > urls.py

![비주얼스튜디오_Queryset을 통한 검색구현_3](https://user-images.githubusercontent.com/60806047/147305863-655515ac-0fa0-4384-9443-42cd76d15b20.JPG)

<pre>
<code>
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
]
</code>
</pre>

- instagram > templates > instagram > post_list.html 이동

![비주얼스튜디오_Queryset을 통한 검색구현_5](https://user-images.githubusercontent.com/60806047/147305938-8727a209-cd24-4ee4-88cd-3f6f9dd9fa57.JPG)

- ! 치고 자동완성창이 보이면 ! 엔터눌러주세요.

![비주얼스튜디오_Queryset을 통한 검색구현_6](https://user-images.githubusercontent.com/60806047/147305961-68165675-7cbc-4fdb-bf44-444461083b25.JPG)

- 사진처럼 <body> {{ post_list }} </body> 입력해주세요.

![비주얼스튜디오_Queryset을 통한 검색구현_7](https://user-images.githubusercontent.com/60806047/147305998-e14b6827-2043-4528-b39e-0a46806f6f3d.JPG)

- 실행하고 주소창에 ../instagram 입력해서 이렇게 볼 수 있습니다.

![비주얼스튜디오_Queryset을 통한 검색구현_8](https://user-images.githubusercontent.com/60806047/147306021-83948f1a-0e50-438d-8c06-6a7a0f7110d7.JPG)

<pre>
  <code>
      {% for post in post_list %}
        {{ post.photo }}
        {{post.message }}
      {% endfor %}
  </code>
</pre>

- tabel, tbody이라는 태크 입력하고 이렇게 작성해주세요.

![비주얼스튜디오_Queryset을 통한 검색구현_9](https://user-images.githubusercontent.com/60806047/147306110-b4f81606-8714-41a0-ac59-ad56f1d08aee.JPG)

- 실행하면 이렇게 이미지같이 나올 수 있습니다.

![비주얼스튜디오_Queryset을 통한 검색구현_10](https://user-images.githubusercontent.com/60806047/147306159-87c90e6a-5096-41d8-b478-7678422de13a.JPG)

- 이렇게 작성해주시고

![비주얼스튜디오_Queryset을 통한 검색구현_11](https://user-images.githubusercontent.com/60806047/147306173-ef677a13-4833-4687-b678-cd1464a17ff9.JPG)

- 한개아니라 등록했던거 다 같이 나오죠? 그런데 이거 보기좀 그렇지만
  
- 부트스트랩이라는 템플렛을 이용해서 방금 페이지를 꾸미려고 합니다
- https://getbootstrap.com/
 
![비주얼스튜디오_Queryset을 통한 검색구현_12](https://user-images.githubusercontent.com/60806047/147306228-0cfd1f70-7a69-4d13-8007-c658a465f3ae.JPG)
  
- 아래로 이동하셔서

![비주얼스튜디오_Queryset을 통한 검색구현_13](https://user-images.githubusercontent.com/60806047/147306258-7afb6727-3136-43e9-93f9-8713defa11fd.JPG)

- 저거 Copy 복사해주세요.

![비주얼스튜디오_Queryset을 통한 검색구현_14](https://user-images.githubusercontent.com/60806047/147306329-f2a8fdd1-743f-4b92-8536-e9fd69bce45e.JPG)

- 사진처럼 meta과 title에 사이에 넣어주시면 됩니다!!

![비주얼스튜디오_Queryset을 통한 검색구현_15](https://user-images.githubusercontent.com/60806047/147306347-458620b5-ed4f-4255-b29c-b82dd795d8c2.JPG)

- 이렇게 작성하시면 되겠습니다.

![비주얼스튜디오_Queryset을 통한 검색구현_16](https://user-images.githubusercontent.com/60806047/147306425-d3f0a0b8-0da6-4233-bdc4-1c109e35cc44.JPG)

- 사진처럼 이미지가 잘 불러올 수 있죠?
  
- 검색버튼 생성하려고 합니다!
  
![비주얼스튜디오_Queryset을 통한 검색구현_17](https://user-images.githubusercontent.com/60806047/147306445-b03754ed-c18e-493f-8582-27ab8bef4c19.JPG)
  
![비주얼스튜디오_Queryset을 통한 검색구현_18](https://user-images.githubusercontent.com/60806047/147306502-90f4b9d5-dfc7-4e2a-8368-aad718c3dbac.JPG)

- 사진처럼 검색 인풋 생기고, 버튼도 생성되었음을 볼 수 있습니다.
  
![비주얼스튜디오_Queryset을 통한 검색구현_19](https://user-images.githubusercontent.com/60806047/147306530-8548748e-f464-4103-bb5c-a5f5bc1fa90b.JPG)

- 검색창에 ddd 검색하니까 검색 잘 됐습니다!
  
# 정렬 조건 추가하기 - SELECT 쿼리에 "ORDER BY" 추가
- 정렬 조건을 추가하지 않으면 일관된 순서를 보장받을 수가 없습니다!!
- DB에서 다수 필드에 대한 정렬을 지원하지만, 가급적 단일 필드로 하는 것이 성능에 이익
- 시간순 / 역순 정렬이 필요할 경우, id 필드를 활용해볼 수 있음.
- 정렬 조건을 지정하는 2가지 방법
  1. (추천방법) 모델 클래스의 "Meta" 속성으로 ordering 설정 : list로 지정
  2. 모든 queryset에 order_by(...)에 지정

![Queryset의 정렬 및 범위 조건_1](https://user-images.githubusercontent.com/60806047/147314474-8ed2f0f0-1d38-4972-ba12-d76591c3eb91.JPG)

- pip install django-extensions 설치

<pre>
<code>
python manage.py shell_plus --print-sql --ipython
</code>
<pre>

- askcompany > settings.py

![Queryset의 정렬 및 범위 조건_2](https://user-images.githubusercontent.com/60806047/147314490-841ba511-f42d-4930-9db4-1ba2ced30cdb.JPG)

- 42라인, 'django_extenstion',

- 이렇게 저장해야 shell 실행할 수 있습니다.

![Queryset의 정렬 및 범위 조건_3](https://user-images.githubusercontent.com/60806047/147314528-d27e6021-ae57-41fe-9361-e25f6e9c0d90.JPG)

<pre>
<code>
 python manage.py shell_plus --print-sql --ipython
</code>
</pre>

- In [1]: 안에 명령어 입력!

![Queryset의 정렬 및 범위 조건_4](https://user-images.githubusercontent.com/60806047/147314595-3d606534-8014-47b2-b2e0-8ddf9e608c9c.JPG)

- from instagram.models import Post

![Queryset의 정렬 및 범위 조건_5](https://user-images.githubusercontent.com/60806047/147314608-d0d21065-559a-44ce-9c72-26531d29bb64.JPG)

- Post.objects.all() 사용하기

![Queryset의 정렬 및 범위 조건_6](https://user-images.githubusercontent.com/60806047/147314619-b65221af-bac9-41c7-bb9f-ed7469a4e9cd.JPG)

- instagram > models.py > 21~22 작성

![Queryset의 정렬 및 범위 조건_6](https://user-images.githubusercontent.com/60806047/147314671-cccac303-be53-4544-804e-59faadea79f1.JPG)

- 다시 Post.objects.all() 확인

![Queryset의 정렬 및 범위 조건_7](https://user-images.githubusercontent.com/60806047/147314690-a253c660-0363-4031-af0b-0789d3fa8812.JPG)

- 만약에 이렇게 안나오면, In[n]에서 exit() 명렁어 친 후, 다시 python manage.py shell_plus --print-sql --ipython 입력

![Queryset의 정렬 및 범위 조건_8](https://user-images.githubusercontent.com/60806047/147314730-93a934ab-6e2b-4aaa-a510-0762d5bf4157.JPG)

- Post.objects.all().order_by('created_at') 확인

![Queryset의 정렬 및 범위 조건_9](https://user-images.githubusercontent.com/60806047/147314749-878ab53e-49fe-4497-801c-809043b902e8.JPG)

- Post.objects.all().order_by('id')[:2] 확인


