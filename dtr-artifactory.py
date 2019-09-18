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

        if len(capture) > 0:

            while (re.search(group_finder, file)):

                group1 = re.search(group_finder, file).group(0)
                print "group1 " + group1
                group2 = re.search(group_finder, file).group(1)
                print "group2 " + group2
                try:
                    key, value = group2.split("/")
                except ValueError:
                    print "Failure"
                    built = re.sub('INSERT_TEXT_TO_HERE', group2, builder)
                    print "built " + built
                    finder = re.sub(re.escape('.*'), group2, whole_finder)
                    print "finder " + finder
                else:
                     print "Success"
                    print key
                    print value
                    built = re.sub('INSERT_TEXT_TO_HERE', value, builder)
                    print "built " + built
                    finder = re.sub(re.escape('.*'), group2, whole_finder)
                    print "finder " + finder

                splitOnDollarSign = finder.split("$")
                finder = "\$".join(splitOnDollarSign)
                finder += r'\n'
                built += r'\n'

                print "Replacing ->" + '\n' + finder + '\n\n' + "With ->" + '\n' + built + '\n\n'
                file = (re.sub(finder, built, file))
                outhandle = open(file_name + '.yml', "w")
                outhandle.write(file)
                outhandle.close()

        else:
            outhandle = open(file_name + '.yml', "w")
            outhandle.write(file)
            outhandle.close()

    search_and_rep(r'image: *registry.docker.org.company.com/teamx/(.*)',
        r'image: *registry.docker.org.company.com/teamx/.*',
        """image: teamx-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE""" )

    search_and_rep(r'image: *registry.docker.org.company.com/ems/(.*)',
        r'image: *registry.docker.org.company.com/ems/.*',
        """image: ems-docker-tools.artifactory.org.company.com/INSERT_TEXT_TO_HERE""" )

    search_and_rep(r'image: *registry.docker.org.company.com/(.*)',
        r'image: *registry.docker.org.company.com/.*',
        """image: ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE""" )

    search_and_rep(r'image: *\"registry.docker.org.company.com/teamx/(.*)\"',
        r'image: *\"registry.docker.org.company.com/teamx/.*\"',
        """image: \"teamx-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE\"""" )

    search_and_rep(r'image: *\"registry.docker.org.company.com/ems/(.*)\"',
        r'image: *\"registry.docker.org.company.com/ems/.*\"',
        """image: \"ems-docker-tools.artifactory.org.company.com/INSERT_TEXT_TO_HERE\"""" )

    search_and_rep(r'image: *\"registry.docker.org.company.com/(.*)\"',
        r'image: *\"registry.docker.org.company.com/.*\"',
        """image: \"ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE\"""" )

    search_and_rep(r'registry: *registry.docker.org.company.com(.*)',
        r'registry: *registry.docker.org.company.com*',
        """registry: ce-docker-dev-local.artifactory.org.company.com""" )


    search_and_rep(r'repo: *registry.docker.org.company.com/teamx/(.*)',
        r'repo: *registry.docker.org.company.com/teamx/.*',
        """repo: teamx-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE
    username: ${ARTIFACTORY_DOCKER_USERNAME}
    password: ${ARTIFACTORY_DOCKER_PASSWORD}
    registry: teamx-docker-dev-local.artifactory.org.company.com
    email: svcacct-sie-droneart@company.com""" )

    search_and_rep(r'repo: *registry.docker.org.company.com/ems/(.*)',
        r'repo: *registry.docker.org.company.com/ems/.*',
        """repo: ems-docker-tools.artifactory.org.company.com/INSERT_TEXT_TO_HERE
    username: ${ARTIFACTORY_DOCKER_USERNAME}
    password: ${ARTIFACTORY_DOCKER_PASSWORD}
    registry: ems-docker-tools.artifactory.org.company.com
    email: svcacct-sie-droneart@company.com""" )

    search_and_rep(r'repo: *registry.docker.org.company.com/(.*)',
        r'repo: *registry.docker.org.company.com/.*',
        """repo: ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE
    username: ${ARTIFACTORY_DOCKER_USERNAME}
    password: ${ARTIFACTORY_DOCKER_PASSWORD}
    registry: ce-docker-dev-local.artifactory.org.company.com
    email: svcacct-sie-droneart@company.com""" )

    search_and_rep(r'repo: *\${DOCKER_REGISTRY}/(.*)',
        r'repo: *\${DOCKER_REGISTRY}/.*',
        """repo: ce-docker-dev-local.artifactory.org.company.com/INSERT_TEXT_TO_HERE
    username: ${ARTIFACTORY_DOCKER_USERNAME}
    password: ${ARTIFACTORY_DOCKER_PASSWORD}
    registry: ce-docker-dev-local.artifactory.org.company.com
    email: svcacct-org-droneart@company.com""" )


if __name__ == "__main__":
    main()
