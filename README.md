# Homelab
ASRock N100M motherboard and Cooler Master MWE 600 PSU. 4 HDDs for NAS storage and one SSD for OS/VM/LXC storage. 

To expand the number of SATA connections, a M.2 to SATA controller with an ASM1166 chip is used.

[Proxmox VE](https://www.proxmox.com/en/proxmox-virtual-environment/):
- Containers:
    - [Pi-hole](https://github.com/pi-hole/pi-hole/#one-step-automated-install) + [Unbound](https://docs.pi-hole.net/guides/dns/unbound/)
    - Alpine SAMBA File Share
    - [Jellyfin](https://jellyfin.org/docs/general/installation/linux) & [Audiobookshelf](https://www.audiobookshelf.org/docs/#linux-install-deb)
    - [Arrs](https://wiki.servarr.com/)
        - [Sonarr](https://sonarr.tv/)[^1]
        - [Radarr](https://radarr.video/)[^1]
        - [Bazarr](https://www.bazarr.media/)
        - [Prowlarr](https://github.com/Prowlarr/Prowlarr)
        - [SABnzbd](https://sabnzbd.org/)
- Virtual Machines:
    - [Docker](https://docs.docker.com/engine/install/)[^2]
        - [Vaultwarden](https://github.com/dani-garcia/vaultwarden)
        - [Organizr](https://github.com/causefx/Organizr)
        - [Nginx Proxy Manager](https://nginxproxymanager.com/)
        - [Gotify](https://gotify.net/)
        - [Jellyseerr](https://github.com/Fallenbagel/jellyseerr)
        - [Watchtower](https://containrrr.dev/watchtower/)
        - [Dockge](https://github.com/louislam/dockge)
        - [Grocy](https://docs.linuxserver.io/images/docker-grocy/)
        - [Barcodebuddy](https://github.com/Forceu/barcodebuddy-docker)
        - [Ansible Semaphore](https://docs.semui.co/administration-guide/installation)
    - [Proxmox Backup Server](https://www.proxmox.com/en/proxmox-backup-server/)

Raspberrypi:
- Backup [Pi-hole](https://github.com/pi-hole/pi-hole/#one-step-automated-install) + [Unbound](https://docs.pi-hole.net/guides/dns/unbound/)

[^1]:My [Settings](https://github.com/Blitzritze/homelab/tree/main/media).

[^2]:My [Compose files](https://github.com/Blitzritze/homelab/tree/main/docker).
