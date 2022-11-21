class VersionManager:

    def __init__(self, version=''):
        if version == '':
            version = '0.0.1'

        self._major, self._minor, self._patch, *_ = version.split('.') + ['0', '0']

        try:
            self._major, self._minor, self._patch = int(self._major), int(self._minor), int(self._patch)
        except ValueError:
            raise Exception("Error occured while parsing version!")

        self.histoy = []


    def major(self):
        self._add_to_history()
        self._major += 1
        self._minor = self._patch = 0
        return self


    def minor(self):
        self._add_to_history()
        self._minor += 1
        self._patch = 0
        return self


    def patch(self):
        self._add_to_history()
        self._patch += 1
        return self


    def rollback(self):
        try:
            self._major, self._minor, self._patch = self.histoy.pop()
        except IndexError:
            raise Exception("Cannot rollback!")
        return self


    def release(self):
        return f"{self._major}.{self._minor}.{self._patch}"


    def _add_to_history(self):
        self.histoy.append((self._major, self._minor, self._patch))