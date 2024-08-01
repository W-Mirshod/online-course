import os
import json
from blogs.models import Blog
from root.settings import BASE_DIR
from django.dispatch import receiver
from django.db.models.signals import pre_delete


@receiver(pre_delete, sender=Blog)
def archiving_deleted_blogs(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'deleted/blogs', f"{instance.id}_{instance.title}.json")
    print('1' * 30)
    product_info = {
        'id': instance.id,
        'slug': instance.slug,
        'title': instance.title,
        'content': instance.content,
        'created_at': str(instance.created_at),
        'updated_at': str(instance.updated_at)}

    with open(file_path, 'w') as file:
        json.dump(product_info, file, indent=4)

    print(f"Blog \"{instance.title}\" has deleted")
