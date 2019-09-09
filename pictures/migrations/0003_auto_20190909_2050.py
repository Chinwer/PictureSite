# Generated by Django 2.2.4 on 2019-09-09 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_auto_20190907_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=200)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pictures.Post')),
            ],
        ),
    ]