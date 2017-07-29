pike:
	sudo docker run \
		-v ${PWD}:/tmp/base -v /opt/yumrepo/centos/7/x86_64:/opt/yumrepo/centos/7/x86_64 \
		syunkitada/centos7-rpm-builder:latest /tmp/base/build.sh openstack-tools pike 0.0.1
	cp /opt/yumrepo/centos/7/x86_64/openstack-tools-* ../centos/7/x86_64/
	createrepo ../centos/7/x86_64/
