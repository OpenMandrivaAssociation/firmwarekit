Summary:	Linux Firmware Tester
Name:   	firmwarekit
Version:	r2
Release:	%mkrel 1
License:	LGPL
Group:  	System/Configuration/Hardware
URL:    	http://www.linuxfirmwarekit.org/
Source: 	http://www.linuxfirmwarekit.org/download/firmwarekit-%version.tar.gz
Patch0:  	firmwarekit-r2-distro.patch
Patch1: 	firmwarekit-r2-mandriva_lspci.patch
Patch2: 	firmwarekit-r2-dmesg.patch
BuildRoot:	%_tmppath/%name-buildroot

BuildRequires:	gccmakedep
BuildRequires:	newt-devel
Requires:   	iasl
Requires:   	pmtools

%description
The Linux-ready Firmware Developer Kit is a tool to test how well Linux works
together with the firmware (BIOS or EFI) of your machine. 

%prep
%setup -q -n linuxfirmwarekit
%patch0 -p1 -b .distro
%patch1 -p1 -b .mandriva_lspci
%patch2 -p1 -b .dmesg

%build
%make libdir=%_libdir

%install
rm -rf %buildroot
make DESTDIR=%buildroot libdir=%_libdir install

touch %buildroot/%_var/log/firmwarekit/{acpi.dump,DSDT.aml,DSDT.dat,DSDT.dsl}
touch %buildroot/%_var/log/firmwarekit/{resources,results}.xml
touch %buildroot/%_var/log/firmwarekit/results.txt

%clean
rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%_bindir/announce_resource
%_bindir/finish_test
%_bindir/report_result
%_bindir/report_testrun_progress
%_bindir/start_test
%_sbindir/biostest
%_libdir/firmwarekit/plugins/SUN.exe
%_libdir/firmwarekit/plugins/acpicompile.exe
%_libdir/firmwarekit/plugins/acpiinfo.so
%_libdir/firmwarekit/plugins/apicedge.exe
%_libdir/firmwarekit/plugins/bashshell.so
%_libdir/firmwarekit/plugins/battery.exe
%_libdir/firmwarekit/plugins/chk_hpet.exe
%_libdir/firmwarekit/plugins/cpufreq.exe
%_libdir/firmwarekit/plugins/dmi.exe
%_libdir/firmwarekit/plugins/ebda.so
%_libdir/firmwarekit/plugins/edd.exe
%_libdir/firmwarekit/plugins/ethernet.exe
%_libdir/firmwarekit/plugins/fadt.so
%_libdir/firmwarekit/plugins/fan.exe
%_libdir/firmwarekit/plugins/maxreadreq.exe
%_libdir/firmwarekit/plugins/mcfg.so
%_libdir/firmwarekit/plugins/microcode.exe
%_libdir/firmwarekit/plugins/msrpoke.so
%_libdir/firmwarekit/plugins/mtrr.exe
%_libdir/firmwarekit/plugins/os2gap.so
%_libdir/firmwarekit/plugins/pcipoke.so
%_libdir/firmwarekit/plugins/pciresource.so
%_libdir/firmwarekit/plugins/suspend.so
%_libdir/firmwarekit/plugins/thermal_trip.sh
%_libdir/firmwarekit/plugins/tonetest.so
%_libdir/firmwarekit/plugins/usbports.so
%_libdir/firmwarekit/plugins/virt.exe
%defattr(0644,root,root,0755)
%_libdir/firmwarekit/plugins/resourcedb.txt
%_libdir/libstandalone.so
%dir %_var/log/firmwarekit
%ghost %_var/log/firmwarekit/acpi.dump
%ghost %_var/log/firmwarekit/DSDT.aml
%ghost %_var/log/firmwarekit/DSDT.dat
%ghost %_var/log/firmwarekit/DSDT.dsl
%_var/log/firmwarekit/resources.css
%ghost %_var/log/firmwarekit/resources.xml
%_var/log/firmwarekit/results.css
%ghost %_var/log/firmwarekit/results.txt
%ghost %_var/log/firmwarekit/results.xml
%dir %_var/log/firmwarekit/usbkey
