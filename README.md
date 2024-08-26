# Homelab

- Hardware:
    - Mainboard: [ASRock N100M](https://www.asrock.com/mb/Intel/N100M/)
    - RAM: [Team Electronic Elite 32GB DDR4 3200](https://www.teamgroupinc.com/de/product-detail/memory/TEAMGROUP/elite-u-dimm-ddr4/elite-u-dimm-ddr4-TED432G3200C2201/)
    - PSU: [Cooler Master MWE 600 Bronze V2](https://www.coolermaster.com/de/de-de/catalog/power-supplies/mwe-series/mwe-600-bronze-v2/)
    - SSD: [Samsung 860 Evo](https://www.samsung.com/de/memory-storage/sata-ssd/860-evo-sata-3-2-5-inch-ssd-500gb-mz-76e500b-eu/)
    - HDDs: 2x Seagate 1,5TB [ST31500341AS](https://www.amazon.de/Seagate-Barracuda-Festplatte-Cache-ST31500341AS/dp/B001IKKCLI) & 2x Seagate 4TB [ST4000DM004](https://www.amazon.de/Seagate-ST4000DM004-Barracuda-interne-Festplatte/dp/B0713R3Y6F)
    - M.2 to SATA Adapter: [KALEA-INFORMATIQUE ASM1166](https://www.amazon.de/Karte-M-2-Ports-SATA-Schl%C3%BCssel/dp/B0B77C2L1K)

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
- Virtual Machines:
    - [Docker](https://docs.docker.com/engine/install/)[^2]
        - [Vaultwarden](https://github.com/dani-garcia/vaultwarden)
        - [Organizr](https://github.com/causefx/Organizr)
        - [Nginx Proxy Manager](https://nginxproxymanager.com/)
        - [Gotify](https://gotify.net/)
        - [Jellyseerr](https://github.com/Fallenbagel/jellyseerr)
        - [Watchtower](https://containrrr.dev/watchtower/)
        - [Dockge](https://github.com/louislam/dockge)
        - [SABnzbd](https://sabnzbd.org/)
    - [Azerothcore](https://www.azerothcore.org/) with modules
        - [mod-playerbots](https://github.com/liyunfan1223/mod-playerbots)
        - [DungeonRespawn](https://github.com/AnchyDev/DungeonRespawn)
        - [mod-account-achievements](https://github.com/azerothcore/mod-account-achievements)
        - [mod-ah-bot](https://github.com/azerothcore/mod-ah-bot)
        - [mod-aoe-loot](https://github.com/azerothcore/mod-aoe-loot)
        - [mod-arac](https://github.com/heyitsbench/mod-arac)
        - [mod-groupquest](https://github.com/noisiver/mod-groupquests)
        - [mod-instance-reset](https://github.com/azerothcore/mod-instance-reset)
        - [mod-no-hearthstone-cooldown](https://github.com/BytesGalore/mod-no-hearthstone-cooldown)
        - [mod-transmog](https://github.com/azerothcore/mod-transmog)
        - [mod-vanilla-naxxramas](https://github.com/sogladev/mod-vanilla-naxxramas)
        - [mod-warlock-pet-rename](https://github.com/silviu20092/mod-warlock-pet-rename)


[Raspberry Pi 4 Model B Rev 1.5 2GB](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/):
- Backup [Pi-hole](https://github.com/pi-hole/pi-hole/#one-step-automated-install) + [Unbound](https://docs.pi-hole.net/guides/dns/unbound/)
- [Zabbix](https://www.zabbix.com/download?zabbix=6.0&os_distribution=debian_arm64&os_version=12&components=server_frontend_agent&db=mysql&ws=apache)
- [Proxmox Backup Server](https://github.com/wofferl/proxmox-backup-arm64)

[^1]:My [Settings](https://github.com/Blitzritze/homelab/tree/main/media).

[^2]:My [Compose files](https://github.com/Blitzritze/homelab/tree/main/docker).
