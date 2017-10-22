Name:           %{name}
Url:            https://github.com/openstack/%{name}
Summary:        %{name}
License:        Apache-2.0
Group:          System/Emulators/PC
Version:        %{version}
Release:        %{release}
Source0:        src.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}
AutoReq: no

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%description
%{name}

%prep
rm -rf %{buildroot}
tar -xf ../SOURCES/src.tar.gz

%build
virtualenv opt/%{name} --system-site-packages
cd src/%{name}
../../opt/%{name}/bin/pip install -r requirements.txt
../../opt/%{name}/bin/python setup.py install

cd ../../

find opt/%{name} -name '*.pyc' | xargs rm -f || echo 'no *.pyc'
sed -i "s/\/tmp\/rpmbuild\/BUILD//g" opt/%{name}/bin/*


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/var/log/%{name}
cp -r opt %{buildroot}
cp -r src/%{name}/etc %{buildroot}/etc/%{name}


%clean
rm -rf %{buildroot}


%files
/opt/%{name}
%dir %attr(0755, root, root) /var/log/%{name}
%dir %attr(0755, root, root) /etc/%{name}
%config(noreplace) %attr(-, root, root) /etc/%{name}/*


%changelog
