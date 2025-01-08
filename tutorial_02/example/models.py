from django.db import models
from django_lifecycle import LifecycleModel, hook, BEFORE_CREATE
from pyhub_ai.models import Conversation


class LLMChatRoom(LifecycleModel):
    # 언어 필드 : 영어, 일본어, 중국어 등
    # 상황 필드 : 스타벅스에서 커피를 주문하는 상황, 카페에서 카페라떼를 주문하는 상황 등
    # 레벨 필드 : 초급, 중급, 고급

    conversation = models.OneToOneField(
        Conversation,
        on_delete=models.CASCADE,
    )


    # 모델 인스턴스 생성 이후에 자동 호출됩니다.
    @hook(BEFORE_CREATE)
    def on_before_create(self):
        # 본 모델에 소유자 User 필드가 있다면 지정해주세요.
        owner = None
        self.conversation = Conversation.objects.create(user=owner)
