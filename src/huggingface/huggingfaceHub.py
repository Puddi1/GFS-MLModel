from huggingface_hub import hf_hub_download


def DownloadFromHfHub(repo_id: str, filename: str, repo_type: str | None = None,) -> str:
    # also add where to save file + cache problems
    return hf_hub_download(repo_id, filename, repo_type)
