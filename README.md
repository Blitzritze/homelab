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
        - [Sonarr V4](https://sonarr.tv/)
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
        - [Guacamole](https://github.com/boschkundendienst/guacamole-docker-compose)
        - [Watchtower](https://containrrr.dev/watchtower/)
        - [Portainer](https://docs.portainer.io/start/install-ce)[^3]
        - [Dockge](https://github.com/louislam/dockge)
        - [Dozzle](https://dozzle.dev/)[^3]
    - [Ansible](https://docs.ansible.com/ansible/latest/index.html) with [Ansible Semaphore](https://github.com/ansible-semaphore/semaphore)

Raspberrypi:
- [Proxmox Backup Server](https://github.com/wofferl/proxmox-backup-arm64)
- Backup Pi-hole + Unbound

[^1]:[Some Settings](https://github.com/Blitzritze/homelab/tree/3dbaa343cc9bb6ce9e8edc5599ff26d274491b66/media).

[^2]:[Docker Compose](https://github.com/Blitzritze/homelab/tree/3dbaa343cc9bb6ce9e8edc5599ff26d274491b66/docker) files.

[^3]:Not sure if or how long these containers will stay.
