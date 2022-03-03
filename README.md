# HTTP-Request
Use Flask and OkHttp to make HTTP Request from server

## Installing 
- Install Flask `pip install flask`

## Add Android Dependencies in build.gradle
`implementation("com.squareup.okhttp3:okhttp:4.9.0")`

## Add uses permission to AndroidManifest.XML
- (above application tag) 'uses-permission android:name="android.permission.INTERNET"/'
- (inside application tag) 'android:usesCleartextTraffic="true">'

## Opening Server with Flask in Python 
- Create server homepage route `@app.route("/")`
- Host server on machine's IP with `app.run(host="0.0.0.0")`

## Create OkHttp Client Request 
`OkHttpClient okhttpclient = new OkHttpClient();`

## Create Request with Server URL
`Request request = new Request.Builder().url("http://192.168.0.113:5000/").build();`

## Access Server Response 
`response.body().string;`
