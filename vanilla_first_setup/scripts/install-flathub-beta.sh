#!/usr/bin/env bash
pacman -S flatpak
flathub remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
