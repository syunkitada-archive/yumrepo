#!/bin/sh -xe

BASE_DIR=/tmp/base/
NAME=$1
VERSION=$2
RELEASE=0
TOP_DIR=/tmp/rpmbuild
SRC_DIR=$TOP_DIR/SOURCES
mkdir -p $SRC_DIR

yum install -y /opt/yumrepo/centos/7/x86_64/vde2-*.x86_64.rpm
wget -P $SRC_DIR http://download.qemu-project.org/qemu-${VERSION}.tar.xz

cd $BASE_DIR
rpmbuild --bb ${VERSION}-rpm.spec \
    --define "_topdir ${TOP_DIR}" \
    --define "name ${NAME}" \
    --define "version ${VERSION}" \
    --define "release ${RELEASE}"

cp /tmp/rpmbuild/RPMS/x86_64/* /opt/yumrepo/centos/7/x86_64
