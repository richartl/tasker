# -*- coding: utf-8 -*-
from fabric.api import task, local
from fabric import state
"""
This task required:
    Docker
"""
@task
def start():
    """
    Init the project
    """
    print "Start containers.."
    local( 'sudo docker-compose up -d' )

@task
def stop():
    """
    Stop the containers
    """
    print "Stop the conainers..."
    local( 'sudo docker-compose stop' )

@task
def remove():
    """
    Remove containers
    """
    print "Remove containers .."
    local( "sudo docker-compose rm" )

@task
def analyze():
    """
    Start the test with codeclimate
    """
    state.output['user'] = True
    print "Start the codeclimate test.."
    local("sudo docker run \
          --interactive --tty --rm \
          --env CODE_PATH=\"$PWD/src/\" \
          --volume \"$PWD/src\":/code \
          --volume /var/run/docker.sock:/var/run/docker.sock \
          --volume /tmp/cc:/tmp/cc \
          codeclimate/codeclimate analyze")

@task
def bundle_install():
    """
    Run bundle install within taskerRails container|
    """
    local( 'sudo docker exec -it taskerRails bundle install' )

@task
def rake( action ):
    """
    Run rake action within taskerRails container
    """
    if( not action ):
        print "The action is required param.."
    else:
        print "Run " + action
        local ( "sudo docker exec -it taskerRails rake " + action )

@task
def db_create():
    """
    Run db:create within taskerRails container
    """
    print "Run db create ..."
    local( "sudo docker exec -it taskerRails rake db:create" )

@task
def migrate():
    """
    Run db:migrate within taskerRails container
    """
    print "Run db migrate ..."
    local( "sudo docker exec -it taskerRails rake db:migrate" )


