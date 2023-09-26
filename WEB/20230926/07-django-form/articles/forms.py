

# class ArticleForm(forms.Form):
#   # 사용자로부터 제목과 내용을 받고 있음
#   title = forms.CharField(max_length=10)
#   content = forms.CharField(widget=forms.Textarea) 
#   # TextField가 없음 / form필드의 CharField의 max length는 필수 인자가 아니다


from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
  title = forms.CharField(
    label='제목',
    widget=forms.TextInput(
     # attribute
      attrs={
        'class':'my-title',
      }
 
    ),
  )


  # model 등록만 하면 끝
  class Meta:
    # Meta : 메타 데이터 (어떠한 데이터에 대한 데이터) 
    # AritcleForm에 대한 데이터
    model = Article
    fields = '__all__'
    # Article 모델에서 정의한 field 중 전체 field를 불러온다


