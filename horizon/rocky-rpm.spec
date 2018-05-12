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
mkdir -p %{buildroot}/etc/%{name}
cp -r base/etc/* %{buildroot}/etc/%{name}/
mkdir -p %{buildroot}/usr/lib/systemd/
cp -r base/system %{buildroot}/usr/lib/systemd/system
cp -r opt %{buildroot}
mkdir -p %{buildroot}/opt/%{name}/share/horizon
cp -r %{name}-%{version}/openstack_dashboard %{buildroot}/opt/%{name}/share/horizon/
cp -r %{name}-%{version}/manage.py %{buildroot}/opt/%{name}/share/horizon/

cd %{buildroot}/opt/%{name}/share/horizon/ && %{buildroot}/opt/%{name}/bin/python manage.py collectstatic --noinput
cd %{buildroot}/opt/%{name}/share/horizon/ && %{buildroot}/opt/%{name}/bin/python manage.py compress --force

cp %{buildroot}/opt/%{name}/share/horizon/openstack_dashboard/local/local_settings.py.example %{buildroot}/etc/%{name}/local_settings.py
cd %{buildroot}/opt/%{name}/share/horizon/openstack_dashboard/local/
ln -s ../../../../../../etc/horizon/local_settings.py local_settings.py

%clean
rm -rf %{buildroot}


%files
/opt/%{name}
%attr(-, root, root) /usr/lib/systemd/system/*
%dir %attr(0755, root, root) /etc/%{name}
%config(noreplace) %attr(-, root, root) /etc/%{name}/*


%changelog
