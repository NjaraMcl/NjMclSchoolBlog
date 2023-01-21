from django import forms
from .models import Post


class addPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "author",
            "content",
            "status",
        ]
        widgets = {
            "author": forms.TextInput(attrs={"type": "hidden"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({"class": ("form-control")})
        self.fields["author"].widget.attrs.update(
            {
                "class": ("form-control"),
                "id": ("author"),
                "value": (""),
            }
        )


class editPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "status",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({"class": ("form-control")})
