def obj_info(obj):
    def get_obj_name(_obj, items=globals()):
        for key, x in items.items():
            if x is _obj and key is not None:
                return key
            if "<function" in str(x):
                try:
                    if str(_obj) == str(eval(f"{key}()")):
                        return f"{key} {x}"
                    if isinstance(_obj, pd.core.groupby.generic.DataFrameGroupBy) and str(_obj.describe()) == str(
                            eval(f"{key}()").describe()):
                        return f"{key} {x}"
                except TypeError:
                    pass
            if "items" in dir(x) and len(x) > 0 and get_obj_name(_obj, items=x) is not None:
                return get_obj_name(_obj, items=x)

    name = get_obj_name(obj)
    print(
        f"{'_' * 75}\n\n"
        f"\033[1;35mname:\033[1;m "
        f"{name}"
        f"\n\n\033[1;35mvalue:\033[1;m "
        f"{obj}"
        f"\n\n\033[1;35mtype:\033[1;m "
        f"{type(obj)}"
        f"\n\n\033[1;35m__doc__:\033[1;m "
        f"{obj.__doc__}"
        f"\n{'_' * 75}"
    )
