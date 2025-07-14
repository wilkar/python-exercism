import string
import random


letters = string.ascii_uppercase


class Robot:
    _used_names: set = set()

    def __init__(self):
        self._name = None
        self.reset()

    @property
    def name(self):
        return self._name

    def set_name(self) -> str:
        while True:
            prefix = random.choices(letters, k=2)
            sufix = [str(random.randint(0, 9)) for _ in range(3)]
            name = "".join(prefix + sufix)
            if name not in Robot._used_names:
                Robot._used_names.add(name)
                return name

    def reset(self):
        if self._name in Robot._used_names:
            Robot._used_names.remove(self._name)
        randnewname = self.set_name()

        self._name = self.set_name()
