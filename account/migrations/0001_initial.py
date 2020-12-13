# Generated by Django 3.1.4 on 2020-12-13 17:40

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('is_admin', models.IntegerField(blank=True, null=True)),
                ('is_superuser', models.IntegerField(blank=True, null=True)),
                ('date_joined', models.DateField(blank=True, null=True)),
                ('last_login', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': ('user',),
                'verbose_name_plural': 'users',
                'db_table': 'user',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
