from exercise import city_country, city_country_population
def test_city_country():
    formatted_city_country = city_country('santigo', 'chile')
    assert formatted_city_country == 'santigo, chile'
def test_city_country_population():
    formatted_city_country_population = city_country_population(
        'santigo', 'chile', '5000000'
    )
    assert formatted_city_country_population == 'santigo, chile - population 5000000'