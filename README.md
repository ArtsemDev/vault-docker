```
cd vault
docker compose up
docker exec -it vault vault operator init
docker exec -it vault vault operator unseal <unseal key 1>
docker exec -it vault vault operator unseal <unseal key 2>
docker exec -it vault vault operator unseal <unseal key 3>
docker exec -it vault vault login <root token>
docker exec -it vault vault secrets enable -version=1 -path=secret kv
```