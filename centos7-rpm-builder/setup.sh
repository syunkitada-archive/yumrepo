yum -y update
yum -y install curl wget git gcc gcc-c++ rpm-build createrepo \
               libxml2-devel libxslt-devel libffi-devel \
               openssl-devel libvirt-devel liberasurecode-devel \
               pulseaudio-libs-devel systemtap-sdt-devel bluez-libs-devel \
               libusb1-devel vte3-devel librdmacm-devel \
               iasl libuuid-devel SDL-devel libaio-devel usbredir-devel \
               zlib zlib-devel ncurses-devel numactl-devel numactl-libs \
               libgudev1 libcap-ng-devel jemalloc-devel libiscsi-devel libpcap-devel libcap-devel


yum -y install python-setuptools python-setuptools-devel python-devel
easy_install pip
pip install virtualenv
