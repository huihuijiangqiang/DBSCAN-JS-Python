# DBSCAN-JS-Python
javascript实现DBSCAN算法

使用python``sklearn.datasets``的``make_moons``生成数据集

算法使用javascript实现

具体代码

```javascript
  function DBSCAN(key, obj) {
        if (!obj[Number(key)].vis) {//如果未被访问，则执行
            obj[key].vis = true;
            var sum = 0;//计数
            var brr = [];//计算密度范围内的点
            for (const j in obj) {
                //计算欧式距离 pow返回x的y次幂
                var c = Math.pow(obj[key][0] - obj[j][0], 2);
                var d = Math.pow(obj[key][1] - obj[j][1], 2);
                var e = Math.pow(c + d, 0.5);
                //是否满足给定的eps
                if (e < this.Eps) {
                    sum++;
                    brr.push(j);
                }
            }
            if (sum > this.MinPts) {//满足密度条件
                obj[key].cluster = this.Clusterid;//标记簇序号
                for (m in brr) {//对密度范围内所有点递归
                    this.DBSCAN(brr[m], obj);
                }
                return true;
            } else {//不满足密度条件
                sum = 0;//计数清空
                brr.length = 0;//存储的点清空
                return false;
            }
        }
    }
```
