# Generated by Django 4.1.1 on 2024-06-10 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visitas', '0017_remove_cita_direccion_alter_cita_fecha_visita'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='visitador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visitador_servicio', to=settings.AUTH_USER_MODEL),
        ),
    ]
