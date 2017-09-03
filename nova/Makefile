pike:
	sudo docker run \
		-v ${PWD}:/tmp/base -v /opt/yumrepo/centos/7/x86_64:/opt/yumrepo/centos/7/x86_64 \
		syunkitada/centos7-rpm-builder:latest /tmp/base/build.sh nova pike 16.0.0
	cp /opt/yumrepo/centos/7/x86_64/nova-16.* ../centos/7/x86_64/
	createrepo ../centos/7/x86_64/
