#!/usr/bin/bash
pacman -S --noconfirm nix
systemctl enable --now nix-daemon.service
usermod -aG nix-users $(id -nu $PKEXEC_UID)
su $(id -nu $PKEXEC_UID) -c 'nix-channel --add https://nixos.org/channels/nixpkgs-unstable'
su $(id -nu $PKEXEC_UID) -c 'nix-channel --update'