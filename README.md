Environment Variable Manager (evm)
==================================

CLI tool for centralizing environment variables.


Use Case
--------

My team works with several related but separate projects that share the same environment variables. We use [Codeship](https://codeship.com/) for continuous deployment, and we store the environment variables for each project as part of the Codeship project's settings.

We had three problems with this:

1. *Duplication* - The same variable is stored in different places and if we want to change it, we have to go over all the projects that use it.
2. *Error-prone* - Management of these variables is a nightmare. If we want to update a variable, we have to copy-paste the new value to all the projects that use it.
3. *No revision handling* - If we set a variable to the wrong value accidentally, there's no way we can get the original value back. 
 
 
Solution
--------

We store those environment variables in the cloud (e.g. AWS DynamoDB), let `evm` retrieve those variables during the build/deploy process, then make `evm` generate a shell script that we can `source` in our build/deploy script.

Instead of duplicating the same environment variables in each Codeship project, we now have a centralized, DRY approach for managing these variables. Each project will now refer to the same variable.

To support revisions, whenever we set a new value for an existing variable, we simply archived the old value. This way, we can always go back to it if we need to.


Limitations
-----------

At this stage, this tool is still a "proof-of-concept". It still needs more work to make it more flexible and robust.


TODOs
-----

* Setup and usage instructions
* Support for multiple stages/regions (e.g. *staging* and *production* use the same variables but different values)
* Support for other backends (e.g. sqlite, [Google Datastore](https://cloud.google.com/datastore/))
* Test Coverage with Travis CI
* PyPI package
