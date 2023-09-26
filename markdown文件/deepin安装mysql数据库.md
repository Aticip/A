# deepin安装mysql数据库

## 第一步

- 如果此时deepin没有软件源，需要先在官网下载mysql的软件包，[Mysql社区版最新地址](https://dev.mysql.com/downloads/mysql/) 。
- Select Operating System 和 Select OS Version 需要根据自己电脑进行选择，前者如果没有特定的版本，例如deepin，则选择Generic，后者根据cpu进行选择，x86或者arm以及32位或是64位的操作系统。
- 选择第一个进行下载。

<img src="/home/Sun/Pictures/Screenshots/截图_选择区域_20230926220001.png" style="zoom: 50%;" />

##  第二步

1. 找到刚才下载的软件包，进入所在目录执行如下命令，将其解压至/usr/local目录下。

   ```
   sudo tar -xvJf mysql-8.1.0-linux-glibc2.28-x86_64.tar.xz -C /usr/local
   ```

​		<!--如果下载的软件包不同，请将命令中的包名更换成自己的-->

2. 进入/usr/local目录下

   ```3
   cd /usr/local
   ```

3. 创建软链接方便操作
    ```
    sudo ln -s mysql-8.1.0-linux-glibc2.28-x86_64.tar.xz mysql
    ```

## 第三步

- 创建mysql用户和用户组

  ```
  sudo useradd -r -s /bin/false mysql
  
  # -s /bin/false 参数指定 mysql 用户仅拥有所有权，而没有登录权限
  # 这里不用添加mysql组了，会有默认的mysql组
  ```

- 进入mysql目录

  ```
  cd /usr/local/mysql
  ```

- 在该mysql目录下建立data目录，用于存放mysql数据

  ```
  sudo mkdir /usr/local/mysql/data
  ```

- 修改mysql目录的所有者为mysql

  ```
  sudo chown -R mysql:mysql ./
  ```

- 安装

  ```
  sudo ./bin/mysqld --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data --initialize 
  ```

**安装成果后会有如下显示**

> [Server] A temporary password is generated for root@localhost: sL:maY*3y6)d

## 第四步

- 将mysql放入系统进程中，若未启动mysql则选择启动命令

  ```
  sudo cp support-files/mysql.server /etc/init.d/mysqld
  service mysqld start       #mysql启动命令
  service mysqld restart     #mysql重新启动命令
  ```

- 在 /usr/bin 下建立指向 mysql 的软连接之后使用随机密码登录 mysql 数据库

  **注意保存密码，如sL:maY*3y6)d，在登录时输入即可**
	```
	sudo ln -s /usr/local/mysql/bin/mysql /usr/bin
	
	mysql -u root -p
	```

- 进入mysql后，为root用户设置新的密码

  ```
  alter user 'root'@'localhost' identified by '123456';
  ```

### 以后登录mysql需要先启动，然后输入登录命令

