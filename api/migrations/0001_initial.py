# Generated by Django 2.1.7 on 2019-03-12 15:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('content', models.TextField(max_length=2048, verbose_name='内容')),
                ('pubTime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='发布时间')),
                ('modifyTime', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('url', models.URLField(blank=True, null=True, verbose_name='路径')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('paramName', models.CharField(max_length=50, unique=True, verbose_name='参数名')),
                ('group', models.CharField(blank=True, max_length=50, verbose_name='组')),
                ('value', models.CharField(max_length=1024, verbose_name='值')),
                ('enable', models.BooleanField(default=True, verbose_name='有效')),
                ('readonly', models.BooleanField(default=False, verbose_name='只读')),
            ],
            options={
                'verbose_name': '参数',
                'verbose_name_plural': '设置',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='编号')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='昵称')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('email', models.CharField(max_length=200, unique=True, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=200, unique=True, verbose_name='电话')),
                ('sex', models.CharField(choices=[('0', '男'), ('1', '女'), ('2', '保密')], max_length=10, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('level', models.IntegerField(default=0, editable=False, verbose_name='等级')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='api.User', verbose_name='作者'),
        ),
    ]
