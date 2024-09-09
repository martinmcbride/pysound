import numpy as np

from pysound.pysound_defs import BaseUnit, Unit, DATA_LENGTH, Connection


class AddUnit(BaseUnit):
    """
    Add two signals
    """

    def __init__(self, a: Unit, b: Unit):
        """
        Args:
            a: Input unit a
            b: Input unit b

        Returns:
            a + b
        """
        super().__init__()
        self.data_length = DATA_LENGTH
        self.a = Connection(a)
        self.b = Connection(b)


    def get(self):
        a = self.a.get(self.data_length)
        b = self.b.get(self.data_length)
        return a + b


class NegUnit(BaseUnit):
    """
    Negate a  signals
    """

    def __init__(self, a: Unit):
        """
        Args:
            a: Input unit a

        Returns:
            -a
        """
        super().__init__()
        self.data_length = DATA_LENGTH
        self.a = Connection(a)


    def get(self):
        a = self.a.get(self.data_length)
        return -a


class SubUnit(BaseUnit):
    """
    Subtract two signals
    """

    def __init__(self, a: Unit, b: Unit):
        """
        Args:
            a: Input unit a
            b: Input unit b

        Returns:
            a - b
        """
        super().__init__()
        self.data_length = DATA_LENGTH
        self.a = Connection(a)
        self.b = Connection(b)

    def get(self):
        a = self.a.get(self.data_length)
        b = self.b.get(self.data_length)
        return a - b


class MulUnit(BaseUnit):
    """
    Multiply two signals
    """

    def __init__(self, a: Unit, b: Unit):
        """
        Args:
            a: Input unit a
            b: Input unit b

        Returns:
            a * b
        """
        super().__init__()
        self.data_length = DATA_LENGTH
        self.a = Connection(a)
        self.b = Connection(b)

    def get(self):
        a = self.a.get(self.data_length)
        b = self.b.get(self.data_length)
        return a * b


class DivUnit(BaseUnit):
    """
    Divide two signals
    """

    def __init__(self, a: Unit, b: Unit):
        """
        Args:
            a: Input unit a
            b: Input unit b

        Returns:
            a * b
        """
        super().__init__()
        self.data_length = DATA_LENGTH
        self.a = Connection(a)
        self.b = Connection(b)

    def get(self):
        a = self.a.get(self.data_length)
        b = self.b.get(self.data_length)
        return a / b


class MinUnit(BaseUnit):
    """
    Find minimum of two signals
    """

    def __init__(self, a: Unit, b: Unit):
        """
        Args:
            a: Input unit a
            b: Input unit b

        Returns:
            minimum(a, b)
        """
        super().__init__()
        self.data_length = DATA_LENGTH
        self.a = Connection(a)
        self.b = Connection(b)

    def get(self):
        a = self.a.get(self.data_length)
        b = self.b.get(self.data_length)
        return np.minimum(a, b)


class MaxUnit(BaseUnit):
    """
    Find minimum of two signals
    """

    def __init__(self, a: Unit, b: Unit):
        """
        Args:
            a: Input unit a
            b: Input unit b

        Returns:
            maximum(a, b)
        """
        super().__init__()
        self.data_length = DATA_LENGTH
        self.a = Connection(a)
        self.b = Connection(b)

    def get(self):
        a = self.a.get(self.data_length)
        b = self.b.get(self.data_length)
        return np.maximum(a, b)



