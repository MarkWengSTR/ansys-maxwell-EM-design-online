def spec_present(ctx):
    if bool(ctx["request"]):
        return True
    else:
        ctx["error"]["validate"]["msg"] = "no data"
        return False


def data_type_validate(ctx):
    for v in ctx["request"].values():
        if not type(v) == int or type(v) == float:
            ctx["error"]["validate"]["msg"] = "not validate data type"
            return False
    return True


def spec_keys_validate(ctx):
    if sorted(ctx["request"].keys()) == sorted(
            ["stator_OD_limit", "max_power", "voltage_dc", "max_torque_nm", "max_speed_rpm"]):
        return True
    else:
        ctx["error"]["validate"]["msg"] = "not validate keys"
        return False


def ansys_overload_check(ctx):
    process = ctx["process"]

    if process["count"] <= process["limit"]:
        return True
    else:
        ctx["error"]["validate"]["msg"] = "ansys over loading"
        return False
