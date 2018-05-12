pike:
	sudo docker run \
	-v ${PWD}:/tmp/base -v /opt/yumrepo/centos/7/x86_64:/opt/yumrepo/centos/7/x86_64 \
	syunkitada/centos7-rpm-builder:latest /tmp/base/build.sh keystone pike 12.0.0
	cp /opt/yumrepo/centos/7/x86_64/keystone-12* ../centos/7/x86_64/
	createrepo ../centos/7/x86_64/


rocky:
	sudo docker run \
	-v ${PWD}:/tmp/base -v /opt/yumrepo/centos/7/x86_64:/opt/yumrepo/centos/7/x86_64 \
	syunkitada/centos7-rpm-builder:latest /tmp/base/build.sh keystone rocky 14.0.0.0b1
	cp /opt/yumrepo/centos/7/x86_64/keystone-14* ../centos/7/x86_64/
	createrepo ../centos/7/x86_64/
