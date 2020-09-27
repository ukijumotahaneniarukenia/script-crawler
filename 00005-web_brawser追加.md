VER

```
$ cat /etc/os-release
NAME="Ubuntu"
VERSION="18.04.5 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.5 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

CMD

rootユーザーで以下のコマンドを実行

```
pip3 install --upgrade pip

sed -i.bak -e 's/archive.ubuntu.com\|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

apt update

apt install -y qttools5-dev-tools qttools5-dev

apt install -y python3-qtpy pyqt5-dev pyqt5-dev-tools python3-pyqt5 libqt5widgets5 libqt5gui5 libqt5dbus5 libqt5network5 libqt5core5a

pip3 install SIP

pip3 install PyQt5

pip3 install PySide2

pip3 install PyQtWebEngine

strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
```

VER


```
$ cat /etc/os-release
NAME="Ubuntu"
VERSION="20.04.1 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.1 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```


CMD

rootユーザーで以下のコマンドを実行

```
cd /usr/local/src

apt install -y qttools5-dev-tools qttools5-dev

apt install -y python3-qtpy pyqt5-dev pyqt5-dev-tools python3-pyqt5 libqt5widgets5 libqt5gui5 libqt5dbus5 libqt5network5 libqt5core5a

pip3 install SIP

pip3 install PyQt5

pip3 install PySide2

pip3 install PyQtWebEngine

strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
```



HTTP
- http://www.html-tidy.org/


HTTPS

- https://ukijumotahaneniarukenia.site/



