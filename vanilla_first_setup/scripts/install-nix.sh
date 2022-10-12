#!/usr/bin/bash
pacman -S nix
systemctl enable --now nix-daemon.service
su $(id -nu $PKEXEC_UID) -c 'nix-channel --add https://nixos.org/channels/nixpkgs-unstable'
su $(id -nu $PKEXEC_UID) -c 'nix-update --channel'