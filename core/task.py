from huey.contrib.djhuey import task

@task()
def task_comment_notification():
    print('create user notification')
    pass

