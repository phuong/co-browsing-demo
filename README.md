# co-browsing-demo
Clone project
```sh
# Clone main repo
git@github.com:phuong/co-browsing-demo.git

# Clone submodule
cd co-browsing-demo
git submodule update --init --recursive
```

Start api server (you can use current vs environment)


	uvicorn api:app --reload --port 8011 --host 0.0.0.0

Build the bundle

```sh
cd syncit/packages/ui
npm install
npm run-script build
cd public
```

Edit app.html: update new transporter

```js
new syncit.App({
        target: document.body,
        props: {
          createTransporter({ role, uid }) {
            return new syncitTransporter.WebSocketTransporter({
              role,
              uid,
              url: 'ws://localhost:8011/ws/any_client_id'
            });
          },
        },
});

```


Edit the embed.html and update to the new transporter

```js

new syncit.App({
        target: document.body,
        props: {
          createTransporter({ role, uid }) {
            return new syncitTransporter.WebSocketTransporter({
              role,
              uid,
              url: 'ws://localhost:8011/ws/any_client_id'
            });
          },
        },
});
```

Open app.html and embed.html in browsers and play. If you get issue with CORS, please use [Node serve](https://www.npmjs.com/package/serve) 
or [python simple http server](https://www.hackerearth.com/practice/notes/simple-http-server-in-python/) to serve public directory as a "localhost" website.

