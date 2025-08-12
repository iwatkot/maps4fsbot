<p align="center">
<a href="https://github.com/iwatkot/maps4fs">maps4fs</a> •
<a href="https://github.com/iwatkot/maps4fsui">maps4fs UI</a> •
<a href="https://github.com/iwatkot/maps4fsdata">maps4fs Data</a> •
<a href="https://github.com/iwatkot/maps4fsapi">maps4fs API</a> •
<a href="https://github.com/iwatkot/maps4fsstats">maps4fs Stats</a> •
<a href="https://github.com/iwatkot/maps4fsbot">maps4fs Bot</a><br>
<a href="https://github.com/iwatkot/pygmdl">pygmdl</a> •
<a href="https://github.com/iwatkot/pydtmdl">pydtmdl</a>
</p>

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
