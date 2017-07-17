# yumrepo


## repo 設定
```
[syunkitadarepo]
name=CentOS-$releasever - syunkitadarepo
baseurl=http://syunkitada.github.io/yumrepo/centos/7/x86_64/
enabled=1
gpgcheck=0
```


## rpm-builderイメージの作成
```
$ cd centos7-rpm-builder
$ make build

# Docker Hubにログインして、イメージをPushする
$ make login
$ make push
```


## NginxでRPMを公開する
sudo apt-get -y install createrepo nginx

sudo mkdir -p /opt/nginx/yumrepo/centos/7/x86_64
sudo chown -R www-data:www-data /opt/nginx-repo
sudo mv *rpm /opt/nginx/yumrepo/centos/7/x86_64/
sudo createrepo /opt/nginx/yumrepo/centos/7/x86_64/

cat << EOS | sudo tee /etc/nginx/conf.d/yumrepo.conf
server {
    listen 8000;
    root /opt/yumrepo/centos;
    autoindex    on;
}
EOS

sudo systemctl restart nginx
```


## GitHubPagesでRPMを公開する
```
$ git clone https://github.com/syunkitada/yumrepo.git
$ cd yumrepo
$ git checkout --orphan gh-pages
$ mkdir -p centos/7/x86_64/
$ cp hoge.rpm centos/7/x86_64/
$ createrepo centos/7/x86_64/
$ git add .
$ git commit -a -m "hoge"
$ git push origin gh-pages
```
