# Generated by Django 4.0.3 on 2022-04-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_role_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='roles',
            field=models.ManyToManyField(blank=True, null=True, to='user.role', verbose_name='角色'),
        ),
    ]