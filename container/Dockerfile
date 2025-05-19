FROM alpine:latest

EXPOSE 80

RUN apk add --no-cache \
    curl \
    nginx \
    python3 \
    py3-pillow \
    py3-requests \
    tzdata


# nginx
RUN rm -rf \
        /etc/nginx/http.d/ \
        /etc/nginx/modules/ \
        /var/lib/nginx/html/
RUN rm -f \
        /etc/nginx/fastcgi.conf \
        /etc/nginx/fastcgi_params \
        /etc/nginx/scgi_params \
        /etc/nginx/uwsgi_params

RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log
RUN ln -sf /srv/www /var/lib/nginx/html

RUN mkdir -p /var/cache/nginx
RUN chown -R nginx:nginx /var/cache/nginx

COPY container/etc/nginx/nginx.conf /etc/nginx/nginx.conf
COPY --chown=nginx:www-data container/srv/www /srv/www


# cron jobs
COPY container/etc/crontabs /etc/crontabs


# control scripts
COPY container/usr/local/sbin /usr/local/sbin


# ash profile
COPY container/etc/profile.d /etc/profile.d
RUN ln -sf /etc/profile.d/color_prompt.sh.disabled \
        /etc/profile.d/color_prompt.sh


# python modules
RUN mkdir -p /usr/lib
COPY src/gather /usr/lib/gather
COPY src/render /usr/lib/render
COPY src/serve /usr/lib/serve


WORKDIR /root
ENTRYPOINT ["/usr/local/sbin/trmnl_srv"]
