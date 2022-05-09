# Generated by Django 3.2.7 on 2022-01-23 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=100)),
                ('elocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='elocation',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='ename',
        ),
        migrations.AddField(
            model_name='employee',
            name='edept',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='testapp.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='erole',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='testapp.role'),
            preserve_default=False,
        ),
    ]