class BaseBranch:
    def __init__(self):
        self.commits = []


class BaseNewGitRepository:
    def __init__(self, branches):
        self.branches = branches