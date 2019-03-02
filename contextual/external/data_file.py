from pathlib import Path

app_dir = Path.home().joinpath(".contextual")
if not app_dir.exists():
    app_dir.mkdir()
