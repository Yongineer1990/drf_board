# Board

## API Documentation
[문서보기](https://documenter.getpostman.com/view/11684511/T1LMhmp3?version=latest)

## 적용 기술 (Backend)

- Python
- Django
- Django REST Framework
- ipware
- Pagination
- Bcrypt
- Mysql
- CORS headers
- Docker

## 구현 기능
### 게시물 목록
- board 페이지 진입시 게시물 목록들을 전부 가져옵니다.
- Pagination을 적용했습니다.
### 게시물 작성
- POST 요청시 body의 데이터를 기반으로 게시물을 생성합니다. body에서 사용되는 키값은 다음과 같습니다.
  - title
  - body
  - password
- Password는 단방향 암호화 과정을 거칩니다.(Bcrypt)
### 게시물 보기
- 작성한 게시물을 읽어옵니다.
### 게시물 수정
- PUT요청시 게시물을 수정합니다. body의 데이터를 기반으로 게시물을 수정합니다. body에서 사용되는 키값은 다음과 같습니다.
  - title
  - body
  - password
- Password 검증을 합니다.
 ### 게시물 삭제
- 게시물을 삭제합니다.
- Password 검증을 합니다.
### 답글 작성
- 게시물에서 POST요청으로 작성합니다.
- body의 데이터를 기반으로 답글을 작성하며 이때 사용되는 body 키값은 다음과 같습니다.
  - title
  - body
  - password
- Password는 단방향 암호화 과정을 거칩니다.(Bcrypt)
### 답글 보기
- 답글을 읽어옵니다.
### 답글 수정
- PUT요청시 게시물을 수정합니다. body의 데이터를 기반으로 게시물을 수정합니다. body에서 사용되는 키값은 다음과 같습니다.
  - title
  - body
  - password
- Password 검증을 합니다.
### 답글 삭제
- 게시물을 삭제합니다.
- Password 검증을 합니다.