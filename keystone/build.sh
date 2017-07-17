#!/bin/sh -xe

BASE_DIR=/tmp/base/
NAME=keystone
VERSION=$1
RELEASE=`date +"%Y%m%d"`
TOP_DIR=/tmp/rpmbuild
SRC_DIR=$TOP_DIR/SOURCES
mkdir -p $SRC_DIR

cd $BASE_DIR/../
tar -cf $SRC_DIR/base.tar.gz base

rpmbuild --bb base/rpm.spec \
    --define "_topdir ${TOP_DIR}" \
    --define "name ${NAME}" \
    --define "version ${VERSION}" \
    --define "release ${RELEASE}"

cp /tmp/rpmbuild/RPMS/x86_64/* /opt/yumrepo/centos/7/x86_64
