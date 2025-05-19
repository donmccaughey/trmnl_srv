# Docs

37.77257° N, 122.39330° W


## Weather

- [National Weather Service API](https://www.weather.gov/documentation/services-web-api)
- [API FAQs](https://weather-gov.github.io/api/)
- [List of National Weather Service Weather Forecast Offices](https://en.wikipedia.org/wiki/Template%3AList_of_National_Weather_Service_Weather_Forecast_Offices)


## Synology Docker Info

- [Set up SSH publickey authentication](https://kb.synology.com/en-my/DSM/tutorial/How_to_log_in_to_DSM_with_key_pairs_as_admin_or_root_permission_via_SSH_on_computers)

Be sure to follow "Step D" and append your public key to `~/.ssh/authorized_keys`

- [Manage docker without needing sudo](https://davejansen.com/manage-docker-without-needing-sudo-on-your-synology-nas/)


## Getting a Docker Container Image Deployed on Synology

    # on your dev machine

    $ docker image save <image> | gzip > <image>.tar.gz
    $ rsync --archive <image>.tar.gz <user>@<synology ip>:~
    $ ssh <user>@<synology ip>
    
    # on the synology box
    
    $ docker image load --input <image>.tar.gz
    $ docker image prune --force
    $ docker run \
            --detach \
            --env BASE_URL='http://10.0.0.100:4000' \
            --init \
            --name <container> \
            --publish 4000:80 \
            <image>
    
    # container runs ...
    
    $ docker stop <container>
    $ docker rm <container>


## Alpine Linux Cheatsheet

See running services:

    sudo rc-status

Start the trmnl_srv service:

    sudo rc-service trmnl_srv start

Stop the trmnl_srv service:

    sudo rc-service trmnl_srv stop


## Old Alpine Deploy Target

    RSYNC_FLAGS ?= \
		--compress \
		--delete \
		--exclude '__pycache__' \
		--exclude '*_test.py' \
		--quiet \
		--recursive \
		--rsh ssh \
		--times

    $(TMP)/deploy.stamp.txt : \
            $(TMP)/pytest.stamp.txt \
            $(alpine_files) \
            $(src_files)
        rsync \
            $(RSYNC_FLAGS) \
            src/ \
            donmcc@10.1.1.1:~/trmnl_srv/
        rsync \
            $(RSYNC_FLAGS) \
            alpine/ \
            donmcc@10.1.1.1:~/trmnl_setup/
        date > $@
