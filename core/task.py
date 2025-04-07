from huey.contrib.djhuey import task

from apps.blog.models import Post

@task()
def task_update_count_view(post_id: int):
    try:
        post = Post.objects.get(id = post_id)
        post.views += 1
        post.save()
    except Post.DoesNotExist:
        print(f'post id {post_id} does not exist')
    except :
        print('something went wrong')

