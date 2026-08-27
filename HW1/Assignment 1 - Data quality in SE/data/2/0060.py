class Monad:
    def __init__(self, value):
        self._value = value

    @classmethod
    def unit(cls, val):
        """Lifts a single value into the elevated world
        Signature: a -> E<a>
        Alternative names: return, pure, unit, yield, point"""
        raise NotImplementedError

    @classmethod
    def lift(cls, func):
        """Lifts a function into the elevated world
        Signature: (a->b) -> E<a> -> E<b>
        Alternative names: map, fmap, lift, select"""
        raise NotImplementedError

    @classmethod
    def liftn(cls, func):
        """Combines two (or three, or four) elevated values using a specified function
        Signature: lift2: (a->b->c) -> E<a> -> E<b> -> E<c>,
                   lift3: (a->b->c->d) -> E<a> -> E<b> -> E<c> -> E<d>, etc
        Alternative names: map, fmap, lift, select"""
        raise NotImplementedError

    @classmethod
    def apply(cls, func):
        """ Unpacks a function wrapped inside a elevated value into a lifted function
        Signature: E<(a->b)> -> E<a> -> E<b>
        Alternative names: ap"""
        raise NotImplementedError

    @property
    def value(self):
        """ Returns wrapped values"""
        return self._value

    def __eq__(self, other):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError
