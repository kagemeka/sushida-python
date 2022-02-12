# sushida-py
The RPA tool for Sushida with Python


# Environment
- ubuntu:20.04
- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/install/)


# Usage
## start
```sh
$ xhost + \
  && cd ./env/docker/ \
  && docker-compose up
```

## stop forcely
```sh
$ docker-compose down
```


## Sample result
The screenshot of the result is saved as `data/result.png`
after the program done successfly.
![score](./docs/static/score.png)
![rank](./docs/static/rank.png)
