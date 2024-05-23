Playing around with spotify-auth-flow. Currently it is designed to adhere to the [credentials flow](https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow) as well as the authentication code flow described in [this](https://developer.spotify.com/documentation/general/guides/authorization-guide/) article. It is designed for use with flask, but can be easily modified to work with any other framework as well. The code below shows how the client would make a request and get an access token.

A post request is made to `/api/token`with the necessary headers and grant type. The token is then stored using the flask session object and used in subsequent requests. NOTE: Client credentials is useful for server to server communication, but if you were wanting to authorize users in a web app, using OAuth2 would be more appropriate. Per the documentaiton:

```
req.body {
	grant_type: 'authorization_code',
	code: AUTH_CODE sent from auth server
	redirect_uri: redirect_uri from original request,
	client_id: from app
	code_verifier: random hash
}
// HTTP Headers
req.headers {
	Authorization: Basic <base64 encoded client_id:client_secret>, toString('base64')
	Content-Type: Set to `application/x-www-form-urlencoded`.
}

```

The response will contain an access_token and refresh_token that you can reference in client

![](https://developer.spotify.com/images/documentation/web-api/auth-code-flow.png)

(A) The client initiates the flow by directing the resource owner's
user-agent to the authorization endpoint. The client includes
its client identifier, requested scope, local state, and a
redirection URI to which the authorization server will send the
user-agent back once access is granted (or denied).

(B) The authorization server authenticates the resource owner (via
the user-agent) and establishes whether the resource owner
grants or denies the client's access request.

(C) Assuming the resource owner grants access, the authorization
server redirects the user-agent back to the client using the
redirection URI provided earlier (in the request or during
client registration). The redirection URI includes an
authorization code and any local state provided by the client
earlier.

(D) The client requests an access token from the authorization
server's token endpoint by including the authorization code
received in the previous step. When making the request, the
client authenticates with the authorization server. The client
includes the redirection URI used to obtain the authorization
code for verification.

(E) The authorization server authenticates the client, validates the
authorization code, and ensures that the redirection URI
received matches the URI used to redirect the client in
step (C). If valid, the authorization server responds back with
an access token and, optionally, a refresh token.

This provides a layer between the resource owner and the client. The user needs to gain authorization to request a token.
