from pathlib import Path

class RepositoryEngine:

    def __init__(self, root=None):
        if root is None:
            self.root = Path.home()
        else:
            self.root = Path(root)

    def repositories(self):
        repos = []

        for git in self.root.rglob(".git"):
            repos.append(git.parent)

        return sorted(repos)

    def summary(self):
        return {
            "Repositories": len(self.repositories())
        }