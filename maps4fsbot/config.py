"""Configuration for the bot."""

import os
import shutil
import subprocess
import tempfile

try:
    from dotenv import load_dotenv

    load_dotenv("local.env")
except ModuleNotFoundError:
    pass

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN is not set")

SECRET_SALT = os.getenv("SECRET_SALT")
if not SECRET_SALT:
    raise ValueError("SECRET_SALT is not set")


class Roles:
    """Roles for the bot."""

    admin = "Admin"
    moderator = "Moderator"


class Channels:
    """Channels for the bot."""

    suggest_feature = "suggest-feature"


CHROMADOCS_REPO = "https://github.com/iwatkot/maps4fschromadocs.git"

CHROMA_DB_DIR_NAME = "chroma_db"
CHROMA_DB_DIR = os.path.join(os.getcwd(), CHROMA_DB_DIR_NAME)
print(f"Chroma DB directory: {CHROMA_DB_DIR}")
EMBEDDING_MODEL = "nomic-embed-text"  # For retrieval
LLM_MODEL = "llama3.2:3b"  # Balanced lightweight model - good quality/speed tradeoff
TOP_K_RESULTS = 8  # Number of relevant chunks to retrieve


def ensure_chroma_db():
    """Ensure that the Chroma DB directory exists, downloading if necessary."""
    if not os.path.isdir(CHROMA_DB_DIR) or not os.listdir(CHROMA_DB_DIR):
        print(f"Warning: Chroma DB directory {CHROMA_DB_DIR} does not exist or is empty.")
        print("Attempting to download Chroma DB from repository...")

        try:

            # Create temporary directory for cloning
            with tempfile.TemporaryDirectory() as temp_dir:
                clone_path = os.path.join(temp_dir, "chromadocs")

                # Shallow clone the repository
                subprocess.run(
                    ["git", "clone", "--depth", "1", CHROMADOCS_REPO, clone_path], check=True
                )

                # Copy the chroma_db folder from the cloned repo
                source_chroma = os.path.join(clone_path, CHROMA_DB_DIR_NAME)
                if os.path.isdir(source_chroma):
                    shutil.copytree(source_chroma, CHROMA_DB_DIR)
                    print(f"Successfully downloaded Chroma DB to {CHROMA_DB_DIR}")
                else:
                    print(f"Error: {CHROMA_DB_DIR_NAME} folder not found in {CHROMADOCS_REPO}")

        except Exception as e:
            print(f"Failed to download Chroma DB: {e}")
            print("Please manually clone the repository or create the chroma_db folder.")


ensure_chroma_db()
