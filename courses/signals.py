import os
import json
from courses.models import Course, Comment
from root.settings import BASE_DIR
from django.dispatch import receiver
from django.db.models.signals import pre_delete


@receiver(pre_delete, sender=Course)
def archiving_deleted_courses(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'deleted/courses', f"{instance.id}_{instance.title}.json")
    print('1' * 30)
    product_info = {
        'id': instance.id,
        'slug': instance.slug,
        'title': instance.title,
        'number_of_students': instance.number_of_students,
        'price': instance.price,
        'duration': instance.duration,
        'created_at': instance.created_at,
        'updated_at': instance.updated_at}

    with open(file_path, 'w') as file:
        json.dump(product_info, file, indent=4)

    print(f"Product \"{instance.title}\" has deleted")


@receiver(pre_delete, sender=Comment)
def archiving_deleted_comments(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'deleted/comments', f"{instance.id}_{instance.name}.json")
    print('1' * 30)
    product_info = {
        'id': instance.id,
        'name': instance.name,
        'email': instance.email,
        'comment': instance.comment,
        'is_published': instance.is_published,
        'rating': instance.rating,
        'created_at': str(instance.created_at),
        'updated_at': str(instance.updated_at)}

    with open(file_path, 'w') as file:
        json.dump(product_info, file, indent=4)

    print(f"Course \"{instance.name}\" has deleted")
