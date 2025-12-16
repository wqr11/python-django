from time import time
from django.db import models
from .utils.snowflake import snowflake_id

tag_snowflake_factory = snowflake_id(0)
todo_snowflake_factory = snowflake_id(1)

class User(models.Model):
    tg_id = models.BigIntegerField(primary_key=True)

    # For logging purposes
    def __str__(self):
        return f'<User_tg: {self.tg_id}>'

class Tag(models.Model):
    id = models.BigIntegerField(primary_key=True, default=tag_snowflake_factory)
    content = models.CharField(max_length=128)

    # For logging purposes
    def __str__(self):
        return f'<Tag: {content}>'

class Todo(models.Model):
    id = models.BigIntegerField(primary_key=True, default=todo_snowflake_factory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    content = models.TextField(default='')
    execution_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # For logging purposes
    def __str__(self):
        return f'<Todo: {id}>'