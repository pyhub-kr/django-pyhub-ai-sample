# 튜토리얼 #1: 30분 만에 LLM 에이전트 만들기

(유튜브 영상) [파이썬/장고로 30분 만에 데이터 분석 에이전트 챗봇 만들기](https://www.youtube.com/watch?v=10Fp78n3jSw)

## 구동방법

1. `tutorial_01` 폴더를 다운받습니다.
2. 가상환경을 생성/활성화하고 라이브러리를 설치합니다.

```
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
venv\Scripts\activate  # windows
source venv/bin/activate  # mac/linux

# 패키지 설치
python -m pip install -r requirements.txt
```

3. `tutorial_01` 디렉토리에 `.env` 파일을 생성하고 OpenAI API Key 값으로 `OPENAI_API_KEY` 환경변수를 설정합니다. OpenAI API Key는 [OpenAI 대시보드의 API Key](https://platform.openai.com/api-keys)페이지 "Create new secret key" 메뉴를 통해 발급받으실 수 있습니다. 이때 API 권한 (Permission)에 제한 (Restricted)을 거실 경우, 반드시 "Model capabilities" 권한은 `Write`로 지정해주셔야만 합니다.

```.env
OPENAI_API_KEY=...
```

4. 개발서버 구동

```sh
python manage.py runserver
```

5. 브라우저로 접속 확인

[https://127.0.0.1:8000/example/chat/language-tutor/](https://127.0.0.1:8000/example/chat/language-tutor/) 접속하여, 챗봇 테스트

## 문의

+ 유튜브 채널 : [파이썬 사랑방 TV](https://www.youtube.com/@pyhub-kr)
+ 문의 : help@pyhub.kr
