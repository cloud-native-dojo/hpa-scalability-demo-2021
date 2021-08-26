# cloud-native-dojo-2021

Build container

```
docker build -t myapp:v0.1.1 .
```

Start container

```
docker run -d -p 5000:5000 --rm myapp:v0.1.1
```

Access container

```
curl localhost:5000
```
