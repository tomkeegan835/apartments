def tuplify(data):
    return (data['url'], data['price'], data['title'], data['neighborhood'], data['stats']['bedrooms'], data['stats']['sqft'], data['postid'], data['postDatetime'])
