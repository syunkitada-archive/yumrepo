#!/bin/sh -xe

BASE_DIR=/tmp/base/
SRC_DIR=/tmp/src/
NAME=openstack-manager
RELEASE=`date +"%Y%m%d"`
TOP_DIR=/tmp/rpmbuild
SOURCES_DIR=$TOP_DIR/SOURCES
mkdir -p $SRC_DIR
mkdir -p $SOURCES_DIR

cd /tmp
git clone https://github.com/syunkitada/openstack-manager.git
cd openstack-manager
VERSION=`python setup.py --version | tail -n 1`
cd ../
cp -r openstack-manager $SRC_DIR
cp -r $BASE_DIR $SRC_DIR

cd $SRC_DIR/../
tar -cf $SOURCES_DIR/src.tar.gz src

rpmbuild --bb base/rpm.spec \
    --define "_topdir ${TOP_DIR}" \
    --define "name ${NAME}" \
    --define "version ${VERSION}" \
    --define "release ${RELEASE}"

cp /tmp/rpmbuild/RPMS/x86_64/* /opt/yumrepo/centos/7/x86_64
