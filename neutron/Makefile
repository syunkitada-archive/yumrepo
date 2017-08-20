pike:
	sudo docker run \
		-v ${PWD}:/tmp/base -v /opt/yumrepo/centos/7/x86_64:/opt/yumrepo/centos/7/x86_64 \
		syunkitada/centos7-rpm-builder:latest /tmp/base/build.sh neutron pike 11.0.0.0rc1
	cp /opt/yumrepo/centos/7/x86_64/neutron-11.* ../centos/7/x86_64/
	createrepo ../centos/7/x86_64/
