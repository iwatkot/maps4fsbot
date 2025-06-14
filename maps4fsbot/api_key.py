"""API key generation utilities."""

import base64
import hashlib

from maps4fsbot.config import SECRET_SALT


def generate_api_key(user_id: int) -> str:
    """Generates a unique API key for the user based on their user ID.

    Arguments:
        user_id (int): The unique identifier for the user.

    Returns:
        str: A unique API key for the user, formatted as "encoded_id.hashed_id".
    """
    encoded_id = encode_user_id(user_id)
    raw = f"{user_id}:{SECRET_SALT}"
    hashed = hashlib.sha256(raw.encode()).hexdigest()[:32]
    return f"{encoded_id}.{hashed}"


def encode_user_id(user_id: int) -> str:
    """Encodes the user ID into a URL-safe base64 string.

    Arguments:
        user_id (int): The unique identifier for the user.

    Returns:
        str: A URL-safe base64 encoded string of the user ID.
    """
    return base64.urlsafe_b64encode(str(user_id).encode()).decode().rstrip("=")
