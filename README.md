# spartamarket_DRF

>
## 1. Project name
spartamarket_DRF
><br/> 
## 2.Development time 
2024.09.06 ~ 09.10
 
## 3. Development Environment
- Programming Language: python 3.10.14
- Web Framework: Django REST Framework(DRF)
- Database: SQLite
- IDE: VS code
- Version Control: Git, Github

><br/>

## 4.Development member
남지민(개인)
><br/>
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
><br/>
## 6. Project introduction
spartamarket은 sparta 수강캠프 AI_7기 인원들이 사용할 수 있는 우리만의 중고거래 사이트로
><br/>
이전에 팀프로젝트로 진행한 spartamarket 웹페이지 구현을 더 나아가 DRF로 코드를 바꾸어 구현하는 작업이다.

><br/>


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
### DRF!! (Django REST Framework)
<br/>
  **기본 조건 (Basis)**
    -  프로젝트 명은 `spartamarket_DRF` 입니다.
    - 아래의 앱은 필수로 포함하며, 이외에는 자유롭게 구현해 주세요.
        - `accounts` - 계정 관련 기능
        - `products` - 상품 관련 기능
<br/>
- **회원가입**
    - **Endpoint**: **`/api/accounts`**
    - **Method**: **`POST`**
    - **조건**: username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력하며 성별, 자기소개 생략 가능
    - **검증**: username과 이메일은 유일해야 하며, 이메일 중복 검증(선택 기능).
    - **구현**: 데이터 검증 후 저장.
    - <br/>
- **로그인**
    - **Endpoint**: **`/api/accounts/login`**
    - **Method**: **`POST`**
    - **조건**: 사용자명과 비밀번호 입력 필요.
    - **검증**: 사용자명과 비밀번호가 데이터베이스의 기록과 일치해야 함.
    - **구현**: 성공적인 로그인 시 토큰을 발급하고, 실패 시 적절한 에러 메시지를 반환.
    - <br/>
- **프로필 조회**
    - **Endpoint**: **`/api/accounts/<str:username>`**
    - **Method**: **`GET`**
    - **조건**: 로그인 상태 필요.
    - **검증**: 로그인 한 사용자만 프로필 조회 가능
    - **구현**: 로그인한 사용자의 정보를 JSON 형태로 반환.
 <br/>
  - **상품 등록**
    - **Endpoint**: **`/api/products`**
    - **Method**: **`POST`**
    - **조건**: 로그인 상태, 제목과 내용, 상품 이미지 입력 필요.
    - **구현**: 새 게시글 생성 및 데이터베이스 저장.
    - <br/>
- **상품 목록 조회**
    - **Endpoint**: **`/api/products`**
    - **Method**: **`GET`**
    - **조건**: 로그인 상태 불필요.
    - **구현**: 모든 상품 목록 페이지네이션으로 반환.
    - <br/>
- **상품 수정**
    - **Endpoint**: **`/api/products/<int:productId>`**
    - **Method**: **`PUT`**
    - **조건**: 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능.
    - **검증**: 요청자가 게시글의 작성자와 일치하는지 확인.
    - **구현**: 입력된 정보로 기존 상품 정보를 업데이트.
    - <br/>
- **상품 삭제**
    - **Endpoint**: **`/api/products/<int:productId>`**
    - **Method**: **`DELETE`**
    - **조건**: 로그인 상태, 삭제 권한 있는 사용자(게시글 작성자)만 가능.
    - **검증**: 요청자가 게시글의 작성자와 일치하는지 확인.
    - **구현**: 해당 상품을 데이터베이스에서 삭제.



