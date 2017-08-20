#!/bin/sh -xe

BASE_DIR=/tmp/base/
NAME=$1
VERSION=$2
RELEASE=0
TOP_DIR=/tmp/rpmbuild
SRC_DIR=$TOP_DIR/SOURCES
mkdir -p $SRC_DIR

yum install -y libtool gettext-devel libnl-devel yajl-devel device-mapper-devel libpciaccess-devel \
               xhtml1-dtds readline-devel libtasn1-devel gnutls-devel libblkid-devel augeas sanlock-devel \
               libnl3-devel avahi-devel cyrus-sasl-devel polkit-devel libacl-devel parted-devel \
               librados2-devel glusterfs-api-devel glusterfs-devel fuse-devel netcf-devel libcurl-devel \
               audit-libs-devel scrub librbd1-devel dnsmasq radvd ebtables lvm2 iscsi-initiator-utils nfs-utils numad

yum install -y /opt/yumrepo/centos/7/x86_64/vde2-*.x86_64.rpm
yum install -y /opt/yumrepo/centos/7/x86_64/qemu-2.*.x86_64.rpm

git clone https://github.com/libvirt/libvirt.git
cd libvirt
git checkout v$VERSION
./autogen.sh
make -j 8 dist
mv libvirt-$VERSION.tar.xz $SRC_DIR

rpmbuild --bb libvirt.spec \
    --define "_topdir ${TOP_DIR}" \
    --define "name ${NAME}" \
    --define "version ${VERSION}" \
    --define "release ${RELEASE}"

yum install -y /tmp/rpmbuild/RPMS/x86_64/libvirt-{devel,libs,client}-${VERSION}-*.el7.centos.x86_64.rpm
cp /tmp/rpmbuild/RPMS/x86_64/* /opt/yumrepo/centos/7/x86_64

cd
git clone https://github.com/libvirt/libvirt-python.git
cd libvirt-python
git checkout v${VERSION}
python setup.py bdist_rpm
cp dist/libvirt-python-${VERSION}-*.x86_64.rpm /opt/yumrepo/centos/7/x86_64
