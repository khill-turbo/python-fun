#!/usr/bin/env python3

import mmap
import re
import json

files = [
    '.drone'
    ]

# For help on building regular expressions:  https://docs.python.org/2/library/re.html

def main():
    for f in files:
        convert(f)

def convert(file_name):
    # Read in BiGG namespace file

    print ""

    def search_and_rep(group_finder, whole_finder, builder):
        file_handle = open(file_name + '.yml', "r")
        file = file_handle.read()
        #print 'file_name: ' + file_name

        capture = re.findall(group_finder, file)
        #print "capture " + capture
        if len(capture) > 2:
            group0 = re.search(group_finder, file).group(0)
            print "group0 " + group0
            group1 = re.search(group_finder, file).group(1)
            print "group1 " + group1
            group2 = re.search(group_finder, file).group(2)
            print "group2 " + group2
            built = re.sub('INSERT_TEXT_TO_HERE', group2, builder)
            print "Replacing ->" + '\n' + group1 + '\n\n' + "With ->" + '\n' + built + '\n\n'
            file = (re.sub(whole_finder, built, file))
            outhandle = open(file_name + '.yml', "w")
            outhandle.write(file)
            outhandle.close()
        elif len(capture) > 1:
            group1 = re.search(group_finder, file).group(0)
            print "group1 " + group1
            group2 = re.search(group_finder, file).group(1)
            print "group2 " + group2
            built = re.sub('INSERT_TEXT_TO_HERE', group2, builder)
            print "Replacing ->" + '\n' + group1 + '\n\n' + "With ->" + '\n' + built + '\n\n'
            file = (re.sub(whole_finder, built, file))
            outhandle = open(file_name + '.yml', "w")
            outhandle.write(file)
            outhandle.close()
        elif len(capture) > 0:
            group1 = re.search(group_finder, file).group(0)
            print "group1 " + group1
            group2 = re.search(group_finder, file).group(1)
            print "group2 " + group2
            built = re.sub('INSERT_TEXT_TO_HERE', group2, builder)
            print "Replacing ->" + '\n' + group1 + '\n\n' + "With ->" + '\n' + built + '\n\n'
            file = (re.sub(whole_finder, built, file))
            outhandle = open(file_name + '.yml', "w")
            outhandle.write(file)
            outhandle.close()
        else:
            outhandle = open(file_name + '.yml', "w")
            outhandle.write(file)
            outhandle.close()



    search_and_rep(r'docker_image: *\${DOCKER_REGISTRY}/clientops/(.*)\${DRONE_BUILD_NUMBER}',
        r'docker_image: *\${DOCKER_REGISTRY}/clientops/.*\${DRONE_BUILD_NUMBER}',
        """docker_image: ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE${DRONE_BUILD_NUMBER}""" )

    search_and_rep(r'docker_image: *\${DOCKER_REGISTRY}/clientops/(.*)\${DRONE_PULL_REQUEST}',
        r'docker_image: *\${DOCKER_REGISTRY}/clientops/.*\${DRONE_PULL_REQUEST}',
        """docker_image: ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE${DRONE_PULL_REQUEST}""" )

    search_and_rep(r'docker_image: *\${DOCKER_REGISTRY}/clientops/(.*)\${DRONE_TAG}',
        r'docker_image: *\${DOCKER_REGISTRY}/clientops/.*\${DRONE_TAG}',
        """docker_image: ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE${DRONE_TAG}""" )

    search_and_rep(r'docker_image: *\"\${DOCKER_REGISTRY}/clientops/(.*)\${DRONE_TAG##v}\"',
        r'docker_image: *\"\${DOCKER_REGISTRY}/clientops/.*\${DRONE_TAG##v}\"',
        """docker_image: \"ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE${DRONE_TAG##v}\"""" )



    search_and_rep(r'docker_image: *registry.docker.org.company.com/clientops/(.*)\${DRONE_BUILD_NUMBER}',
        r'docker_image: *registry.docker.org.company.com/clientops/.*\${DRONE_BUILD_NUMBER}',
        'docker_image: ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE${DRONE_BUILD_NUMBER}' )

    search_and_rep(r'docker_image: *registry.docker.org.company.com/clientops/(.*)\${DRONE_PULL_REQUEST}',
        r'docker_image: *registry.docker.org.company.com/clientops/.*\${DRONE_PULL_REQUEST}',
        """docker_image: ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE${DRONE_PULL_REQUEST}""" )

    search_and_rep(r'docker_image: *registry.docker.org.company.com/clientops/(.*)\${DRONE_TAG}',
        r'docker_image: *registry.docker.org.company.com/clientops/.*\${DRONE_TAG}',
        """docker_image: ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE${DRONE_TAG}""" )

    search_and_rep(r'docker_image: *\${DOCKER_REGISTRY}/clientops/(.*)\${DRONE_TAG##v}',
        r'docker_image: *\${DOCKER_REGISTRY}/clientops/.*\${DRONE_TAG##v}',
        """docker_image: ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE${DRONE_TAG##v}""" )


if __name__ == "__main__":
    main()

