docker image load --input trmnl_srv.tar.gz
docker image prune --force
docker stop trmnl_srv
docker rm trmnl_srv
docker run \
    --detach \
    --env BASE_URL='http://10.0.0.100:4000' \
    --init \
    --name 'trmnl_srv' \
    --publish 4000:80 \
    'trmnl_srv'
