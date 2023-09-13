from pathlib import Path as P

from chessdotcom import get_player_profile

chess_path = P(__file__).parent / "data" / "chess.com"


def get_player(username):
    return get_player_profile(username).json()


response = get_player_profile("fabianocaruana")
chess_path.write_text(response.json())

player_name = response.player.name
