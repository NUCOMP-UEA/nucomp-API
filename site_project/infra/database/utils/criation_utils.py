def update_info(user_info):
    user_copy = user_info.copy()
    user_dict = user_copy.dict()
    user_dict["id_"] = str(user_dict["id_"])
    del user_dict["user_type"]
    return user_dict
