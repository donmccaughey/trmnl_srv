cat trmnl_srv_deploy.env > /run/trmnl_srv.env
docker image load --input trmnl_srv.tar.gz
docker image prune --force
docker stop trmnl_srv
docker rm trmnl_srv
docker run \
    --detach \
    --env-file /run/trmnl_srv.env \
    --init \
    --name 'trmnl_srv' \
    --publish 4000:80 \
    'trmnl_srv'
