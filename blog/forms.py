# ch09 1/1 추가 시작
# 장고에서는 폼도 클래스를 활용하여 정의
from django import forms

# django.forms.Form 클래스를 상속받아 폼을 작성
class PostSearchForm(forms.Form):  # forms 덕분에 검색어에 네모난 폼이 나타나는 것
    # 폼을 정의하는 방법은 테이블의 모델 클래스를 정의하는 방법과 유사함
    # CharField는 TextInput 위젯으로 표현됨
    # TextInput 위젯 앞에 label이 표시되고,
    # 변수 search_word는 입력 필드에 대한 id 역할
    search_word = forms.CharField(label='제목 검색어')  # 폼 앞에 "검색어" 라고 붙여지는 것, 이것만 붙이면 콜론과 "확인"이 자동으로 붙여짐
    search_word2 = forms.CharField(label='요약 검색어')
    search_word3 = forms.CharField(label='본문 검색어')
    search_word4 = forms.CharField(label='태그 검색어')

# ch09 1/1 추가 종료