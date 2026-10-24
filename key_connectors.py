users=[{"id":0,"name":"hero"},
{"id":1,"name":"Arthur"},
{"id":2,"name":"Amy"},
{"id":3,"name":"Abel"},
{"id":4,"name":"Priya"},
{"id":5,"name":"Ziva"},
{"id":6,"name":"Finn"},
{"id": 7, "name": "Sherlock"},
{"id": 8, "name": "Kate"},
{"id": 9, "name": "Kevin"}]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
friendships={user["id"]:[] for user in users}
for i,j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
def number_of_friends(user):
    user_id=user["id"]
    friend_ids=friendships[user_id]
    return len(friend_ids)
total_con=sum(number_of_friends(user) for user in users)
num_users=len(users)
avg_con=total_con/num_users
num_friends_by_id=[(user["id"],number_of_friends(user)) for user in users]
num_friends_by_id.sort(key=lambda id_and_friends:id_and_friends[1],reverse=True)
#the key function extracts index[1]that is the friend count from each tuple to determine the sort order
       
print(total_con)
print(num_users)
print(avg_con)
print(num_friends_by_id)
