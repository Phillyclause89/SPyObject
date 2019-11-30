class SPyObject:
    def __init__(self, instance, scope=globals()):
        self.obj = instance
        self.scope = scope
        self.name = self.get_obj_name(self.scope)
        self.type = type(self.obj)
        self.docstr = self.obj.__doc__

    def obj_info(self):
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

    def get_obj_name(self, items=globals()):
        names = []
        for key, x in items.items():
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
            if "items" in dir(x) and len(x) > 0 and self.get_obj_name(items=x) is not None:
                return self.get_obj_name(items=x)
        return names


if __name__ == "__main__":
    def tester():
        return "Hello World"

    FucCaller = tester()
    SPyObject(FucCaller).obj_info()

    class Tester:
        """Some __doc__ text!"""
        def __init__(self, X):
            self.x = X

        def show_x(self):
            return self.x

    ClsCaller = Tester(420)
    SPyObject(ClsCaller).obj_info()

    ClsMetCaller = ClsCaller.show_x()
    SPyObject(ClsMetCaller).obj_info()

    ClsAttrCaller = ClsCaller.x
    SPyObject(ClsAttrCaller).obj_info()

