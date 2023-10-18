用[QDUOJ](https://github.com/QingdaoU/OnlineJudge)作为毕设并且将其二次开发（CUSTOJ，里面有CUSTOJ的元素）成可以运行版本，脱离了docker，现将数据脱敏并开源出来供大家使用。

里面的内容根据毕设的需要，删除了一些，但是我只删除了前端的元素，所以如果想用QDUOJ的原版OJ的话，可以直接替换vue文件回去（QDUOJ原生的前端有问题，无法直接运行，这里我做了修改）。

运行

```shell
docker-compose up -d
./run.sh
```

作者：laris

QQ：1292199899