import os
import json
from root.settings import BASE_DIR
from teachers.models import Teacher
from django.dispatch import receiver

from django.db.models.signals import pre_delete


@receiver(pre_delete, sender=Teacher)
def archiving_deleted_teachers(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'deleted/teachers', f"{instance.id}_{instance.full_name}.json")
    print('1' * 30)
    product_info = {
        'id': instance.id,
        'slug': instance.slug,
        'full_name': instance.full_name,
        'description': instance.description,
        'level': instance.level,
        'twitter_link': instance.twitter_link,
        'facebook_link': instance.facebook_link,
        'linkedin_link': instance.linkedin_link,
        'created_at': str(instance.created_at),
        'updated_at': str(instance.updated_at)}

    with open(file_path, 'w') as file:
        json.dump(product_info, file, indent=4)

    print(f"Teacher \"{instance.full_name}\" has deleted")
