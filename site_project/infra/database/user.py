def search_users_by_email(db, email):
    pipeline = [
        {
            "$lookup": {
                "from": "students",
                "localField": "email",
                "foreignField": "email",
                "as": "students",
            }
        },
        {
            "$lookup": {
                "from": "coordinators",
                "localField": "email",
                "foreignField": "email",
                "as": "coordinators",
            }
        },
        {
            "$lookup": {
                "from": "teachers",
                "localField": "email",
                "foreignField": "email",
                "as": "teachers",
            }
        },
        {
            "$project": {
                "users": {"$concatArrays": ["$students", "$coordinators", "$teachers"]}
            }
        },
        {"$unwind": "$users"},
        {"$replaceRoot": {"newRoot": "$users"}},
        {"$match": {"email": email}},
    ]

    result = db.users.aggregate(pipeline)
    return list(result)
