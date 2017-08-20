Name:           %{name}
Url:            https://github.com/openstack/%{name}
Summary:        %{name}
License:        Apache-2.0
Group:          System/Emulators/PC
Version:        %{version}
Release:        %{release}
Source0:        base.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}
AutoReq: no

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%description
%{name}

%prep
rm -rf %{buildroot}
tar -xf ../SOURCES/base.tar.gz
wget https://github.com/openstack/%{name}/archive/%{version}.tar.gz
tar -xf %{version}.tar.gz

%build
virtualenv opt/%{name} --system-site-packages
opt/%{name}/bin/pip install -r base/%{version_name}-requirements.txt

cd %{name}-%{version}
git config --global user.name "nobody"
git config --global user.email "nobody@example.com"
git init
git add .
git commit -m %{version}
git tag -a %{version} -m %{version}
../opt/%{name}/bin/python setup.py install
cd ../

find opt/%{name} -name '*.pyc' | xargs rm -f || echo 'no *.pyc'
sed -i "s/\/tmp\/rpmbuild\/BUILD//g" opt/%{name}/bin/*

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/var/log/%{name}
mkdir -p %{buildroot}/usr/lib/systemd/
mkdir -p %{buildroot}/var/lib/nova/instances
cp -r opt %{buildroot}
cp -r %{name}-%{version}/etc/nova %{buildroot}/etc/%{name}
cp -r base/system %{buildroot}/usr/lib/systemd/system

%clean
rm -rf %{buildroot}

%files
/opt/%{name}
%attr(-, root, root) /usr/lib/systemd/system/*
%dir %attr(0755, root, root) /var/log/%{name}
%dir %attr(0755, root, root) /var/lib/%{name}
%dir %attr(0755, root, root) /var/lib/%{name}/instances
%dir %attr(0755, root, root) /etc/%{name}
%dir %attr(0755, root, root) /etc/%{name}/rootwrap.d
%config(noreplace) %attr(-, root, root) /etc/%{name}/*
%config(noreplace) %attr(-, root, root) /etc/%{name}/rootwrap.d/*

%changelog
