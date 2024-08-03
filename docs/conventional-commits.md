# Conventional Commits

This project uses [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) to standardize the commit messages. This convention follows the [Semantic Versioning](https://semver.org/) specification.

The commit message should be structured as follows:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

The `type` is required and must be one of the following:

Here I am following the [Angular convention for commit messages](https://github.com/angular/angular/blob/68a6a07/CONTRIBUTING.md#commit

- `build`: Changes that affect the build system or external dependencies (example scopes: pip, docker, etc.)
- `ci`: Changes to our CI configuration files and scripts (example scopes: GitLab CI, GitHub Actions, etc.)
- `chore`: Other changes that don't modify src or test files
- `docs`: Documentation only changes
- `feat`: A new feature
- `fix`: A bug fix
- `perf`: A code change that improves performance
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests

The `scope` is optional and can be anything specifying the place of the commit change.

The `description` is required and should be clear and concise.

The `body` is optional and can provide more detailed information about the commit.

The `footer` is optional and can be used to reference issues or pull requests.

Here are some examples of conventional commits:

```text
feat: add new endpoint for user registration

feat(user): add new endpoint for user registration
```

### Scope

The scope can be anything specifying the place of the commit change. For example, `user`, `auth`, `api`, `db`, etc.

Each application is going to have a set of scopes that are specific to it. For example, a web application might have `auth`, `user`, `admin`, etc. A mobile application might have `auth`, `user`, `settings`, etc.

I am going to try to document the scopes I settle on [here](scopes.md), for the purposes of this Demo project.

To ensure that the commit messages are formatted correctly, you can use the `commitlint` tool. The configuration for `commitlint` is provided in the `.commitlintrc.json` file.

## References

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Semantic Versioning](https://semver.org/)
- [Commitlint](https://commitlint.js.org/)'
- [Angular Commit Message Conventions](https://github.com/angular/angular/blob/68a6a07/CONTRIBUTING.md#commit)