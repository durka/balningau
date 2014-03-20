from fabric.api import lcd, local

def prepare_deployment(branch_name):
    local('python manage.py test balningau')
    local('git add -p && git commit')

