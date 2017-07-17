pike:
	sudo docker run \
		-v ${PWD}:/tmp/base -v /opt/yumrepo/centos/7/x86_64:/opt/yumrepo/centos/7/x86_64 \
		syunkitada/centos7-rpm-builder:latest /tmp/base/build.sh cinder pike 11.0.0.0b2
	cp /opt/yumrepo/centos/7/x86_64/cinder-11.* ../centos/7/x86_64/
	createrepo ../centos/7/x86_64/
