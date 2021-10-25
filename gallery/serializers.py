from rest_framework import serializers
from gallery.models import Images

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Images 
        fields=('imgId','imgName', 'imgURL', 'imgDetails')