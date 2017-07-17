#!/bin/sh -xe

BASE_DIR=/tmp/base/
NAME=$1
VERSION=$2
RELEASE=0
TOP_DIR=/tmp/rpmbuild
SRC_DIR=$TOP_DIR/SOURCES
mkdir -p $SRC_DIR

cd $BASE_DIR/../
wget -P $SRC_DIR http://downloads.sourceforge.net/project/vde/vde2/${VERSION}/vde2-${VERSION}.tar.gz

rpmbuild --bb base/${VERSION}-rpm.spec \
    --define "_topdir ${TOP_DIR}" \
    --define "name ${NAME}" \
    --define "version ${VERSION}" \
    --define "release ${RELEASE}"

cp /tmp/rpmbuild/RPMS/x86_64/* /opt/yumrepo/centos/7/x86_64
