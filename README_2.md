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






















