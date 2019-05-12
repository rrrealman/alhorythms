
class Meta(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        print(
            'Meta.__new__(mcs={}, name={}, bases={}, attrs={}, {})'.format(
            mcs, name, bases, attrs, kwargs))

        func = attrs['method']
        def method_wrapper(self):
            return func(self) * 2
        attrs['method'] = method_wrapper
        
        return super().__new__(mcs, name, bases, attrs)
    
    
class Base(metaclass=Meta):
    def method(self):
        return 42

    
class Descendant(Base):
    def method(self):
        return 25

    
if __name__ == '__main__':
    b = Base()
    d = Descendant()
    print(b.method())
    print(d.method())
