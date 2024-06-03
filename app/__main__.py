from os import getenv

from fastapi import FastAPI
from httpx import Client
from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_TOKEN: SecretStr

    @classmethod
    def from_vault(cls, vault_url: str, vault_token: str):
        with Client() as client:
            response = client.get(
                url=vault_url,
                headers={
                    "X-Vault-Token": vault_token
                }
            )
            if response.status_code == 200:
                return cls.model_validate(response.json().get("data"))


settings = Settings.from_vault(
    vault_url=getenv("VAULT_URL"),
    vault_token=getenv("VAULT_TOKEN")
)


app = FastAPI()


@app.get(path="/secret")
async def secret():
    return {"token": settings.API_TOKEN.get_secret_value()}


if __name__ == '__main__':
    from uvicorn import run
    run(app=app, host="0.0.0.0", port=80)
