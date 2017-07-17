2.3.2:
	sudo docker run \
		-v ${PWD}:/tmp/base -v /opt/yumrepo/centos/7/x86_64:/opt/yumrepo/centos/7/x86_64 \
		syunkitada/centos7-rpm-builder:latest /tmp/base/build.sh vde2 2.3.2
	cp /opt/yumrepo/centos/7/x86_64/vde2* ../centos/7/x86_64/
	createrepo ../centos/7/x86_64/
