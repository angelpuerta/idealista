from client.search.builder import basic_filter
from client.search.search_service import search_service
from client.search.builder.geo_query_builder import from_city
from client.search.builder.query_builder import sales_spain, rent_spain
from client.search.search_request import SearchRequest

request = SearchRequest(sales_spain(), from_city('Madrid', 5000))
request.add_filter(basic_filter.basic_filter(100000, 30, 280000))
request
# iterator = search_service.query_iterator(request, limit=100)
# for i in iterator :
#    print(i)

request = SearchRequest(rent_spain(), from_city('Madrid', 5000))
request.add_filter(basic_filter.basic_filter(400, 30, 1500))
request
# iterator = search_service.query_iterator(request, limit=100)
