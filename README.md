# My Homelab
[Proxmox VE](https://www.proxmox.com/en/proxmox-virtual-environment/):
- Containers:
    - [Pi-hole](https://github.com/pi-hole/pi-hole/#one-step-automated-install) + [Unbound](https://docs.pi-hole.net/guides/dns/unbound/)
    - [Grafana](https://grafana.com/grafana/download)
    - [InfluxDB](https://www.influxdata.com/downloads/)
    - Python specific container
    - [Turnkey Fileserver](https://www.turnkeylinux.org/fileserver)
- Virtual Machines:
    - [Jellyfin](https://github.com/jellyfin/jellyfin)[^1]
        - [Sonarr](https://sonarr.tv/)
        - [Radarr](https://radarr.video/)
        - [Bazarr](https://www.bazarr.media/)
        - [SABnzbd](https://sabnzbd.org/)
        - [Prowlarr](https://github.com/Prowlarr/Prowlarr)
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
    - [Proxmox Backup Server](https://github.com/wofferl/proxmox-backup-arm64)

Raspberrypi:
- Backup [Pi-hole](https://github.com/pi-hole/pi-hole/#one-step-automated-install) + [Unbound](https://docs.pi-hole.net/guides/dns/unbound/)

[^1]:[My Settings](https://github.com/Blitzritze/homelab/tree/main/media).

[^2]:[My Compose](https://github.com/Blitzritze/homelab/tree/main/docker) files.
