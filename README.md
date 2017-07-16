# yumrepo


## 初期設定
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


## repo 設定
```
[syunkitadarepo]
name=CentOS-$releasever - syunkitadarepo
baseurl=http://syunkitada.github.io/yumrepo/centos/7/x86_64/
enabled=1
gpgcheck=0
```
