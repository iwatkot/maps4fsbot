<div align="center" markdown>
<img src="https://github.com/user-attachments/assets/62cd4824-ab72-42f4-af54-0bc70e00dd00">
</a>

<p align="center">
    <a href="#launch-in-docker">Lanuch in Docker</a> •
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