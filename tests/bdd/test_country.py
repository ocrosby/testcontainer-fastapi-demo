from pytest_bdd import scenario


@scenario('../../features/country.feature', 'Retrieve a list of countries')
def test_retrieve_a_list_of_countries():
    pass


@scenario('../../features/country.feature', 'Retrieve a single country by ID')
def test_retrieve_a_single_country_by_id():
    pass


@scenario('../../features/country.feature', 'Create a new country')
def test_create_a_new_country():
    pass


@scenario('../../features/country.feature', 'Update an existing country')
def test_update_an_existing_country():
    pass


@scenario('../../features/country.feature', 'Delete an existing country')
def test_delete_an_existing_country():
    pass


@scenario('../../features/country.feature', 'Delete a country that does not exist')
def test_delete_a_country_that_does_not_exist():
    pass
