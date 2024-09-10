# spartamarket_DRF


## 1. Project name
spartamarket_DRF
<br/> 
<br/> 
## 2.Development time 
2024.09.06 ~ 09.10
<br/> 
<br/> 
## 3. Development Environment
- Programming Language: python 3.10.14
- Web Framework: Django REST Framework(DRF)
- Database: SQLite
- IDE: VS code
- Version Control: Git, Github

<br/>

## 4.Development member
남지민(개인)
<br/>
## 5.Development function
- 회원가입
- 로그인
- 로그아웃
- 프로필 조회
- 게시글 작성
- 게시글 수정
- 상품 목록 조회
- 게시글 수정
- 게시글 삭제
<br/>
 

## 6. Project introduction
spartamarket은 sparta 수강캠프 AI_7기 인원들이 사용할 수 있는 우리만의 중고거래 사이트로 이전에 팀프로젝트로 진행한 spartamarket 웹페이지 구현을 더 나아가 DRF로 코드를 바꾸어 구현하는 작업이다.


<br/>


## 7. project structure
```bash
spartamarket_DRF/
├── accounts/          # 사용자 관련 기능 (회원가입, 로그인, 프로필)
├── products/          # 상품 관련 기능 (등록, 조회, 수정, 삭제)
├── spartamarket_DRF/   # 메인 프로젝트 폴더 (설정 및 URL 설정)
└── manage.py          # Django 실행 파일
```

<br/>

## 8. Requirements

### Django REST Framework
<br/>
🟢 기본 조건 (Basis) 🟢
  <br/>
- 프로젝트 명은 `spartamarket_DRF` 입니다.
 <br/>
- `accounts` - 계정 관련 기능
  <br/>
- `products` - 상품 관련 기능
 <br/>
 <br/>
  🟢 회원가입
   <br/>
    - Endpoint: /api/accounts
   <br/>
    - Method: POST
<br/>
    - 조건: username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력하며 성별, 자기소개 생략 가능
<br/>
    - 검증: username과 이메일은 유일해야 하며, 이메일 중복 검증(선택 기능).
  <br/>
    - 구현: 데이터 검증 후 저장.
  <br/>
  <br/>
 🟢  로그인
  <br/>
    - Endpoint: /api/accounts/login
  <br/>
    - Method**: POST
  <br/>
    - 조건: 사용자명과 비밀번호 입력 필요.
  <br/>
    - 검증: 사용자명과 비밀번호가 데이터베이스의 기록과 일치해야 함.
  <br/>
    - 구현: 성공적인 로그인 시 토큰을 발급하고, 실패 시 적절한 에러 메시지를 반환.
  <br/>
  <br/>
🟢  프로필 조회
  <br/>
    - Endpoint: /api/accounts/<str:username>
  <br/>
    - Method: GET
  <br/>
    - 조건: 로그인 상태 필요.
  <br/>
    - 검증: 로그인 한 사용자만 프로필 조회 가능
     <br/>
    - 구현: 로그인한 사용자의 정보를 JSON 형태로 반환.
  <br/>
  <br/>
 🟢   상품 등록
  <br/>
    - Endpoint: /api/products
     <br/>
    - Method: POST
     <br/>
    - 조건: 로그인 상태, 제목과 내용, 상품 이미지 입력 필요.
      <br/>
    - 구현: 새 게시글 생성 및 데이터베이스 저장.
     <br/>
      <br/>
🟢 상품 목록 조회
  <br/>
    - Endpoint: /api/products
    <br/>
    - Method: GET
    <br/>
    - 조건: 로그인 상태 불필요.
    <br/>
    - 구현: 모든 상품 목록 페이지네이션으로 반환.
     <br/>
      <br/>
 🟢 상품 수정
    <br/>
    - Endpoint: /api/products/<int:productId>
    <br/>
    - Method: PUT
    <br/>
    - 조건: 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능.
    <br/>
    - 검증: 요청자가 게시글의 작성자와 일치하는지 확인.
    <br/>
    - 구현: 입력된 정보로 기존 상품 정보를 업데이트.
     <br/>
      <br/>
 🟢  상품 삭제
      <br/>
    - Endpoint: /api/products/<int:productId>
      <br/>
    - Method:`DELETE
      <br/>
    - 조건: 로그인 상태, 삭제 권한 있는 사용자(게시글 작성자)만 가능.
      <br/>
    - 검증: 요청자가 게시글의 작성자와 일치하는지 확인.
      <br/>
    - 구현: 해당 상품을 데이터베이스에서 삭제.


## 9. Final result
**: Postman 으로 테스트**

<br/>

![image](https://github.com/user-attachments/assets/f69861b8-84a4-4894-8bb3-35f90878e8c0)
 <br/>
 **: 회원 가입 기능** 

<br/>

![image](https://github.com/user-attachments/assets/edb9a524-f867-40ae-b5a4-bdfbf2f96b1c)
 <br/>
  **: 로그인 기능** 

<br/>

![image](https://github.com/user-attachments/assets/17cc195c-c5e4-463c-9657-c57879a79ced)
 <br/>
 **: 토큰 갱신**

<br/>

![image](https://github.com/user-attachments/assets/f2c12bac-5aa1-459d-979f-706047d29a8e)
 <br/>
 **: 프로필 조회 (토큰 O)**

<br/>

![image](https://github.com/user-attachments/assets/c3c5976a-d302-4533-b7a6-b5bb0373a52c)
 <br/>
 **: 프로필 조회 (토큰 X)**

<br/>

![image](https://github.com/user-attachments/assets/e33c81c7-fd2a-4c47-a978-e0dd60793188)
 <br/>
 **: 상품 등록(로그인O)**

<br/>

![image](https://github.com/user-attachments/assets/e44a566f-53cd-4e9a-a552-a24e902cf84f)
 <br/>
 **: 상품 등록(로그인X)**

<br/>

![image](https://github.com/user-attachments/assets/ba670f02-2b09-4630-ace9-b7180c7b7fad)
 <br/>
 **: 상품 목록 조회**

<br/>

![image](https://github.com/user-attachments/assets/cb637dce-bc6a-4e32-8ed0-d32ededbca88)
 <br/>
 **: 상품 수정**

<br/>

![image](https://github.com/user-attachments/assets/b9179d82-8f49-4526-adae-43221e79198f)
![image](https://github.com/user-attachments/assets/8c390113-f460-4661-896b-abe9bcb9e25b)
 <br/>

**: 상품 삭제/ 데이터베이스에서도 완전히 삭제된 모습**
