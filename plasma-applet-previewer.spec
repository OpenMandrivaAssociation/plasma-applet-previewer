Name:           plasma-applet-previewer
Summary:        Plasma applet that allow to preview files dropped in it
Version:        0.1
Release:        %mkrel 1 
Url:            http://www.kde-look.org/content/show.php/Previewer?content=84465
License:        GPLv2+
Group:          Graphical desktop/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        84465-previewer.tar.bz2
BuildRequires:  kdebase4-workspace-devel

%description
Just a simple previewer applet which uses KPart to preview the files you drop on.

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_previewer.so
%_kde_datadir/kde4/services/plasma-applet-previewer.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n previewer 

%build
%cmake_kde4
%make

%install
cd build
make DESTDIR=%buildroot install

%clean
%{__rm} -rf "%{buildroot}"
