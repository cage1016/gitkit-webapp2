gitkit-webapp2
==============

This is a simple gitkit (Google identity toolkit) demo via GAE python webapp2 framework

###Getting Started

####Step 1: Clone repo.

```sh
git clone https://github.com/cage1016/gitkit-webapp2
```

####Step 2: install packages.

install python third-party libraries

```sh
sudo python install -r requestments.txt -t lib
```

####Step 3: Create GAE project

Please visit your [Google Developers Console](https://console.developers.google.com/project) and choose one project or create new one project.

Create client id for web application

1.	Click **APIs & Auth** > **credential**.
2.	Click **Click new Client ID**.
3.	Choose **Web application**.
4.	modify **Authorized JavaScript origins**.

	```sh
	http://localhost:8080
	```

5.	modify **Authorized redirect URIs**.

	```sh
	http://localhost:8080/widget
	```

6.	Click **Create Client ID**

Create Service Account

1.	Click **APIs & Auth** > **credential**.
2.	Click **Click new Client ID**.
3.	Choose **Service Account**.
4.	Key type : **P12 Key**
5.	Click **Create Client ID**
6.	**P12.Key** file will be downloaded. You have to convert `p12` to `pem` cause PKCS12 format is not supported by the PyCrypto library.

	```sh
	(openssl pkcs12 -in xxxxx.p12 -nodes -nocerts > privatekey.pem)
	```

Create Public API access

1.	Click **APIs & Auth** > **credential**.
2.	Click **Click new Key** in **Public API access** section
3.	Click **Browser key**
4.	Click **Create**

####Step 4

Enable **Identity Toolkit API** and setup

1.	Click **APIs & Auth** > **APIs** > **API Library**.
2.	Search **Identity Toolkit API** and turn it on.
3.	switch **Enabled APIs** and Click **Identity Toolkit API** setting icon.
4.	Click **API Configuration**
5.	Click **origin console**. you will swtich old google console
6.	Fill the Identity Toolkit setting
	-	set Sign-in Success URL: **/signin**
	-	set Sign-out URL: **/logou**
	-	set Send Email URL: **/**
7.	Click Server-side configuration file **Download** to download `gitkit-server-config.json`

	```sh
	{
	  "clientId" : "<your-client-id>",
	  "serviceAccountEmail" : "<your-service-account-email>",
	  "serviceAccountPrivateKeyFile" : "INSERT/PATH/TO/PRIVATEKEY",
	  "widgetUrl" : "http://localhost:8080/gitkit",
	  "cookieName" : "gtoken"
	}
	```

	modify `INSERT/PATH/TO/PRIVATEKEY` with `<your-pem-file>` path you just converted.

8.	Fill the Facebook **ClientID** and **Secret key** if you want to gitkit support faebook signin.

####Step 5

modify `templates/widget` as `<your-public-api-key>` your created

```javascript
var config = {
    apiKey: '<your-public-api-key>',
    signInSuccessUrl: '/signin',
    idps: ["google"],
    oobActionUrl: '/',
```

####Step 6

You can run gitkit locally now

```sh
dev_appserver.py .
```

###Reference

1.	[Introduction - Google Identity Toolkit — Google Developers](https://developers.google.com/identity-toolkit/)
2.	[google/identity-toolkit-python-client](https://github.com/google/identity-toolkit-python-client)
3.	[GoogleCloudPlatform/abelana-gcp](https://github.com/GoogleCloudPlatform/abelana-gcp)
