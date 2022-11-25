FROM nginx:1.19.10-alpine
COPY ./frontend/index.html /usr/share/nginx/html
EXPOSE 5000
COPY ./frontend/nginx.conf /etc/nginx/conf.d/default.conf.template
COPY ./frontend/nginx.sh .
ENTRYPOINT ["/nginx.sh"]
CMD ["nginx", "-g", "daemon off;"]