from git import Repo


def git_info(working_dir):
    repo = Repo(working_dir)
    if not repo.bare:
        branch = repo.head.reference.name
        tree_diff = repo.head.commit.diff(None)
        return branch, len(tree_diff)
