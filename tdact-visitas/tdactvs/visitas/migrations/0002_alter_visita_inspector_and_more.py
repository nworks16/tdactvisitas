# Generated by Django 4.1.1 on 2024-03-05 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_avatar_usuario_foto'),
        ('visitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='inspector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitas_inspeccionadas', to='core.usuario'),
        ),
        migrations.AlterField(
            model_name='visita',
            name='responsable_visita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitas_asignadas', to='core.usuario'),
        ),
    ]