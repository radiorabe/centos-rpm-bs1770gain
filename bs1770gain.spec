#
# spec file for package bs1770gain
#
# Copyright (c) 2018 Radio Bern RaBe
#                    http://www.rabe.ch
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public 
# License as published  by the Free Software Foundation, version
# 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License  along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
# Please submit enhancements, bugfixes or comments via GitHub:
# https://github.com/radiorabe/centos-rpm-bs1770gain
#


Name:           bs1770gain
Version:        0.4.12
Release:        1%{?dist}
Summary:        BS1770GAIN is a loudness scanner implementing ITU-R BS.1770.

License:        GPLv2
URL:            http://bs1770gain.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

# Upstream builds their static releases against avutil-55, swresample-2,
# avcodec-57 and avformat-57 (as of 2015-09-12, 0.4.6). We do the same here by
# requiring a newer ffmpeg version.
BuildRequires:  ffmpeg-devel >= 3.3
BuildRequires:  sox-devel

%description
BS1770GAIN is a loudness scanner compliant with ITU-R BS.1770 and its flavors
EBU R128, ATSC A/85, and ReplayGain 2.0. It helps normalizing the loudness of
audio and video files to the same level.



%prep
%setup -q


%build
# Detect the header directories for ffmpeg and sox as they are located outside
# the default GCC search path and the configure script currently doesn't use
# pkg-config macros.
FFMPEG_CFLAGS="$( ${cross_prefix}pkg-config --cflags libavformat libavcodec \
                                                     libswscale libavutil )"

SOX_CFLAGS="$( ${cross_prefix}pkg-config --cflags sox )"

%configure CFLAGS="%{optflags} ${FFMPEG_CFLAGS} ${SOX_CFLAGS}"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc ChangeLog NEWS README
%{_bindir}/*



%changelog
* Fri Jan 12 2018 Christian Affolter <c.affolter@purplehaze.ch> - 0.4.12-1
- Initial release

