# FakeApis
code to quicky generate fake api

Usage 
> python StatusGeneric.py -code int_status_code_to_return -content message_content

Example:
> python StatusGeneric.py -code 403

> python StatusGeneric.py -code 403 -content "error in code"


Make a GET request to any path of format http://FakeApisIPAddress:FakeApisPort/api/any_entity_name

Example: 
> http://localhost:5000/api/anyentityname

And result will be based on you command arguments
