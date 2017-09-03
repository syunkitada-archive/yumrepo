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

%build
virtualenv opt/%{name} --system-site-packages
opt/%{name}/bin/pip install -r base/%{version_name}-requirements.txt

find opt/%{name} -name '*.pyc' | xargs rm -f || echo 'no *.pyc'
sed -i "s/\/tmp\/rpmbuild\/BUILD//g" opt/%{name}/bin/*

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -r opt %{buildroot}

mkdir -p %{buildroot}/usr/bin/
cd %{buildroot}/usr/bin/
ln -s ../../opt/%{name}/bin/openstack openstack
ln -s ../../opt/%{name}/bin/uwsgi uwsgi


%clean
rm -rf %{buildroot}


%files
/opt/%{name}
/usr/bin
%attr(0755, root, root) /usr/bin/*


%changelog
