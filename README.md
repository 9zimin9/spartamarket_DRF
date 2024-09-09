# spartamarket_DRF

>
**1. Project 이름 :** spartamarket_DRF
><br/> 
**2. 프로젝트 기간 :** 2024.09.06 ~ 09.10
><br/>
**3. 개발언어 :** Python & Django & Django REST Framework(DRF)
><br/>
**4. 멤버:** 남지민(개인)
><br/>
**5. 기능 :** 회원가입, 로그인, 로그아웃, 프로필 조회, 게시글 작성, 게시글 수정, 상품 목록 조회, , 게시글 수정, 게시글 삭제
><br/>
**6. 프로젝트 소개:**
 spartamarket은 sparta 수강캠프 AI_7기 인원들이 사용할 수 있는 우리만의 중고거래 사이트로 이전에 팀프로젝트로 진행한 spartamarket 웹페이지 구현을 더 나아가 DRF로 코드를 바꾸어 구현하는 작업이다.

><br/>

**7. 프로젝트 구조**
```bash
spartamarket_DRF/
├── accounts/          # 사용자 관련 기능 (회원가입, 로그인, 프로필)
├── products/          # 상품 관련 기능 (등록, 조회, 수정, 삭제)
├── spartamarket_DRF/   # 메인 프로젝트 폴더 (설정 및 URL 설정)
└── manage.py          # Django 실행 파일
```

<br/>

## app별 소개 
**I . accounts app**
기능 [1] forms.py
회원가입
회원 정보 변경
[2] models.py class User - AbstractUser 상속 자세한 내용은 공식문서를 https://docs.djangoproject.com/en/5.1/topics/auth/customizing/ 참조

following : manytomanyfield 활용
profile_image : imagefield 활용
II. products app

기능 [1] forms.py
articleForm(form.modelform):
[2] models.py class Article - models.model 상속 자세한 내용은 공식문서를 https://docs.djangoproject.com/en/5.1/topics/db/models/ 참조

image
title
price
created_at
updated_at
author
like_users
n_hit
like_count
필수 라이브러리 Asgiref == 3.8.1 Django == 4.2 Pillow == 10.4.0 Sqlparse == 0.5.1 typing_extensions == 4.12.2 Tzdata == 2024.1
버그 및 디버그
. bug: 로그인 안해도 url주소를 치면 글 목록 등 권한 없이 넘어갈수 있는 이슈 -> 권한 필요한 함수에 login데코레이터 삽입.
bug: 조회수가 새로고침이나 찜, 팔로잉 버튼을 누를때마다 증가 -> MTM 방식으로 구현
