# RDBMS에서의 관계 예시
- 1 : N 관계 -> models.ForeignKey로 표현
  - 1명의 유저가 쓰는 다수의 포스팅(Post)
  - 1명의 유저가 쓰는 다수의 댓글
  - 1개의 포스팅에 다수의 댓글
- 1 : 1 관계 -> models.OneoOneField로 표현
  - 1명의 유저는 1개의 프로필
- M : N 관계 -> models.ManyToManyRield로 표현
  - 1개의 포스팅에는 다수의 태그 = 1개의 태그ㅔ는 다수의 포스팅

# ForeignKey
- 1 : N 관계에서 N측에 명시
  - ex) Post:Comment, user:Post, user:Comment
- ForeignKey(to, on_delete)
  - to : 대상모델 : 클래스를 직접 지정하거나, 클래스명을 문자열로 지정. 자기 참조는 "self" 지정한다.
  - on_delete : Record 삭제 시 Rule : https://docs.djangoproject.com/en/2.1/ref/models/fields/
#django.db.models.ForeignKey.on_delete
    - CASCADE : FK로 참조하는 다른 모델의 Record도 삭제
    - PROTECT : ProtectedError (IntegrityError 상속) 를 발생시키며, 삭제 방지
    - SET_NULL : null로 대체. 필드에 null=True 옵션 필수.
    - SET_DEFAULT : 디폴트 값으로 대체. 필드에 디폴트값 지정 필수.
    - SET : 대체할 값이나 함수 지정. 함수의 경우 호출하여 리턴값을 사용.
    - DO_NOTHING : 어떠한 액션 X. DB에 따라 오류가 발생할 수도 있습니다.
    
# 올바른 User 모델 지정

- django/contrib/auth/models.py
  - class User(AbstractBaseUser): ...
 
- blog/models.py
  - class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    >>> user.post_set.all()
 
 # migration(s)이란?
 - Django의 모델에서 설정한 데이터베이스의 테이블 구조를 데이터베이스에 적용시키기 위한 기록으로 볼 수 있다.
