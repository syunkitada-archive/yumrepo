pike:
	sudo docker run \
		-v ${PWD}:/tmp/base -v /opt/yumrepo/centos/7/x86_64:/opt/yumrepo/centos/7/x86_64 \
		syunkitada/centos7-rpm-builder:latest /tmp/base/build.sh horizon pike 12.0.0.0b2
	cp /opt/yumrepo/centos/7/x86_64/horizon-12.* ../centos/7/x86_64/
	createrepo ../centos/7/x86_64/
