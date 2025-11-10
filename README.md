<div align="center" markdown>

[![Maps4FS](https://img.shields.io/badge/maps4fs-gray?style=for-the-badge)](https://github.com/iwatkot/maps4fs)
[![PYDTMDL](https://img.shields.io/badge/pydtmdl-blue?style=for-the-badge)](https://github.com/iwatkot/pydtmdl)
[![PYGDMDL](https://img.shields.io/badge/pygmdl-teal?style=for-the-badge)](https://github.com/iwatkot/pygmdl)  
[![Maps4FS API](https://img.shields.io/badge/maps4fs-api-green?style=for-the-badge)](https://github.com/iwatkot/maps4fsapi)
[![Maps4FS UI](https://img.shields.io/badge/maps4fs-ui-blue?style=for-the-badge)](https://github.com/iwatkot/maps4fsui)
[![Maps4FS Data](https://img.shields.io/badge/maps4fs-data-orange?style=for-the-badge)](https://github.com/iwatkot/maps4fsdata)
[![Maps4FS ChromaDocs](https://img.shields.io/badge/maps4fs-chromadocs-orange?style=for-the-badge)](https://github.com/iwatkot/maps4fschromadocs)  
[![Maps4FS Upgrader](https://img.shields.io/badge/maps4fs-upgrader-yellow?style=for-the-badge)](https://github.com/iwatkot/maps4fsupgrader)
[![Maps4FS Stats](https://img.shields.io/badge/maps4fs-stats-red?style=for-the-badge)](https://github.com/iwatkot/maps4fsstats)
[![Maps4FS Bot](https://img.shields.io/badge/maps4fs-bot-teal?style=for-the-badge)](https://github.com/iwatkot/maps4fsbot)

</div>

<div align="center" markdown>
<img src="https://github.com/user-attachments/assets/62cd4824-ab72-42f4-af54-0bc70e00dd00">
</a>

<p align="center">
    <a href="#launch-in-docker">Launch in Docker</a> •
    <a href="https://manage.maps4fs.xyz/">Portainer Management</a> •
    <a href="https://stats.maps4fs.xyz/">Statistics Management</a> •
    <a href="https://stats.maps4fs.xyz/public/dashboard/f8defe6a-09db-4db1-911f-b6b02075d4b2">Public Statistics</a>
</p>
</div>

## Launch in Docker

```bash
docker stop maps4fsbot
docker rm maps4fsbot
docker image rm iwatkot/maps4fsbot
docker system prune -f
docker run -d --name maps4fsbot -e DISCORD_TOKEN="YOUR-TOKEN-HERE" iwatkot/maps4fsbot
```
