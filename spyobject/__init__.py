class SPyObject:
    """
    A class used to spy on Python Object Instances

    ...

    Attributes
    ----------
    obj : object instance
        an instance of the object being spied on
    scope : dict
        the scope in memory for finding assignments should be either
        globals() or locals()
    name : list
        a list of variable names assigned to this object
    type : type
        holds the spied object's type()
    docstr : str
        the __doc__ text of the spied object, if there is any
    attributes : list
        holds the spied object's dir()


    Methods
    -------
    __init__(instance, scope)
        Initialize the spying object with an instance of the spied object. Will call the
        get_obj_name(scope) method to recursively search the globals() or locals() scope list
        for variables or functions that are assigned to or return the spied object.
    obj_info()
        Prints a spy report for the spied object. For example:

        >>>import spyobject as spy
        >>>x = 420
        >>>spy.SPyObject(x, globals()).obj_info()
        ___________________________________________________________________________

        Name Assignment(s): ['x <variable x at 0X193E53711F0>']

        Return Value: 420

        Return Type: <class 'int'>

        __doc__ Text: int([x]) -> integer
        int(x, base=10) -> integer

        Convert a number or string to an integer, or return 0 if no arguments
        are given.  If x is a number, return x.__int__().  For floating point
        numbers, this truncates towards zero.

        If x is not a number or if base is given, then x must be a string,
        bytes, or bytearray instance representing an integer literal in the
        given base.  The literal can be preceded by '+' or '-' and be surrounded
        by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
        Base 0 means to interpret the base from the string as an integer literal.
        >>> int('0b100', base=0)
        4
        ___________________________________________________________________________
    get_obj_name(scope)
        A method called during __init__ to search the scope for any variable/function names pointing to the
        spied object. If any names are found they will be returned as a list.

    """

    def __init__(self, instance, scope):
        """
        Initialize the spying object with an instance of the spied object.

        Parameters
        ----------
        :param instance: object
            The object to be spied on. The instance will be assigned to the obj attribute.
        :param scope: dict
            The scope in memory to search for assignments. Can be the dictionary object returned by
            globals() or locals() builtins.

        Return
        -----------
        :return: An instance of spyobject.SPyObject

        """

        self.obj = instance
        self.scope = scope
        self.name = self.get_obj_name(self.scope)
        self.type = type(self.obj)
        self.docstr = self.obj.__doc__
        self.attributes = dir(self.obj)
        if len(self.name) == 0:
            self.name = [f"No Assignments Found for {self.obj}", ]

    def obj_info(self):
        """
        Prints the spy report for the spied object.

        Parameters
        ----------
        None

        Return
        ----------
        :return: None
            (Prints Debug Info to Console)
        """

        print(
            f"{'_' * 75}\n\n"
            f"\033[1;35mName Assignment(s):\033[1;m "
            f"{self.name}"
            f"\n\n\033[1;35mReturn Value:\033[1;m "
            f"{self.obj}"
            f"\n\n\033[1;35mReturn Type:\033[1;m "
            f"{self.type}"
            f"\n\n\033[1;35m__doc__ Text:\033[1;m "
            f"{self.docstr}"
            f"\n{'_' * 75}"
        )

    def get_obj_name(self, scope):
        """
        A method called automatically during __init__ to search the scope for any variable/function names
        pointing to the spied object.

        Parameters
        ----------
        :param scope: dict
            By default this class uses the scope dict from the __init__ method. This param is modified with
            each recursive call of the method.

        Return
        -----------
        :return: list
            Returns a list of variables or functions that point to or return the object

        """

        names = []
        for key, x in scope.items():
            if x is self.obj and key is not None:
                names.append(f"{key} <variable {key} at {hex(id(key)).upper()}>")
            if "<function" in str(x):
                try:
                    if str(self.obj) == str(eval(f"{key}()")):
                        names.append(f"{key} {x}")
                    if isinstance(self.obj, pandas.core.groupby.generic.DataFrameGroupBy) and str(
                            self.obj.describe()) == str(eval(f"{key}()").describe()):
                        names.append(f"{key} {x}")
                except TypeError:
                    pass
                except NameError:
                    pass
            if "items" in dir(x) and self.get_obj_name(scope=x) is not None:
                if len(x) > 0:
                    names.append(self.get_obj_name(scope=x))
        return names


if __name__ == "__main__":
    def tester():
        return "Hello World"

    SPyObject(tester(), globals()).obj_info()
    FucCaller = tester()
    SPyObject(FucCaller, globals()).obj_info()


    class Tester:
        """Some __doc__ text!"""

        def __init__(self, V):
            self.v = V

        def show_v(self):
            return self.v


    ClsCaller = Tester(420)
    SPyObject(ClsCaller, globals()).obj_info()

    ClsMetCaller = ClsCaller.show_v()
    SPyObject(ClsMetCaller, globals()).obj_info()

    ClsAttrCaller = ClsCaller.v
    SPyObject(ClsAttrCaller, globals()).obj_info()
