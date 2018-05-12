pike:
	sudo docker run \
		-v ${PWD}:/tmp/base -v /opt/yumrepo/centos/7/x86_64:/opt/yumrepo/centos/7/x86_64 \
		syunkitada/centos7-rpm-builder:latest /tmp/base/build.sh glance pike 15.0.0
	cp /opt/yumrepo/centos/7/x86_64/glance-15.* ../centos/7/x86_64/
	createrepo ../centos/7/x86_64/


rocky:
	sudo docker run \
		-v ${PWD}:/tmp/base -v /opt/yumrepo/centos/7/x86_64:/opt/yumrepo/centos/7/x86_64 \
		syunkitada/centos7-rpm-builder:latest /tmp/base/build.sh glance rocky 17.0.0.0b1
	cp /opt/yumrepo/centos/7/x86_64/glance-17.* ../centos/7/x86_64/
	createrepo ../centos/7/x86_64/
