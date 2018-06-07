from celery.task import task

@task
def say_hello(name):
    content = "hello {name},welcome django".format(name=name)
    print(content)
    return content

@task
def loop_task():
    content = "this is loop task"
    print(content)
    return content