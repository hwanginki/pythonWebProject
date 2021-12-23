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
- 
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







