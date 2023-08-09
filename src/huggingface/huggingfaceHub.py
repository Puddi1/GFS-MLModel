from huggingface_hub import hf_hub_download
import os


def DownloadFromHfHub(repo_id: str, filename: str) -> str:
    """DownloadFromHfHub is the comment of the function
    test
    test
    """

    downloadPath = "./hf/"
    # , repo_type: str | None = None
    # also add where to save file + cache problems
    # return hf_hub_download(repo_id, filename, repo_type)
    return True
