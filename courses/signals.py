import os
import json
from courses.models import Course
from root.settings import BASE_DIR
from django.dispatch import receiver
from django.db.models.signals import pre_delete


@receiver(pre_delete, sender=Course)
def archiving_deleted_products(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'deleted/courses', f"{instance.id}_{instance.name}.json")
    print('1'*30)
    product_info = {
        'id': instance.id,
        'slug': instance.slug,
        'title': instance.title,
        'number_of_students': instance.number_of_students,
        'price': instance.price,
        'duration': instance.duration,
        'teachers': instance.teachers,
        'video': instance.video,
        'category': instance.category}

    with open(file_path, 'w') as file:
        json.dump(product_info, file, indent=4)

    print(f"Product \"{instance.name}\" has deleted")
