# これは何
実際に私のサーバーで利用している、docker製アプリケーションをデプロイする際に利用しているスクリプトです。

`(git pull && build -> ) stop -> rm -> start` までを行います。

## how to use

Tips: `APP_NAME`は省略でき、省略した際は代わりに`CONTAINER_NAME`を利用します。

### DockerHub等にすでにアップロードしているイメージをrunする場合

```
CONTAINER_NAME=jenkins APP_NAME=jenkins:latest ./deploy.py -e VIRTUAL_HOST=jenkins.example.com
```

### Dockerfileからbuildしてrunする場合

```
APP_DIR=~/apps/my-app APP_NAME=my-app CONTAINER_NAME=my-app ./deploy.py -e VIRTUAL_HOST=myapp.example.com
```