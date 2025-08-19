---
title: Enable desktop applications
weight: 4
layout: "learningpathall"
---

To use desktop applications like browsers in the Ubuntu container, you need to enable the connection to the ChromeOS desktop using Sommelier. 

Sommelier acts as a bridge, enabling seamless integration and smooth operation of Linux apps within the ChromeOS environment.

## Enable support for Linux GUI applications

Install a minimal desktop environment to provide the necessary libraries for graphical applications:

```bash
sudo apt install -y xubuntu-desktop-minimal
```

Install a test application:

```bash
sudo apt install -y terminator
```

Configure the display environment variables so GUI applications know where to render their windows:

```console
echo 'export DISPLAY=:0' >> ~/.bashrc
```

Install the necessary tools to build Sommelier:

```bash
sudo apt install -y clang meson libwayland-dev cmake pkg-config libgbm-dev libdrm-dev libxpm-dev libpixman-1-dev libx11-xcb-dev libxcb-composite0-dev libxkbcommon-dev libgtest-dev python3-jinja2
```

Build Sommelier from source code because it is not available in Ubuntu repositories:

```bash
git clone https://chromium.googlesource.com/chromiumos/platform2
cd platform2/vm_tools/sommelier
meson build
cd build
ninja
sudo ninja install
```

Sommelier is now installed in `/usr/local/bin/`.

Create a systemd user unit file for X11 support:

```bash
mkdir -p ~/.config/systemd/user
```

Use a text editor to create the file `~/.config/systemd/user/sommelier@.service` with the following contents:

```ini
[Unit]
Description=Sommelier X11 bridge instance %i

[Service]
Environment=DISPLAY=:0
ExecStart=/usr/local/bin/sommelier -X --scale=1 --no-exit-with-child -- /bin/true
Restart=on-failure

[Install]
WantedBy=default.target
```

Reload the systemd user manager and start the Sommelier service:

```bash
systemctl --user daemon-reload
systemctl --user enable --now sommelier@0.service
```

Confirm the Sommelier service is running:

```bash
systemctl --user status sommelier@0.service
```

Test a graphical application. You can pick any application you installed, such as Terminator:

```bash
terminator &
```

You should see a new terminal open on your ChromeOS desktop.

If needed, you can restart Sommelier:

```bash
sudo systemctl restart sommelier@0
```
