class Circle:
    def __init__(self, radius):
        self._radius = radius

    def __eq__(self, other):
        """
            :type other: Circle
        """
        if other._radius == self._radius:
            return True
        return False

    def __le__(self, other):
        """
            :type other: Circle
        """
        if other._radius >= self._radius:
            return True
        return False

    def __lt__(self, other):
        """
            :type other: Circle
        """
        if other._radius > self._radius:
            return True
        return False

    def __add__(self, other):
        """
            :type other: Circle
        """
        self._radius += other._radius
        return self._radius

    def __iadd__(self, other):
        """
            :type other: Circle
        """
        self._radius += other._radius
        return self._radius

    def __sub__(self, other):
        """
            :type other: Circle
        """
        self._radius -= other._radius
        return self._radius

    def __isub__(self, other):
        """
            :type other: Circle
        """
        self._radius = self._radius - other._radius
        return self._radius