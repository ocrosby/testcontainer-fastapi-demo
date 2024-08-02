from pytest_bdd import scenario, given, when, then, parsers


@scenario('../../features/post.feature', 'Create a new post')
def create_new_post():
    pass


@scenario('../../features/post.feature', 'Retrieve all posts')
def retrieve_all_posts():
    pass


@scenario('../../features/post.feature', 'Retrieve a post by ID')
def retrieve_post_by_id():
    pass


@scenario('../../features/post.feature', 'Update a post by ID')
def update_post_by_id():
    pass


@scenario('../../features/post.feature', 'Delete a post by ID')
def delete_post_by_id():
    pass


