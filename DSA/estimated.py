def get_estimated_spread(audiences_followers):
    if not audiences_followers:
        return None
    counter = 0
    num_followers = len(audiences_followers)
    for i in audiences_followers:
        counter += i

    average_audience_followers = counter / num_followers
    estimated_spread = average_audience_followers * ( num_followers ** 1.2 )

    return estimated_spread

print(get_estimated_spread([]))
print(get_estimated_spread([2, 3, 2, 19]))

