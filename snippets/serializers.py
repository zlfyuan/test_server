from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES,STYLE_CHOICES
from django.contrib.auth.models import User

"""
开发我们的Web API的第一件事是为我们的Web API提供一种将代码片段实例序列化和反序列化为诸如json之类的表示形式的方式。
我们可以通过声明与Django forms非常相似的序列化器（serializers）来实现。 在snippets的目录下创建一个名为serializers.py文件，并添加以下内容。
"""
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False,allow_blank=True,max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES,default='freiedly')
#
#     def create(self, validated_data):
#         """
#         根据提供的验证过的数据创建并返回一个新的"Snippet"实例。
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         根据提供的验证过的数据更新和返回一个已经存在的"Snippet"实例
#         """
#         instance.title = validated_data.get('title',instance.title)
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
"""
使用ModelSerializers
我们的SnippetSerializer类中重复了很多包含在Snippet模型类（model）中的信息。如果能保证我们的代码整洁，那就更好了。

就像Django提供了Form类和ModelForm类一样，REST framework包括Serializer类和ModelSerializer类。

我们来看看使用ModelSerializer类重构我们的序列化类。再次打开snippets/serializers.py文件，并将SnippetSerializer类替换为以下内容。
"""


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']

    # def create(self, validated_data):
    #     return Snippet.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
