Summary:	Metapackage for Nagios(tm)
Name:		task-nagios
Version:	0
Release:	%mkrel 4
Group:		System/Servers
License:	GPL
BuildArch:	noarch
Requires:	nagios
Requires:	nagios-conf
Requires:	nagios-imagepaks
Requires:	nagios-plugins
Requires:	nagios-theme-default
Requires:	nagios-www
Requires:	nagios-check_adptraid
Requires:	nagios-check_apache
Requires:	nagios-check_apc_ups
Requires:	nagios-check_appletalk
Requires:	nagios-check_arping
Requires:	nagios-check_asterisk
Requires:	nagios-check_axis
Requires:	nagios-check_backup
Requires:	nagios-check_bgp
Requires:	nagios-check_bgpstate
Requires:	nagios-check_breeze
Requires:	nagios-check_by_ssh
Requires:	nagios-check_ciscotemp
Requires:	nagios-check_cluster
Requires:	nagios-check_cluster2
Requires:	nagios-check_compaq_insight
Requires:	nagios-check_dhcp
Requires:	nagios-check_dig
Requires:	nagios-check_digitemp
Requires:	nagios-check_disk
Requires:	nagios-check_disk_smb
Requires:	nagios-check_dlswcircuit
Requires:	nagios-check_dns
Requires:	nagios-check_dns_random
Requires:	nagios-check_dummy
Requires:	nagios-check_email_loop
Requires:	nagios-check_file_age
Requires:	nagios-check_flexlm
Requires:	nagios-check_fping
Requires:	nagios-check_frontpage
Requires:	nagios-check_game
Requires:	nagios-check_hpjd
Requires:	nagios-check_hprsc
Requires:	nagios-check_http
Requires:	nagios-check_hw
Requires:	nagios-check_ica_master_browser
Requires:	nagios-check_ica_metaframe_pub_apps
Requires:	nagios-check_ica_program_neigbourhood
Requires:	nagios-check_icmp
Requires:	nagios-check_ide_smart
Requires:	nagios-check_ifoperstatus
Requires:	nagios-check_ifstatus
Requires:	nagios-check_inodes
Requires:	nagios-check_ipxping
Requires:	nagios-check_ircd
Requires:	nagios-check_javaproc
Requires:	nagios-check_ldap
Requires:	nagios-check_linux_raid
Requires:	nagios-check_load
Requires:	nagios-check_log
Requires:	nagios-check_log2
Requires:	nagios-check_lotus
Requires:	nagios-check_mailq
Requires:	nagios-check_maxchannels
Requires:	nagios-check_maxwanstate
Requires:	nagios-check_mem
Requires:	nagios-check_ms_spooler
Requires:	nagios-check_mssql
Requires:	nagios-check_mysql
Requires:	nagios-check_mysql_query
Requires:	nagios-check_nagios
Requires:	nagios-check_netapp
Requires:	nagios-check_nmap
Requires:	nagios-check_nt
Requires:	nagios-check_ntp
Requires:	nagios-check_ntp_peer
Requires:	nagios-check_ntp_time
Requires:	nagios-check_nwstat
Requires:	nagios-check_oracle
Requires:	nagios-check_overcr
Requires:	nagios-check_pcpmetric
Requires:	nagios-check_pfstate
Requires:	nagios-check_pgsql
Requires:	nagios-check_ping
Requires:	nagios-check_procs
Requires:	nagios-check_qmailq
Requires:	nagios-check_radius
Requires:	nagios-check_rbl
Requires:	nagios-check_real
Requires:	nagios-check_remote_nagios_status
Requires:	nagios-check_rpc
Requires:	nagios-check_sendim
Requires:	nagios-check_sensors
Requires:	nagios-check_smart
Requires:	nagios-check_smb
Requires:	nagios-check_smtp
Requires:	nagios-check_snmp
Requires:	nagios-check_snmp_disk_monitor
Requires:	nagios-check_snmp_printer
Requires:	nagios-check_snmp_process_monitor
Requires:	nagios-check_snmp_procs
Requires:	nagios-check_sockets
Requires:	nagios-check_ssh
Requires:	nagios-check_swap
Requires:	nagios-check_tcp
Requires:	nagios-check_time
Requires:	nagios-check_timeout
Requires:	nagios-check_traceroute
Requires:	nagios-check_ups
Requires:	nagios-check_uptime
Requires:	nagios-check_users
Requires:	nagios-check_wave
Requires:	nagios-check_wins
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package is a meta-package that will suck in most of the needed packages
to run Nagios(tm) seamlessly.

%files



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0-4mdv2011.0
+ Revision: 615113
- the mass rebuild of 2010.1 packages

* Mon Mar 22 2010 Thierry Vignaud <tv@mandriva.org> 0-3mdv2010.1
+ Revision: 526668
- nagios-check_mrtg* are no more

* Mon Oct 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0-2mdv2010.0
+ Revision: 454327
- nagios-check_mysql_perf doesn't exist anymore

* Tue May 12 2009 Oden Eriksson <oeriksson@mandriva.com> 0-1mdv2010.0
+ Revision: 374921
- import task-nagios


* Tue May 12 2009 Oden Eriksson <oeriksson@mandriva.com> 0-1mdv2010.0
- initial Mandriva package
