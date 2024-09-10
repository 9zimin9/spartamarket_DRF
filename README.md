# spartamarket_DRF

>
1. Project 이름 : spartamarket 
2. 프로젝트 기간 : 2024.08.19 ~ 08.28 
3. 개발언어 : Python & Django 
4. 멤버: 남지민(개인) 
5. 기능 : 회원가입, 로그인, 로그아웃, 게시글 작성, 게시글 수정, 게시글 목록, 게시글 삭제
6. 프로젝트 소개:
 spartamarket은 sparta 수강캠프 AI_7기 인원들이 사용할 수 있는 우리만의 중고거래 사이트 입니다.
단,구매 및 거래는 불가능합니다.
회원가입/로그인/프로필조회/
상품 등록/상품 목록 조회/ 상품 수정/ 상품 삭제

app별 소개 I . accounts app
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

