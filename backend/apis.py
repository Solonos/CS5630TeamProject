import asyncio

import requests
from chessdotcom.aio import ChessDotComResponse, Client, get_player_profile


class ChessDotComClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rate_limit_handler.tries = 2
        self.rate_limit_handler.tts = 4
        self.request_config["headers"]["User-Agent"] = "ben.ruckman@live.com"

    async def get_players(self, usernames: list[str]):
        cors = [get_player_profile(name) for name in usernames]

        async def gather_cors(cors: list[ChessDotComResponse]):
            return await asyncio.gather(*cors)

        responses = await gather_cors(cors)
        return responses

    # async def get_players_from_league(self, league_id: str):
    #     CLient.

    async def get_players_from_leaderboards(self):
        pass
