def join_tuples_to_string(strings_tuple) -> str:
    return " -> ".join(strings_tuple)


country_names = input().split(", ")
city_names = input().split(", ")
country_capitals_list = zip(country_names, city_names)
result = map(join_tuples_to_string, country_capitals_list)
final = [print(item) for item in result]
# for country_city in result:
#     lst = country_city.split()
#     # final_result = " -> ".join(lst)
#     print(final_result)
