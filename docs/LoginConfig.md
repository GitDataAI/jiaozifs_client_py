# LoginConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rbac** | **str** | RBAC will remain enabled on GUI if \&quot;external\&quot;.  That only works with an external auth service.  | [optional] 
**login_url** | **str** | primary URL to use for login. | 
**login_failed_message** | **str** | message to display to users who fail to login; a full sentence that is rendered in HTML and may contain a link to a secondary login method  | [optional] 
**fallback_login_url** | **str** | secondary URL to offer users to use for login. | [optional] 
**fallback_login_label** | **str** | label to place on fallback_login_url. | [optional] 
**login_cookie_names** | **list[str]** | cookie names used to store JWT | 
**logout_url** | **str** | URL to use for logging out. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

